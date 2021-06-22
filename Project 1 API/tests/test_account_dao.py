from daos.account_dao_postgres import AccountDAOPostgres
from entities.account import Account
from exceptions.invalid_parameter_exception import InvalidParameterError
from exceptions.not_found_exception import ResourceNotFoundError

account_dao = AccountDAOPostgres()
employee = Account(4, "a", "a", "a", False, True)


def test_get_account_by_id_fail():
    try:
        account_dao.get_account_by_id(-1)
        assert False
    except ResourceNotFoundError as e:
        assert True


def test_get_account_by_id():
    assert account_dao.get_account_by_id(1)


def test_get_account_by_login_fail():
    try:
        account_dao.get_account_by_login("", "")
        assert False
    except InvalidParameterError as e:
        assert True


def test_get_account_by_login():
    assert account_dao.get_account_by_login("blah@blah.com", "thepass")


def test_update_account():
    assert account_dao.update_account(employee)
