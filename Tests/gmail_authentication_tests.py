from unittest import TestCase
from Email.Account.Type.Authentication.gmail_authentication import GmailAuthentication


class GmailAuthenticationTestCase(TestCase):
    def setUp(self):
        self.gmail_authentication = GmailAuthentication()

    def test_get_credentials_wrong_type_username(self):
        self.assertRaises(TypeError, self.gmail_authentication.get_user_credentials, 0)

    def test_get_credentials_empty_username(self):
        self.assertRaises(ValueError, self.gmail_authentication.get_user_credentials, '')

    def test_get_credentials(self):
        self.assertIsNotNone(self.gmail_authentication.get_user_credentials('kontained'))
