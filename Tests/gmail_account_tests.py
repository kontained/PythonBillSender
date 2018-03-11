from unittest import TestCase
import sys
from Email.Account.Type.gmail import GmailAccount
from Email.Message.message import EmailMessage


class GmailAccountTestCase(TestCase):
    def setUp(self):
        self.gmail_account = GmailAccount('test@gmail.com', 'testpassword')

    def test_gmail_account_init(self):
        self.assertTrue(self.gmail_account is not None)

    def test_email_account_address(self):
        self.assertEqual(self.gmail_account.email_address, 'test@gmail.com')

    def test_email_account_password(self):
        self.assertEqual(self.gmail_account.email_password, 'testpassword')

    def test_send_email(self):
        try:
            message = EmailMessage()

            self.gmail_account.email_address = 'kontained@gmail.com'
            self.gmail_account.email_password = 'shopkazoooscarttribezf'

            message.set_sender(self.gmail_account.email_address)
            message.set_recipient(self.gmail_account.email_address)

            self.gmail_account.send_email(message)
        except:
            test = sys.exc_info()
            print(test)
