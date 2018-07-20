from unittest import TestCase
from Email.Account.account import email_account_factory
from Email.Message.message import EmailMessage


class GmailAccountTestCase(TestCase):
    def setUp(self):
        self.gmail_account = email_account_factory('gmail')

    def test_gmail_account_init(self):
        self.assertTrue(self.gmail_account is not None)

    def test_gmail_account_send_email(self):
        message = EmailMessage()
        message.set_recipient('kontained@gmail.com')
        message.set_sender('kontained@gmail.com')
        self.gmail_account.send_email(message)
