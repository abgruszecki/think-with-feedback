import unittest
from pathlib import Path

from py_shared.io_abstractinator import process_file, _is_def_main, py_parser

TEST_RESOURCES_DIR = Path(__file__).parent/'resources/io_abstractinator'

class TestIoAbstractinator(unittest.TestCase):
    def test_samples_from_directory(self):
        self.assertTrue(TEST_RESOURCES_DIR.exists())

        for sample_dir in TEST_RESOURCES_DIR.iterdir():
            if not sample_dir.is_dir():
                continue

            sample_file = sample_dir / 'sample.py'
            expected_file = sample_dir / 'expected.py'
            got_file = sample_dir / 'got.py'

            with self.subTest(sample=sample_dir.name):
                actual_output = process_file(sample_file)
                self.assertIsNotNone(actual_output)
                got_file.write_text(actual_output)
                expected_output = expected_file.read_text()
                self.assertEqual(actual_output.rstrip(), expected_output.rstrip())

    def test_is_def_main(self):
        def _is_def_main_(src: bytes):
            tree = py_parser.parse(src)
            node = tree.root_node.child(0)
            return _is_def_main(node)

        self.assertTrue(_is_def_main_(b'def main(): pass'))
        self.assertTrue(_is_def_main_(b'@foo\ndef main(): pass'))
        self.assertFalse(_is_def_main_(b'@foo\ndef mains(): pass'))


if __name__ == '__main__':
    unittest.main()