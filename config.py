import json


class Configuration:
    def __init__(self):
        with open('C:\\Users\\konta\\Documents\\development\\python\\PythonBillSender\\config.json', 'r') as f:
            config = json.load(f)

        self.scopes = config['scopes']
        self.client_secrets_file_path = config['client_secrets_file']
        self.credentials_file_path = config['credentials_path']
        self.application_name = 'BillSender'

    def get_scopes(self):
        return self.scopes

    def get_client_secrets_file_path(self):
        return self.client_secrets_file_path

    def get_credentials_file_path(self):
        return self.credentials_file_path

    def get_application_name(self):
        return self.application_name
