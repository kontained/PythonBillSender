from unittest import TestCase
from Email.Message.message import EmailMessage


class EmailMessageTestCase(TestCase):
    def setUp(self):
        self.email_message = EmailMessage()

    def test_email_message_init(self):
        self.assertTrue(self.email_message is not None)

    def test_get_recipient(self):
        self.email_message.set_recipient('test@test.com')
        self.assertEqual(self.email_message.get_recipient(), 'test@test.com')

    def test_set_recipient_good_email(self):
        self.email_message.set_recipient('example-indeed@strange-example.com')

    def test_set_recipient_bad_email(self):
        self.assertRaises(
            ValueError,
            self.email_message.set_recipient,
            'Abc.example.com'
        )

    def test_get_sender(self):
        self.email_message.set_sender('test@test.com')
        self.assertEqual(self.email_message.get_sender(), 'test@test.com')

    def test_set_sender_good_email(self):
        self.email_message.set_sender('example-indeed@strange-example.com')

    def test_set_sender_bad_email(self):
        self.assertRaises(
            ValueError,
            self.email_message.set_sender,
            'Abc.example.com'
        )

    def test_get_subject(self):
        self.email_message.set_subject('Email subject')
        self.assertEqual(self.email_message.message['Subject'], 'Email subject')

    def test_set_subject(self):
        self.assertRaises(
            ValueError,
            self.email_message.set_subject,
            ''
        )
