from daos.reimbursement_request_dao_postgres import ReimbursementRequestDAOPostgres
from entities.reimbursement_request import ReimbursementRequest
from exceptions.not_found_exception import ResourceNotFoundError

request_dao = ReimbursementRequestDAOPostgres()
request = ReimbursementRequest(0, 0, 0, 0, "", True, False, "")


def test_create_request():
    request.account_id = 4
    assert request_dao.create_request(request)


def test_get_request_by_id_fail():
    try:
        request_dao.get_request_by_id(request, -1)
        assert False
    except ResourceNotFoundError as e:
        assert True


def test_get_request_by_id():
    assert request_dao.get_request_by_id(request, 1) is not None


def test_get_all_requests():
    result = request_dao.get_all_requests()
    assert len(result) > 0


def test_get_all_user_requests():
    result = request_dao.get_all_user_request(1)
    assert len(result) > 0


def test_update_request_fail():
    try:
        request.request_id = -1
        request_dao.update_user_request(request)
        assert False
    except ResourceNotFoundError as e:
        assert True


def test_update_request():
    request.request_id = 4
    request.pending = False
    request.approved = True
    request.response = ""
    assert request_dao.update_user_request(request)
