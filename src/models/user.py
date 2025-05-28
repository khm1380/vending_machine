class User:
    VALID_PAYMENT = {
        "coin",
        "card"
    }

    def __init__(self):
        self.balance = 0
        self.payment_method = ""

    def choose_payment(self, method):
        if method not in self.VALID_PAYMENT:
            raise ValueError()
        self.payment_method = method

    def insert_money(self, amount):
        if self.payment_method != "coin":
            raise RuntimeError("coin만 투입이 가능합니다.")
        if amount <= 0:
            raise ValueError()
        self.balance += amount

    def use_balance(self, amount):
        if self.payment_method != "coin":
            return
        if amount <= 0 or amount > self.balance:
            raise ValueError()
        self.balance -= amount

    def reset(self):
        self.balance = 0
        self.payment_method = ""
