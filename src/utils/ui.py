def print_menu(menu, balance, payment_method=""):
    if payment_method:
        pm_label = payment_method
    else:
        pm_label = "없음"

    print("\n--- 자판기 ---")
    print("-" * 30)
    for i in menu:
        stock_info = ""
        if 'stock' in i:
            stock_info = f" (재고: {i['stock']}개)"

        print(f"{i['code']}: {i['name']} - {i['price']}원{stock_info}")

    print("-" * 30)
    print(f"현재 투입 잔액: {balance}원 | 결제수단: {pm_label}")
    print("-" * 30 + "\n")


def prompt_command():
    options = ["1)결제수단선택", "2)투입", "3)상품구매", "4)잔돈반환", "5)관리자모드", "q)종료"]
    print("선택해주세요 : ", *options)

    return input("> ").strip().lower()


def prompt_payment(valid_methods):
    while True:
        method = input(f"결제 수단 선택 {valid_methods}: ").strip().lower()
        if method in valid_methods:
            return method

        print(f"올바른 결제 수단을 선택하세요: {valid_methods}")


def prompt_money():
    while True:
        try:
            return int(input("투입할 금액을 입력하세요 100, 500, 1000, 10000, 50000: ").strip())
        except ValueError:
            print("숫자 형태로 입력해 주세요.")


def prompt_product_code(valid_codes):
    while True:
        code = input(f"상품코드 입력 {valid_codes}: ").strip().upper()
        if code in valid_codes:
            return code
        print(f"등록된 코드 중에서 선택하세요: {valid_codes}")


def prompt_admin_opt():
    options = ["a)추가", "b)삭제", "c)가격수정", "d)재고보충", "q)돌아가기"]
    print("-- 관리자 모드 --")
    print(" | ".join(options))
    return input("> ").strip().lower()
