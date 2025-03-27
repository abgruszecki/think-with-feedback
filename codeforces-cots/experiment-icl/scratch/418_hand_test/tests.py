import unittest
import io
import json
import os
from code_uut import main

class TestMain(unittest.TestCase):
    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        examples_path = os.path.join(current_dir, 'examples.json')
        with open(examples_path, 'r') as f:
            self.test_cases = json.load(f)

    def test_cases_from_json(self):
        for i, test_case in enumerate(self.test_cases):
            with self.subTest(case=i):
                in_stream = io.StringIO(test_case["input"])
                expected_output = test_case["output"].rstrip()

                out_stream = io.StringIO()
                main(in_stream, out_stream)
                real_output = out_stream.getvalue().rstrip()

                self.assertEqual(real_output, expected_output)

if __name__ == "__main__":
    unittest.main()