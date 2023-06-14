import unittest
from staircase_string import staircase_string


class StaircaseTest(unittest.TestCase):
    def test_create_staircase_with_empty_string(self):
        string = ""
        expected_output = []
        self.assertEqual(staircase_string(string), expected_output)

    def test_create_staircase_with_single_character_string(self):
        string = "A"
        expected_output = ["A"]
        self.assertEqual(staircase_string(string), expected_output)

    def test_create_staircase_with_longer_string(self):
        string = "PYTHON"
        expected_output = [
            "P",
            "PY",
            "PYT",
            "PYTH",
            "PYTHO",
            "PYTHON"
        ]
        self.assertEqual(staircase_string(string), expected_output)

    def test_create_staircase_with_special_characters_and_spaces(self):
        string = "!@#$%^&*() "
        expected_output = [
            "!",
            "!@",
            "!@#",
            "!@#$",
            "!@#$%",
            "!@#$%^",
            "!@#$%^&",
            "!@#$%^&*",
            "!@#$%^&*(",
            "!@#$%^&*()",
            "!@#$%^&*() "
        ]
        self.assertEqual(staircase_string(string), expected_output)


if __name__ == "__main__":
    unittest.main()
