"""Offline checks of the public ports, including negative and actual CLI paths."""
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


CITATION = module('public_citation', 'skills/cite-and-verify/scripts/citation_mvf.py')
LEDGER = module('public_ledger', 'skills/cite-and-verify/scripts/validate_claim_ledger.py')
RESULTS = module('public_results', 'skills/result-provenance/scripts/texresults.py')


class CitationTests(unittest.TestCase):
    def test_title_candidate_is_not_verified(self):
        payload = {'meta': {'count': 1}, 'results': [{'title': 'Exact title', 'doi': 'example'}]}
        with patch.object(CITATION, '_req', return_value=payload), patch.object(CITATION, '_cache_load', return_value=None), patch.object(CITATION, '_cache_save'), patch.object(CITATION, '_delay'):
            self.assertEqual(CITATION.verify_title('Exact title', {})['status'], 'low_confidence')

    def test_low_confidence_never_counts_as_verified(self):
        with patch.object(CITATION, 'verify_citation', return_value={'status': 'low_confidence', 'identifier': 'example'}):
            report = CITATION.batch_verify([{'id': 'example'}])
        self.assertEqual(report['stats']['verified'], 0)
        self.assertEqual(report['stats']['low_confidence'], 1)

    def test_timeout_records_every_unprocessed_input(self):
        report = CITATION.batch_verify([{'id': 'one'}, {'id': 'two'}], timeout=-1)
        self.assertEqual(report['stats']['skipped'], 2)
        self.assertEqual(len(report['citations']), 2)

    def test_identifier_title_mismatch(self):
        with patch.object(CITATION, 'verify_citation', return_value={'status': 'verified', 'title': 'Completely unrelated work'}):
            report = CITATION.batch_verify([{'id': 'example', 'expected_title': 'An intended calculation'}])
        self.assertEqual(report['stats']['mismatch'], 1)
        self.assertEqual(report['stats']['verified'], 0)

    def test_malformed_doi_and_wrong_arxiv_identity_are_not_verified(self):
        with patch.object(CITATION, '_req', return_value={'status': 'ok', 'message': {}}), patch.object(CITATION, '_cache_load', return_value=None), patch.object(CITATION, '_cache_save'), patch.object(CITATION, '_delay'):
            self.assertNotEqual(CITATION.verify_doi('10.0000/example', {})['status'], 'verified')
        from unittest.mock import MagicMock
        xml=b'<feed xmlns="http://www.w3.org/2005/Atom" xmlns:o="http://a9.com/-/spec/opensearch/1.1/"><o:totalResults>1</o:totalResults><entry><id>http://arxiv.org/abs/9999.99999v1</id><title>Unrelated title</title></entry></feed>'
        response=MagicMock();response.__enter__.return_value.read.return_value=xml
        with patch.object(CITATION.urllib.request, 'urlopen', return_value=response), patch.object(CITATION, '_cache_load', return_value=None), patch.object(CITATION, '_cache_save'), patch.object(CITATION, '_delay'):
            self.assertNotEqual(CITATION.verify_arxiv('0000.00000', {})['status'], 'verified')

    def test_positive_identifier_metadata_and_encoded_ads_query(self):
        payload={'status': 'ok', 'message': {'DOI': '10.0000/example', 'title': ['Intended title']}}
        with patch.object(CITATION, '_req', return_value=payload), patch.object(CITATION, '_cache_load', return_value=None), patch.object(CITATION, '_cache_save'), patch.object(CITATION, '_delay'):
            self.assertEqual(CITATION.verify_doi('10.0000/example', {})['status'], 'verified')
        bibcode='2020A&A...641A...6P'
        payload={'response': {'numFound': 1, 'docs': [{'bibcode': bibcode, 'title': ['Intended title']}]}}
        with patch.object(CITATION, '_req', return_value=payload) as request, patch.object(CITATION, '_cache_load', return_value=None), patch.object(CITATION, '_cache_save'), patch.object(CITATION, '_delay'):
            self.assertEqual(CITATION.verify_ads(bibcode, {}, 'synthetic-sentinel-only')['status'], 'verified')
            query=CITATION.urllib.parse.parse_qs(CITATION.urllib.parse.urlsplit(request.call_args.args[0]).query)
            self.assertEqual(query['q'], [f'bibcode:"{bibcode}"'])

    def test_provider_error_is_not_absence(self):
        with patch.object(CITATION, '_req', return_value={'_request_error': True, '_http_status': 503}), patch.object(CITATION, '_cache_load', return_value=None), patch.object(CITATION, '_cache_save'), patch.object(CITATION, '_delay'):
            self.assertEqual(CITATION.verify_doi('10.0000/example', {})['status'], 'error')

    def test_failed_identifier_title_fallback_is_unresolved(self):
        with patch.object(CITATION, 'verify_doi', return_value={'status': 'not_found'}), patch.object(CITATION, 'verify_title', return_value={'status': 'verified', 'matched_title': 'An exact title'}):
            result = CITATION.verify_citation('10.0000/example', 'doi', {}, title_fallback='An exact title')
        self.assertEqual(result['status'], 'low_confidence')
        self.assertEqual(result['primary_lookup']['status'], 'not_found')

    def test_missing_ads_cli_fails_without_network(self):
        env = dict(os.environ)
        env.pop('ADS_API_TOKEN', None)
        with tempfile.TemporaryDirectory() as tmp:
            data = Path(tmp)/'input.json'; report = Path(tmp)/'report.json'
            data.write_text(json.dumps([{'id': '2016PhRvL.116f1102A', 'type': 'ads'}]))
            process = subprocess.run([sys.executable, str(ROOT/'skills/cite-and-verify/scripts/citation_mvf.py'), '--input', str(data), '--output', str(report), '--summary'], env=env, capture_output=True, text=True)
            self.assertEqual(process.returncode, 1)
            self.assertNotIn('Traceback', process.stderr)
            self.assertEqual(json.loads(report.read_text())['stats']['skipped'], 1)

    def test_old_cache_schema_is_ignored(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(CITATION,'CACHE_DIR',Path(tmp)):
            key=CITATION._cache_key('doi','10.0000/example');file=Path(tmp)/key[:2]/(key+'.json');file.parent.mkdir()
            file.write_text(json.dumps({'status':'verified','title':None,'_cached_at':CITATION.datetime.now().isoformat()}))
            self.assertIsNone(CITATION._cache_load(key))
            CITATION._cache_save(key,{'status':'verified','title':'An exact title'})
            self.assertEqual(CITATION._cache_load(key)['title'],'An exact title')

    def test_credential_transport_refuses_redirect_and_wrong_host(self):
        req=CITATION.urllib.request.Request('https://other.invalid/',headers={'Authorization':'Bearer synthetic-sentinel'})
        with patch.object(CITATION.urllib.request,'urlopen') as opened:
            with self.assertRaises(CITATION.urllib.error.URLError):CITATION._safe_urlopen(req)
            opened.assert_not_called()
        req=CITATION.urllib.request.Request('https://api.adsabs.harvard.edu/',headers={'Authorization':'Bearer synthetic-sentinel'})
        with self.assertRaises(CITATION.urllib.error.URLError):
            CITATION._NoCredentialRedirect().redirect_request(req,None,302,'redirect',{},'https://other.invalid/')

    def test_empty_cli_input_cannot_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            data=Path(tmp)/'input.json'; data.write_text('[]')
            process=subprocess.run([sys.executable, str(ROOT/'skills/cite-and-verify/scripts/citation_mvf.py'), '--input', str(data)], capture_output=True, text=True)
            self.assertNotEqual(process.returncode, 0)


class ClaimLedgerTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/'skills/cite-and-verify/examples/claim-ledger.json').read_text())

    def test_explicitly_blocked_example_is_structurally_valid(self):
        self.assertEqual(LEDGER.validate(self.data), [])

    def test_empty_ledger_and_duplicate_ids_fail(self):
        self.assertTrue(LEDGER.validate({'schema': 'openclaw.claim-ledger.v1', 'claims': []}))
        self.data['claims'].append(copy.deepcopy(self.data['claims'][0]))
        self.assertTrue(LEDGER.validate(self.data))

    def test_verified_without_support_or_sources_fails(self):
        self.data['claims'][0].update(disposition='verified', identity_status='verified')
        self.assertTrue(LEDGER.validate(self.data))

    def test_human_assertion_requires_named_human(self):
        self.data['claims'][0].update(disposition='human-asserted', support_status='human-verified')
        self.assertTrue(LEDGER.validate(self.data))
        for bad in ({}, '  '):
            self.data['claims'][0]['human_verifier']=bad
            self.assertTrue(LEDGER.validate(self.data))
        self.data['claims'][0]['human_verifier']='example-human'
        self.assertEqual(LEDGER.validate(self.data), [])


class ResultLoggerTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name); self.source=self.root/'producer.py'; self.source.write_text('print(0.5)\n')
        self.path=self.root/'macros_results.tex'
        self.run={'completed': True, 'command': 'python producer.py', 'code_revision': 'example-revision', 'environment': 'python-stdlib', 'scope': 'synthetic scalar', 'configuration': {}, 'inputs': [{'id': 'analytic-specification', 'sha256': hashlib.sha256(b'synthetic').hexdigest()}]}

    def make_record(self):
        log=RESULTS.ResultsLog(self.path, run=self.run)
        log.set('Example', 0.5, source=str(self.source), fmt='.2f')
        return log

    def test_scalar_and_interval_survive_round_trip(self):
        log=self.make_record();log.set_interval('Interval',0.5,0.4,0.7,source=str(self.source),fmt='.2f');log.write()
        recovered=RESULTS.ResultsLog(self.path)
        self.assertEqual(recovered.render(), self.path.read_text())
        self.assertEqual(recovered.entries['Example']['value'],0.5)
        self.assertEqual(recovered.entries['Interval']['value'],[0.5,0.4,0.7])
        self.assertEqual(recovered.entries['Example']['source_sha256'],hashlib.sha256(self.source.read_bytes()).hexdigest())

    def test_missing_provenance_and_nonfinite_results_fail(self):
        log=self.make_record(); log.entries['Example']['run']['completed']=False
        with self.assertRaises(ValueError):log.write()
        log=self.make_record();log.entries['Example']['value']=float('nan')
        with self.assertRaises(ValueError):log.write()
        log=self.make_record();log.entries['Example']['source_sha256']=None
        with self.assertRaises(ValueError):log.write()

    def test_display_overrides_fail_and_macro_names_are_namespaced(self):
        log=self.make_record();log.entries['Example']['latex']='99'
        with self.assertRaises(ValueError):log.write()
        log=self.make_record();log.set('Lambda', 0.5, source=str(self.source));log.write()
        rendered=self.path.read_text()
        self.assertIn('TASresult@Lambda',rendered)
        self.assertNotIn(r'\csname Lambda\endcsname',rendered)

    def test_reversed_interval_fails(self):
        with self.assertRaises(ValueError):self.make_record().set_interval('Interval',0.5,0.8,0.9,source=str(self.source))

    def test_cli_checks_corruption_and_undefined_use(self):
        log=self.make_record();log.write()
        source=self.root/'paper.tex';source.write_text(r'\result{Example}')
        command=[sys.executable,str(ROOT/'skills/result-provenance/scripts/texresults.py'),'--file',str(self.path),'check',str(source)]
        self.assertEqual(subprocess.run(command,capture_output=True).returncode,0)
        self.path.write_text(self.path.read_text().replace('0.50','0.70'))
        self.assertNotEqual(subprocess.run(command,capture_output=True).returncode,0)
        log.write()
        for use in (r'\result{Absent}', r'\result {Absent}', '\\result% comment\n{Absent}', r'\result Absent'):
            source.write_text(use)
            self.assertNotEqual(subprocess.run(command,capture_output=True).returncode,0)

    def test_cli_recording_requires_manifest(self):
        command=[sys.executable,str(ROOT/'skills/result-provenance/scripts/texresults.py'),'--file',str(self.path),'set','Example','0.5','--source',str(self.source)]
        self.assertNotEqual(subprocess.run(command,capture_output=True).returncode,0)
        manifest=self.root/'run.json';manifest.write_text(json.dumps(self.run))
        command=command[:4]+['--run',str(manifest)]+command[4:]
        self.assertEqual(subprocess.run(command,capture_output=True).returncode,0)


if __name__=='__main__':unittest.main()
