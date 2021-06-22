from daos.account_dao import AccountDAO
from entities.account import Account
from exceptions.incorrect_login_exception import InvalidLoginError
from services.account_services import AccountServices
from utils.login_util import login_utility


class AccountServicesImpl(AccountServices):
    def __init__(self, account_dao: AccountDAO):
        self.account_dao = account_dao

    def get_account_by_id(self, account_id: int, user_id: int) -> Account:
        if login_utility.is_a_manager(account_id):
            return self.account_dao.get_account_by_id(user_id)
        else:
            raise InvalidLoginError("Only managers can see employee names")

    def get_account_by_login(self, email: str, password: str) -> Account:
        return self.account_dao.get_account_by_login(email, password)
