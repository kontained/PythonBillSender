from unittest import TestCase
from config import Configuration


class ConfigTestCase(TestCase):
    def setUp(self):
        self.config = Configuration()

    def tearDown(self):
        pass

    def test_get_scopes(self):
        self.assertTrue(self.config.scopes)
        self.assertIsNotNone(self.config.scopes)

    def test_get_client_secrets_file_path(self):
        self.assertTrue(self.config.client_secrets_file_path)
        self.assertIsNotNone(self.config.client_secrets_file_path)

    def test_get_credentials_file_path(self):
        self.assertTrue(self.config.client_secrets_file_path)
        self.assertIsNotNone(self.config.client_secrets_file_path)

    def test_get_application_name(self):
        self.assertTrue(self.config.application_name)
        self.assertIsNotNone(self.config.application_name)
