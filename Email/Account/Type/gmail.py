import httplib2
import base64
from googleapiclient.discovery import build
from Email.Message.message import EmailMessage
from Email.Account.Type.Authentication.gmail_authentication import GmailAuthentication


class GmailAccount(object):
    def __init__(self):
        self.authentication = GmailAuthentication()
        self.http = httplib2.Http()

    def send_email(self, message: EmailMessage):
        self.authenticate(message)

        service = build('gmail', 'v1', http=self.http)

        body = self.base64_encode_email(message)

        (service.users().messages().send(userId='me', body=body).execute())

    def authenticate(self, message: EmailMessage):
        credentails = self.authentication.get_user_credentials(message.get_sender())
        self.http = credentails.authorize(self.http)

    @staticmethod
    def base64_encode_email(message: EmailMessage):
        buffer = bytes(message.message.as_string(), 'UTF-8')
        return {'raw': base64.b64encode(buffer).decode('UTF-8')}
