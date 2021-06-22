class ReimbursementRequest:
    def __init__(self, request_id: int, account_id: int, amount_spent: int, amount_requested: int, reason: str,
                 pending: bool, approved: bool, response: str):
        self.request_id = request_id
        self.account_id = account_id
        self.amount_spent = amount_spent
        self.amount_requested = amount_requested
        self.reason = reason
        self.pending = pending
        self.approved = approved
        self.response = response

    def __str__(self):
        return f"id={self.request_id}, spent={self.amount_spent}, requested={self.amount_requested}"

    def as_json_dict(self):
        return {
            "requestId": self.request_id,
            "accountId": self.account_id,
            "amountSpent": self.amount_spent,
            "amountRequested": self.amount_requested,
            "reason": self.reason,
            "pending": self.pending,
            "approved": self.approved,
            "response": self.response
        }
