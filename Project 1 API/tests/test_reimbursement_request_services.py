from unittest.mock import MagicMock

from daos.reimbursement_request_dao_postgres import ReimbursementRequestDAOPostgres
from exceptions.incorrect_login_exception import InvalidLoginError
from services.account_services_impl import AccountServicesImpl
from entities.account import Account
from entities.reimbursement_request import ReimbursementRequest
from services.reimbursement_request_services_impl import ReimbursementRequestServicesImpl
from utils.login_util import login_utility

from daos.account_dao_postgres import AccountDAOPostgres

employee = Account(0, "", "", "", False, True)
manager = Account(1, "", "", "", True, True)
request = ReimbursementRequest(0, 0, 0, 0, "", True, False, "")

mockDao = ReimbursementRequestDAOPostgres()
mockDao.create_request = MagicMock(return_value=True)
mockDao.get_all_user_request = MagicMock(return_value=True)
mockDao.get_all_requests = MagicMock(return_value=True)
mockDao.update_user_request = MagicMock(return_value=True)
reimbursement_services = ReimbursementRequestServicesImpl(mockDao)


def test_create_request_fail():
    try:
        login_utility.login(0, employee)
        login_utility.login(1, manager)

        reimbursement_services.create_request(1, request)
        assert False
    except InvalidLoginError as e:
        assert True


def test_create_request():
    assert reimbursement_services.create_request(0, request)


def test_get_all_user_requests_fail():
    try:
        reimbursement_services.get_all_user_request(1)
        assert False
    except InvalidLoginError as e:
        assert True


def test_get_all_user_requests():
    assert reimbursement_services.get_all_user_request(0)


def test_get_all_requests_fail():
    try:
        reimbursement_services.get_all_requests(0)
        assert False
    except InvalidLoginError as e:
        assert True


def test_get_all_requests():
    assert reimbursement_services.get_all_requests(1)


def test_update_request_fail():
    try:
        reimbursement_services.update_request(0, request)
        assert False
    except InvalidLoginError as e:
        assert True


def test_update_request():
    assert reimbursement_services.update_request(1, request)
    login_utility.logout(0)
    login_utility.logout(1)
