def vandind_machine(money):
    # 음료수 가격
    drink_price = 700

    #음료수 개수& 잔돈 계산
    num_drink = money // drink_price
    change = money % drink_price
    print(f'{money}원를 넣었을 때 음료수 = {num_drink}잔 잔돈 = {change}원')

vandind_machine(3000)