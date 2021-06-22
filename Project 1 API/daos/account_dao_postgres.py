from daos.account_dao import AccountDAO
from entities.account import Account
from exceptions.not_found_exception import ResourceNotFoundError
from utils.connection_util import connection
from exceptions.invalid_parameter_exception import InvalidParameterError


class AccountDAOPostgres(AccountDAO):
    def get_account_by_id(self, account_id: int) -> Account:
        sql = """select * from account where account_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError("Account could not be found")
        account = Account(*record)
        return account

    def get_account_by_login(self, email: str, password: str) -> Account:
        sql = """select * from account where email = %s and p_word = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [email, password])
        record = cursor.fetchone()
        if record is None:
            raise InvalidParameterError("Invalid email and password")
        account = Account(*record)
        return account

    def update_account(self, account: Account) -> bool:
        sql = """update account set email=%s, p_word=%s, user_name=%s, manager=%s, logged_in=%s where account_id=%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [account.email, account.p_word, account.user_name, account.manager, account.logged_in,
                             account.account_id])
        connection.commit()
        return True
