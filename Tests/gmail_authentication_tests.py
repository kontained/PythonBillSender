from unittest import TestCase, mock
from Email.Account.Type.Authentication.gmail_authentication import GmailAuthentication


class GmailAuthenticationTestCase(TestCase):
    def setUp(self):
        self.gmail_authentication = GmailAuthentication()

    def test_get_credentials(self):
        self.gmail_authentication.get_credentials()
