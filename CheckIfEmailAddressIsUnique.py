# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
#
# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
#
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
#
# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.
#
# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.


import unittest
from typing import List

def numUniqueEmails(emails: List[str]) -> int:
    set_ = set()
    for i in emails:
        final_email = ""
        email = i.split("@")
        email[0] = email[0].replace(".", "")
        if "+" in email[0]:
            index = email[0].index("+")
            email[0] = email[0][:index]
        final_email += email[0] + "@" + email[1]
        set_.add(final_email)
    return len(set_)

class TestNumUniqueEmails(unittest.TestCase):
    def test_empty_list(self):
        emails = []
        expected = 0
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_single_email(self):
        emails = ["test.email@example.com"]
        expected = 1
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_duplicate_emails(self):
        emails = ["test.email@example.com", "test.email@example.com"]
        expected = 1
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_unique_emails(self):
        emails = ["test.email@example.com", "test.email2@example.com", "another.email@example.com"]
        expected = 3
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_emails_with_dots(self):
        emails = ["t.est.email@example.com", "testemail@example.com"]
        expected = 1
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_emails_with_plus(self):
        emails = ["test.email+spam@example.com", "test.email@example.com"]
        expected = 1
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_emails_with_com_suffix(self):
        emails = ["test.email@example.com", "test.email@example.org"]
        expected = 2
        self.assertEqual(numUniqueEmails(emails), expected)

if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passed
