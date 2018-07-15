from Email.Account.Type.gmail import GmailAccount


class EmailAccount(object):
    @staticmethod
    def factory(account_type: str):
        valid_account_types = {'gmail': GmailAccount}
        return valid_account_types[account_type]()
