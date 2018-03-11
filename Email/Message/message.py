from email.mime.multipart import MIMEMultipart
import re


class EmailMessage(object):
    valid_email_regex_pattern = "^[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~.]+@[a-zA-Z0-9-.]+$"
    valid_email_regex = re.compile(valid_email_regex_pattern)

    def __init__(self):
        self.message = MIMEMultipart()

    def get_recipient(self) -> str:
        return self.message['To']

    def set_recipient(self, recipient: str):
        if self.valid_email_regex.match(recipient):
            self.message['To'] = recipient
        else:
            raise ValueError('Invalid recipient email address.')

    def get_sender(self) -> str:
        return self.message['From']

    def set_sender(self, sender: str):
        if self.valid_email_regex.match(sender):
            self.message['From'] = sender
        else:
            raise ValueError('Invalid recipient email address.')

    def get_subject(self) -> str:
        return self.message['Subject']

    def set_subject(self, subject: str):
        if subject:
            self.message['Subject'] = subject
        else:
            raise ValueError('Invalid email message subject')
