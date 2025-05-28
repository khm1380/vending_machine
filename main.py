from src.utils.json_loader import load_json
from src.utils.ui import (
    print_menu,
    prompt_command,
    prompt_payment,
    prompt_money,
    prompt_product_code,
    prompt_admin_opt,
)
from src.services.machine_service import VendingService

catalog = load_json()
svc = VendingService(catalog)

while True:
    menu = svc.vm.menu()
    print_menu(menu, svc.user.balance, svc.user.payment_method)
    cmd = prompt_command()

    if cmd == '1':
        svc.select_payment(prompt_payment(list(svc.user.VALID_PAYMENT)))
        print(f"{svc.user.payment_method} 모드 선택 완료.")

    elif cmd == '2':
        if svc.user.payment_method != 'coin':
            print("현금 결제 모드에서만 금액을 투입할 수 있습니다. 결제 수단을 coin 으로 선택하세요.")
        else:
            svc.insert_money(prompt_money())
            print("금액 투입 완료.")

    elif cmd == '3':
        code = prompt_product_code([item['code'] for item in menu])
        prod = svc.purchase(code)
        print(f"구매 완료: {prod.name} ({prod.price}원)")

    elif cmd == '4':
        change = svc.return_change()
        print("거스름돈 반환:")
        for coin, cnt in change.items():
            print(f"  {coin}원: {cnt}개")
        if input("잔돈 반환 후 종료하시겠습니까? (y/n): ").strip().lower() == 'y':
            break

    elif cmd == '5':
        while True:
            choice = prompt_admin_opt()
            if choice == 'a':
                code = input("새 상품 코드: ").strip().upper()
                name = input("상품명: ").strip()
                price = int(input("가격: ").strip())
                stock = int(input("초기 재고: ").strip())
                try:
                    svc.admin_add(code, name, price, stock)
                    print("✔ 상품 추가 완료.")
                except Exception as e:
                    print(f" 오류: {e}")

            elif choice == 'b':
                code = input("삭제할 상품 코드: ").strip().upper()
                try:
                    svc.admin_remove(code)
                    print("✔ 상품 삭제 완료.")
                except Exception as e:
                    print(f" 오류: {e}")

            elif choice == 'c':
                code = input("수정할 상품 코드: ").strip().upper()
                price = int(input("새 가격: ").strip())
                try:
                    svc.admin_update_price(code, price)
                    print("✔ 가격 수정 완료.")
                except Exception as e:
                    print(f" 오류: {e}")

            elif choice == 'd':
                code = input("재고 보충할 상품 코드: ").strip().upper()
                qty = int(input("보충 수량: ").strip())
                try:
                    svc.admin_restock(code, qty)
                    print("✔ 재고 보충 완료.")
                except Exception as e:
                    print(f" 오류: {e}")

            elif choice == 'q':
                break

            else:
                print(" 유효하지 않은 명령입니다.")

    elif cmd == 'q':
        break

    else:
        print(" 올바른 명령을 선택해 주세요.")

print("종료")
