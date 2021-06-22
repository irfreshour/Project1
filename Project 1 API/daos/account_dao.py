from abc import ABC, abstractmethod
from entities.account import Account


class AccountDAO(ABC):

    # read
    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def get_account_by_login(self, email: str, password: str) -> Account:
        pass

    # update
    @abstractmethod
    def update_account(self, account: Account) -> bool:
        pass
