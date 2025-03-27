import unittest
import io
from code_uut import main

TEST_CASES = [{
    "input": """\
5
7
1
9
7
3
""",
    "output": """\
1 3 7 7 9
""",
}, {
    "input": """\
10
60
1
60
1
""",
    "output": """\
1 1 1 1 1 60 60 60 60 60
""",
}]

class TestMain(unittest.TestCase):
    def test_cases_from_json(self):
        for i, test_case in enumerate(TEST_CASES):
            with self.subTest(case=i):
                in_stream = io.StringIO(test_case["input"])
                expected_output = test_case["output"].rstrip()

                out_stream = io.StringIO()
                main(in_stream, out_stream)
                real_output = out_stream.getvalue().rstrip()

                self.assertEqual(real_output, expected_output)

if __name__ == "__main__":
    unittest.main()