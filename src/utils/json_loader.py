import json
from src.models.product import Product

# TODO
# 나중에 .env에 정의할 예정 (dev,prod 환경 설정 등등 중요한 게 없어서 .env는 불필요)

MENU_PATH = "src/utils/menu.json"


def load_json() -> dict[str, Product]:
    with open(MENU_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    catalog: dict[str, Product] = {}

    for i in data:
        prod = Product.from_dict(i)
        catalog[prod.code] = prod

    return catalog
