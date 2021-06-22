from typing import List
from daos.reimbursement_request_dao import ReimbursementRequestDAO
from entities.reimbursement_request import ReimbursementRequest
from exceptions.not_found_exception import ResourceNotFoundError
from utils.connection_util import connection


class ReimbursementRequestDAOPostgres(ReimbursementRequestDAO):

    def create_request(self, request: ReimbursementRequest) -> bool:
        sql = """insert into request(account_id, amount_spent, amount_requested, reason, pending, approved, response) values (%s,%s,%s,%s,%s,%s,%s) returning request_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (
            request.account_id, request.amount_spent, request.amount_requested, request.reason, request.pending,
            request.approved, request.response))
        connection.commit()
        r_id = cursor.fetchone()[0]
        request.request_id = r_id
        return True

    def get_request_by_id(self, request: ReimbursementRequest, request_id: int) -> ReimbursementRequest:
        sql = """select * from request where request_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [request_id])
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError("No request for that id")
        request = ReimbursementRequest(*record)
        return request

    def get_all_requests(self) -> List[ReimbursementRequest]:
        sql = """select * from request"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        request_list = []
        for record in records:
            request_list.append(ReimbursementRequest(*record))
        return request_list

    def get_all_user_request(self, account_id: int) -> List[ReimbursementRequest]:
        sql = """select * from request where account_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        records = cursor.fetchall()
        request_list = []
        for record in records:
            request_list.append(ReimbursementRequest(*record))
        return request_list

    def update_user_request(self, request: ReimbursementRequest) -> bool:
        sql = """update request set pending=%s, approved=%s, response=%s where request_id=%s returning request_id"""
        cursor = connection.cursor()
        cursor.execute(sql, [request.pending, request.approved, request.response, request.request_id])
        connection.commit()
        result = cursor.fetchone()
        if result is None:
            raise ResourceNotFoundError("No matching request to update")
        return True
