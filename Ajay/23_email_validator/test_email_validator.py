import unittest
from email_validator import is_valid_email


class TestEmailValidation(unittest.TestCase):

    def test_valid_email(self):
        valid_emails = [
            "example@example.com",
            "john.doe@example.com",
            "jane_doe123@example.com",
            "test123@example123.com",
            "user+name@example.com",
            "user-name@example.com"
        ]

        for email in valid_emails:
            self.assertTrue(is_valid_email(email))

    def test_invalid_email(self):
        invalid_emails = [
            "example@",
            "example.com",
            "user@domain",
            "user@.com",
            "@example.com",
            "user name@example.com"
        ]

        for email in invalid_emails:
            self.assertFalse(is_valid_email(email))


if __name__ == '__main__':
    unittest.main()
