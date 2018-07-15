import os
from oauth2client import client, tools, file
from config import Configuration


class GmailAuthentication:
    def __init__(self):
        self.configuration = Configuration()

    def get_user_credentials(self, username: str) -> client.OAuth2Credentials:
        self.validate_username(username)

        self.create_credentials_folder()

        credentials = self.get_credentials_file(username)

        return credentials

    @staticmethod
    def validate_username(username: str):
        if not isinstance(username, str):
            raise TypeError('Username must be a string!')
        if not username:
            raise ValueError('Username cannot be null!')

    def create_credentials_folder(self):
        if not os.path.exists(self.configuration.credentials_file_path):
            os.makedirs(self.configuration.credentials_file_path)

    def get_credentials_file(self, username: str):
        credentials_file_path = os.path.join(
            self.configuration.credentials_file_path, username.split('@')[0] + '.json')

        store = file.Storage(credentials_file_path)
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(
                self.configuration.client_secrets_file_path,
                self.configuration.scopes)
            flow.user_agent = self.configuration.application_name
            credentials = tools.run_flow(flow, store)

        return credentials
