import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('evidence',ROOT/'tools/evidence.py')
evidence=importlib.util.module_from_spec(spec)
spec.loader.exec_module(evidence)

class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for path in ['tools/evidence.py','cases/tooling/input.json','paper/main.tex']:
            target=self.root/path
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy(ROOT/path,target)
        evidence.generate(self.root,self.root/'paper/generated')
    def test_clean_regeneration(self):
        evidence.check(self.root)
    def test_corrupted_artifact_fails(self):
        for name in evidence.PRODUCTS:
            with self.subTest(name=name):
                evidence.generate(self.root,self.root/'paper/generated')
                with (self.root/'paper/generated'/name).open('a') as f:f.write('corrupt')
                with self.assertRaisesRegex(ValueError,'stale or corrupt'):evidence.check(self.root)
    def test_changed_input_fails(self):
        path=self.root/'cases/tooling/input.json'
        config=json.loads(path.read_text()); config['panels']=256
        path.write_text(json.dumps(config))
        with self.assertRaisesRegex(ValueError,'stale or corrupt'):evidence.check(self.root)
    def test_changed_producer_fails(self):
        with (self.root/'tools/evidence.py').open('a') as f:f.write('\n# changed\n')
        with self.assertRaisesRegex(ValueError,'stale or corrupt'):evidence.check(self.root)
    def test_unknown_result_fails(self):
        with (self.root/'paper/main.tex').open('a') as f:f.write(r'\result{Nonexistent}')
        with self.assertRaisesRegex(ValueError,'undefined result'):evidence.check(self.root)
    def test_typed_result_fails(self):
        with (self.root/'paper/main.tex').open('a') as f:f.write('Measured value 0.333.')
        with self.assertRaisesRegex(ValueError,'bare numeric'):evidence.check(self.root)
    def test_untracked_include_fails(self):
        with (self.root/'paper/main.tex').open('a') as f:f.write(r'\input{untracked.tex}')
        with self.assertRaisesRegex(ValueError,'source contract'):evidence.check(self.root)
    def test_unknown_citation_fails(self):
        with (self.root/'paper/main.tex').open('a') as f:f.write(r'\cite{InventedKey}')
        with self.assertRaisesRegex(ValueError,'undefined citation'):evidence.check(self.root)
    def test_duplicate_citation_key_fails(self):
        path=self.root/'paper/main.tex'
        text=path.read_text().replace(r'\end{thebibliography}',r'\bibitem{APS2026} duplicate\end{thebibliography}')
        path.write_text(text)
        with self.assertRaisesRegex(ValueError,'duplicate bibliography'):evidence.check(self.root)
    def test_wrong_computation_fails(self):
        config=json.loads((self.root/'cases/tooling/input.json').read_text())
        with self.assertRaisesRegex(ValueError,'acceptance failed'):evidence.calculate(config,broken=True)
    def test_refinement_reduces_error(self):
        config=json.loads((self.root/'cases/tooling/input.json').read_text())
        coarse=evidence.calculate(config)['IntegralError']; config['panels']*=2
        fine=evidence.calculate(config)['IntegralError']
        self.assertAlmostEqual(coarse/fine,4)

if __name__=='__main__':unittest.main()
