class Admin:
    # 메뉴는 메모리상에서만 관리, json은 변경 x

    def __init__(self, catalog=None):
        self._catalog = catalog.copy() if catalog else {}

    def add(self, product):
        if product.code in self._catalog:
            raise ValueError(f"이미 존재하는 상품 코드입니다: {product.code}")
        self._catalog[product.code] = product

    def remove(self, code):
        if code not in self._catalog:
            raise KeyError(f"삭제할 상품 코드가 없습니다: {code}")
        del self._catalog[code]

    def update_price(self, code, price):
        if code not in self._catalog:
            raise KeyError(f"상품 코드가 없습니다: {code}")
        if price < 0:
            raise ValueError("가격은 0 이상이어야 합니다.")
        self._catalog[code].price = price

    def restock(self, code, qty):
        if code not in self._catalog:
            raise KeyError(f"상품 코드가 없습니다: {code}")
        if qty < 1:
            raise ValueError("재고 보충 수량은 1 이상이어야 합니다.")
        self._catalog[code].stock += qty

    def list_products(self):
        return self._catalog.copy()
