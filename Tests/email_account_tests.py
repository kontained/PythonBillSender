from unittest import TestCase
from Email.Account.account import email_account_factory
from Email.Account.Type.gmail import GmailAccount


class EmailAccountTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_email_account_factory(self):
        gmail = email_account_factory('gmail')
        self.assertTrue(isinstance(gmail, GmailAccount))

    def test_email_account_invalid_type(self):
        self.assertRaises(KeyError, email_account_factory, 'invalid')
