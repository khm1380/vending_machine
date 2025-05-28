from src.models.product import Product
from src.utils.change import get_change


class VendingMachine:
    def __init__(self, catalog: dict[str, Product], coins: list[int] = None) -> None:
        self._catalog = catalog.copy()
        self._balance = 0
        self._coins = coins or [50000, 10000, 5000, 1000, 500, 100]

    @property
    def balance(self) -> int:
        return self._balance

    def insert(self, amount: int) -> None:
        if amount not in self._coins:
            raise ValueError(f"허용되지 않는 화폐: {amount}")
        self._balance += amount

    def purchase(self, code: str) -> Product:
        if code not in self._catalog:
            raise KeyError(f"상품 없음: {code}")

        prod = self._catalog[code]

        if prod.stock == 0:
            raise RuntimeError(f"품절됨: {code}")

        if self._balance < prod.price:
            raise RuntimeError("잔액 부족")

        prod.stock -= 1
        self._balance -= prod.price
        return prod

    def purchase_card(self, code: str) -> Product:
        if code not in self._catalog:
            raise KeyError(f"상품 없음: {code}")

        prod = self._catalog[code]

        if prod.stock == 0:
            raise RuntimeError(f"품절됨: {code}")

        prod.stock -= 1
        return prod

    def change(self) -> dict[int, int]:
        coins = get_change(self._balance, self._coins)
        self._balance = 0
        return coins

    def menu(self) -> list[dict[str, object]]:
        return [prod.to_dict() for prod in self._catalog.values()]
