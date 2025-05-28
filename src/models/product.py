from dataclasses import dataclass, field

@dataclass
class Product:
    code: str
    name: str
    price: int
    stock: int = field(default=0)

    _kor = {
        "code": "상품 코드",
        "name": "상품명",
        "price": "상품 가격",
        "stock": "재고 수량"
    }

    def __post_init__(self):
        if not self.code:
            raise ValueError(f"{self._kor['code']}은(는) 비어 있을 수 없습니다.")
        if not self.name:
            raise ValueError(f"{self._kor['name']}은(는) 비어 있을 수 없습니다.")
        if self.price < 0:
            raise ValueError(f"{self._kor['price']}은(는) 0 이상이어야 합니다.")
        if self.stock < 0:
            raise ValueError(f"{self._kor['stock']}은(는) 0 이상이어야 합니다.")

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(
            code=data["code"],
            name=data["name"],
            price=int(data["price"]),
            stock=int(data.get("stock", 0))
        )
