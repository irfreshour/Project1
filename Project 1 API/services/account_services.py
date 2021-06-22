from abc import ABC, abstractmethod

from entities.account import Account


class AccountServices(ABC):

    @abstractmethod
    def get_account_by_id(self, account_id: int, user_id: int) -> Account:
        pass

    @abstractmethod
    def get_account_by_login(self, email: str, password: str) -> Account:
        pass