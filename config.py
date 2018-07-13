import json


class Configuration:
    def __init__(self):
        with open('C:\\Users\\konta\\Documents\\development\\python\\PythonBillSender\\config.json', 'r') as f:
            config = json.load(f)

        self.scopes = config['scopes']
        self.client_secrets_file_path = config['client_secrets_file']
        self.credentials_file_path = config['credentials_path']
        self.application_name = 'BillSender'
