from entities.account import Account
from exceptions.incorrect_login_exception import InvalidLoginError


class LoginUtil:
    def __init__(self):
        self.logged_users = {}

    def login(self, account_id: int, account: Account):
        if account_id in self.logged_users:
            raise InvalidLoginError("user is already logged in")
        self.logged_users.update({account_id: account})

    def logout(self, account_id):
        if account_id in self.logged_users:
            self.logged_users.pop(account_id)
        else:
            raise InvalidLoginError("User is not logged in")

    def is_a_manager(self, account_id):
        if account_id not in self.logged_users:
            raise InvalidLoginError("User is not logged in")
        else:
            return self.logged_users.get(account_id).manager


login_utility = LoginUtil()
