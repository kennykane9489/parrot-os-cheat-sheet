"""Regression checks for invalid documents and non-execution of examples."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

script = Path(__file__).resolve().parents[1] / 'scripts' / 'check_docs.py'
spec = importlib.util.spec_from_file_location('checker', script)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class CheckDocsTests(unittest.TestCase):
    def fixture(self, text):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / 'README.md').write_text(text, encoding='utf-8')
        return root

    def test_valid(self):
        root = self.fixture('# Home\n\n[Topic](topic.md#one)\n\n```bash\nprintf hi\n```\n')
        (root / 'topic.md').write_text('# Topic\n\n## One\n', encoding='utf-8')
        self.assertEqual(checker.check(root)[0], [])

    def test_missing_file(self):
        root = self.fixture('# Home\n\n[Missing](missing.md)\n')
        self.assertTrue(any('missing local target' in e for e in checker.check(root)[0]))

    def test_missing_anchor(self):
        root = self.fixture('# Home\n\n[Missing](#absent)\n')
        self.assertTrue(any('missing anchor' in e for e in checker.check(root)[0]))

    def test_unclosed_fence(self):
        root = self.fixture('# Home\n\n```bash\nprintf hi\n')
        self.assertTrue(any('unclosed code fence' in e for e in checker.check(root)[0]))

    def test_shell_error(self):
        root = self.fixture('# Home\n\n```bash\nif then\n```\n')
        self.assertTrue(any('invalid Bash syntax' in e for e in checker.check(root)[0]))

    def test_examples_not_executed(self):
        root = self.fixture('# Home\n')
        marker = root / 'must-not-exist'
        (root / 'README.md').write_text(f'# Home\n\n```bash\ntouch "{marker}"\n```\n', encoding='utf-8')
        self.assertEqual(checker.check(root)[0], [])
        self.assertFalse(marker.exists())

    def test_link_outside_root(self):
        root = self.fixture('# Home\n\n[Outside](../outside.md)\n')
        self.assertTrue(any('escapes repository' in e for e in checker.check(root)[0]))

    def test_duplicate_heading(self):
        root = self.fixture('# Home\n\n## Same\n\n## Same\n\n[Second](#same-1)\n')
        self.assertEqual(checker.check(root)[0], [])

    def test_details(self):
        root = self.fixture('# Home\n\n<details>\n<summary>More</summary>\n')
        self.assertTrue(any('unbalanced details' in e for e in checker.check(root)[0]))


if __name__ == '__main__':
    unittest.main()
