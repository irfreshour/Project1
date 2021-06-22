from typing import List

from flask import Flask, request, jsonify
from flask_cors import CORS

from exceptions.invalid_parameter_exception import InvalidParameterError
from exceptions.incorrect_login_exception import InvalidLoginError
from daos.account_dao_postgres import AccountDAOPostgres
from daos.reimbursement_request_dao_postgres import ReimbursementRequestDAOPostgres
from exceptions.not_found_exception import ResourceNotFoundError
from services.account_services_impl import AccountServicesImpl
from utils.login_util import login_utility
from services.reimbursement_request_services_impl import ReimbursementRequestServicesImpl
from entities.reimbursement_request import ReimbursementRequest
import logging

app: Flask = Flask(__name__)
CORS(app)
account_dao = AccountDAOPostgres()
account_service = AccountServicesImpl(account_dao)
reimbursement_dao = ReimbursementRequestDAOPostgres()
reimbursement_service = ReimbursementRequestServicesImpl(reimbursement_dao)
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')


def get_incoming_account_id() -> int:
    account_id: int = int(request.headers.get("accountID"))
    if account_id is None:
        raise InvalidLoginError("There is an issue with your login")
    return account_id


@app.route("/login", methods=["POST"])
def log_in():
    try:
        body = request.json
        account = account_service.get_account_by_login(body.get("email"), body.get("password"))
        login_utility.login(account.account_id, account)
        return jsonify(account.as_json_dict()), 200

    except InvalidParameterError as e:
        return e.message, 400

    except InvalidLoginError as e:
        return e.message, 403


@app.route("/logout", methods=["POST"])
def log_out():
    account_id = get_incoming_account_id()
    login_utility.logout(account_id)
    return "logged out successfully", 200


@app.route("/account/<user_id>", methods=["GET"])
def get_user_by_id(user_id: str):
    try:
        account_id = get_incoming_account_id()
        account = account_service.get_account_by_id(account_id, int(user_id))
        return jsonify(account.as_json_dict()), 200
    except InvalidLoginError as e:
        return e.message, 403


@app.route("/requests", methods=["POST"])
def create_request():
    try:
        account_id = get_incoming_account_id()
        body = request.json
        reimbursement = ReimbursementRequest(0, account_id, body.get("amountSpent"), body.get("amountRequested"),
                                             body.get("reason"), True, False, "")
        reimbursement_service.create_request(account_id, reimbursement)
        return jsonify(reimbursement.as_json_dict()), 201
    except InvalidParameterError as e:
        return e.message, 400

    except InvalidLoginError as e:
        return e.message, 403


@app.route("/requests/user", methods=["GET"])
def get_user_requests():
    try:
        account_id = get_incoming_account_id()
        reimbursement_list: List[ReimbursementRequest] = reimbursement_service.get_all_user_request(account_id)
        json_reimbursement = [r.as_json_dict() for r in reimbursement_list]
        return jsonify(json_reimbursement), 200

    except InvalidLoginError as e:
        return e.message, 403


@app.route("/requests/all", methods=["GET"])
def get_all_requests():
    try:
        account_id = get_incoming_account_id()
        reimbursement_list: List[ReimbursementRequest] = reimbursement_service.get_all_requests(account_id)
        json_reimbursement = [r.as_json_dict() for r in reimbursement_list]
        return jsonify(json_reimbursement), 200
    except InvalidLoginError as e:
        return e.message, 403


@app.route("/requests/update", methods=["PUT"])
def update_request():
    try:

        account_id = get_incoming_account_id()
        body = request.json
        reimbursement = ReimbursementRequest(body.get("requestId"), body.get("accountId"), body.get("amountSpent"),
                                             body.get("amountRequested"), body.get("reason"), body.get("pending"),
                                             body.get("approved"), body.get("response"))
        reimbursement_service.update_request(account_id, reimbursement)
        return "successfully updated", 200
    except InvalidParameterError as e:
        return e.message, 400
    except ResourceNotFoundError as e:
        return e.message, 404
    except InvalidLoginError as e:
        return e.message, 403


if __name__ == '__main__':
    app.run()
