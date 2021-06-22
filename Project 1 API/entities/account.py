class Account:
    def __init__(self, account_id: int, email: str, p_word: str, user_name: str, manager: bool, logged_in: bool):
        self.account_id = account_id
        self.email = email
        self.p_word = p_word
        self.user_name = user_name
        self.manager = manager
        self.logged_in = logged_in

    def __str__(self):
        return f"id={self.account_id}, name={self.user_name}, email={self.email}"

    def as_json_dict(self):
        return {
            "accountID": self.account_id,
            "email": self.email,
            "password": self.p_word,
            "userName": self.user_name,
            "manager": self.manager,
            "loggedIn": self.logged_in
        }
