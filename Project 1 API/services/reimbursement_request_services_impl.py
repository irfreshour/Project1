from typing import List

from daos.reimbursement_request_dao import ReimbursementRequestDAO
from entities.account import Account
from entities.reimbursement_request import ReimbursementRequest
from services.reimbursement_request_services import ReimbursementRequestServices
from utils.login_util import login_utility
from exceptions.incorrect_login_exception import InvalidLoginError


class ReimbursementRequestServicesImpl(ReimbursementRequestServices):

    def __init__(self, reimbursement_dao: ReimbursementRequestDAO):
        self.reimbursement_dao = reimbursement_dao

    def create_request(self, account_id: int, request: ReimbursementRequest):

        if login_utility.is_a_manager(account_id):
            raise InvalidLoginError("Managers cannot post requests")
        else:
            return self.reimbursement_dao.create_request(request)

    def get_request_by_id(self, request_id: int):
        pass

    def get_all_user_request(self, account_id: int) -> List[ReimbursementRequest]:
        if login_utility.is_a_manager(account_id):
            raise InvalidLoginError("Managers cannot post requests")
        else:
            return self.reimbursement_dao.get_all_user_request(account_id)

    def get_all_requests(self, account_id: int) -> List[ReimbursementRequest]:
        if login_utility.is_a_manager(account_id):
            return self.reimbursement_dao.get_all_requests()
        else:
            raise InvalidLoginError("Employees cannot post see other's requests")

    def update_request(self, account_id, request: ReimbursementRequest):
        if login_utility.is_a_manager(account_id):
            return self.reimbursement_dao.update_user_request(request)
        else:
            raise InvalidLoginError("Employees cannot update requests")
