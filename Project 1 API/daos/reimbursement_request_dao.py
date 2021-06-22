from abc import ABC, abstractmethod
from typing import List
from entities.reimbursement_request import ReimbursementRequest


class ReimbursementRequestDAO(ABC):

    # create
    @abstractmethod
    def create_request(self, request: ReimbursementRequest) -> bool:
        pass

    # read
    @abstractmethod
    def get_request_by_id(self,request: ReimbursementRequest, request_id: int) -> ReimbursementRequest:
        pass

    @abstractmethod
    def get_all_requests(self) -> List[ReimbursementRequest]:
        pass

    @abstractmethod
    def get_all_user_request(self, account_id: int) -> List[ReimbursementRequest]:
        pass

    # update
    @abstractmethod
    def update_user_request(self, request: ReimbursementRequest) -> bool:
        pass
