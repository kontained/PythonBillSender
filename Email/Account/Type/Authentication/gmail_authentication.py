import os
import oauth2client
from oauth2client import client, tools, file
from config import Configuration


class GmailAuthentication:
    def __init__(self):
        configuration = Configuration()
        self.scopes = configuration.get_scopes()
        self.client_secrets_file = configuration.client_secrets_file()
        self.credentials_path = configuration.get_credentials_path()
        self.application_name = 'BillSender'

    def get_credentials(self):
        if not os.path.exists(self.credentials_path):
            os.makedirs(self.credentials_path)

        cred_path = os.path.join(self.credentials_path, 'gmail.json')

        store = oauth2client.file.Storage(cred_path)
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.client_secrets_file, self.scopes)
            flow.user_agent = self.application_name
            credentials = tools.run_flow(flow, store)

        return credentials
