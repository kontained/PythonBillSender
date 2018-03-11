import smtplib
from Email.Account.account import EmailAccount
from Email.Message.message import EmailMessage


class GmailAccount(EmailAccount):
    ssl_server_address = 'smtp.gmail.com'
    ssl_server_port = 465

    def __init__(self, email_address, email_password):
        super(GmailAccount, self).__init__(email_address, email_password)
        self.server = smtplib.SMTP_SSL(self.ssl_server_address, self.ssl_server_port)

    def send_email(self, message: EmailMessage):
        self.server.ehlo()
        self.server.login(self.email_address, self.email_password)
        self.server.sendmail(message.get_sender(), message.get_recipient(), message.message.as_string())
