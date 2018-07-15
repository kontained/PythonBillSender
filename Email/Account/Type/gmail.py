import httplib2
import base64
from googleapiclient.discovery import build
from Email.Message.message import EmailMessage
from Email.Account.Type.Authentication.gmail_authentication import GmailAuthentication


class GmailAccount(object):
    def __init__(self):
        self.authentication = GmailAuthentication()

    def send_email(self, message: EmailMessage):
        self.authenticate(message)

    def authenticate(self, message: EmailMessage):
        try:
            http = httplib2.Http()
            credentails = self.authentication.get_user_credentials(message.get_sender())
            http = credentails.authorize(http)
            service = build('gmail', 'v1', http=http)
            buffer = bytes(message.message.as_string(), 'UTF-8')
            body = {'raw': base64.b64encode(buffer).decode('UTF-8')}
            (service.users().messages().send(userId='me', body=body).execute())
        except Exception as error:
            print(error)
