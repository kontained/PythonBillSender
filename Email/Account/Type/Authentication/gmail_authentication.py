import os
import oauth2client
from oauth2client import client, tools, file
from config import Configuration


class GmailAuthentication:
    def __init__(self):
        self.configuration = Configuration()

    def get_user_credentials(self, username):
        self._validate_username(username)

        self._create_credentials_folder()

        credentials = self._get_credentials_file(username)

        return credentials

    def _validate_username(self, username):
        if not isinstance(username, str):
            raise TypeError('Username must be a string!')
        if not username:
            raise ValueError('Username cannot be null!')

    def _create_credentials_folder(self):
        if not os.path.exists(self.configuration.get_credentials_file_path()):
            os.makedirs(self.configuration.get_credentials_file_path())

    def _get_credentials_file(self, username):
        credentials_file_path = os.path.join(self.configuration.get_credentials_file_path(), username + '.json')
        store = oauth2client.file.Storage(credentials_file_path)
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(
                self.configuration.get_client_secrets_file_path(),
                self.configuration.get_scopes())
            flow.user_agent = self.configuration.get_application_name()
            credentials = tools.run_flow(flow, store)

        return credentials
