"""
Пользователь делает вклад в размере N грн. сроком
на YEARS лет под 10% годовых (каждый год размер
его вклада увеличивается на 10%. Эти деньги
прибавляются к сумме вклада, и на них в следующем
году тоже будут проценты).

Тут надо функция bank(money: int, years: int)
а далее логику по циклу while / for range
"""


def bank(money: int, years: int):
    for num in range(years):
        print(f"Деньги: {money:.0f} / год: {num + 1}\n"
              f"Процент за этот год: {money*0.1:.0f}")
        money += money*0.1
    print(f"ИТОГО Деньги: {money:.0f}")
    return int(money)


def pri(money: int):
    print(int(money-(money*0.195)))


pri(bank(1700, 3))
pri(bank(3000, 12))
