from abc import ABC, abstractmethod
from typing import List

from entities.account import Account
from entities.reimbursement_request import ReimbursementRequest


class ReimbursementRequestServices(ABC):

    @abstractmethod
    def create_request(self, account_id: int, request: ReimbursementRequest):
        pass

    @abstractmethod
    def get_request_by_id(self, request_id: int):
        pass

    @abstractmethod
    def get_all_user_request(self, account_id: int) -> List[ReimbursementRequest]:
        pass

    @abstractmethod
    def update_request(self, account_id, request: ReimbursementRequest):
        pass
