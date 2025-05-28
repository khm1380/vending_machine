from src.models.machine import VendingMachine
from src.models.admin import Admin
from src.models.user import User
from src.models.product import Product

class VendingService:

    def __init__(self, initial_catalog):
        self.admin = Admin(initial_catalog)
        self.vm = VendingMachine(self.admin.list_products())
        self.user = User()

    def select_payment(self, method):
        self.user.choose_payment(method)

    def insert_money(self, amount):
        self.user.insert_money(amount)
        self.vm.insert(amount)

    def purchase(self, code):
        if self.user.payment_method == "card":
            prod = self.vm.purchase_card(code)
        else:
            prod = self.vm.purchase(code)
            self.user.use_balance(prod.price)
        self.user.reset()
        return prod

    def return_change(self):
        change = self.vm.change()
        self.user.reset()
        return change

    def admin_add(self, code, name, price, stock):
        prod = Product(code, name, price, stock)
        self.admin.add(prod)
        self._reload_vm()

    def admin_remove(self, code):
        self.admin.remove(code)
        self._reload_vm()

    def admin_update_price(self, code, price):
        self.admin.update_price(code, price)
        self._reload_vm()

    def admin_restock(self, code, qty):
        self.admin.restock(code, qty)
        self._reload_vm()

    def _reload_vm(self):
        self.vm = VendingMachine(self.admin.list_products())
