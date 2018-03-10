from unittest import TestCase
from Email.Account.account import EmailAccount


class EmailAccountTestCase(TestCase):
    def setUp(self):
        self.email_account = EmailAccount('test@gmail.com', 'testpassword')

    def test_email_account_init(self):
        self.assertTrue(self.email_account is not None)

    def test_email_account_address(self):
        self.assertEqual(self.email_account.email_address, 'test@gmail.com')

    def test_email_account_password(self):
        self.assertEqual(self.email_account.email_password, 'testpassword')
