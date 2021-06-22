from unittest.mock import MagicMock

from exceptions.incorrect_login_exception import InvalidLoginError
from services.account_services_impl import AccountServicesImpl
from entities.account import Account
from utils.login_util import login_utility

from daos.account_dao_postgres import AccountDAOPostgres

employee = Account(0, "", "", "", False, True)
manager = Account(1, "", "", "", True, True)

mockDao = AccountDAOPostgres()
mockDao.get_account_by_id = MagicMock(return_value=True)
account_services = AccountServicesImpl(mockDao)




def test_get_account_by_id_fail():
    try:
        login_utility.login(0, employee)
        login_utility.login(1, manager)

        account_services.get_account_by_id(0, 0)
        assert False
    except InvalidLoginError as e:
        assert True


def test_get_account_by_id():
    assert account_services.get_account_by_id(1, 0)
    login_utility.logout(0)
    login_utility.logout(1)
