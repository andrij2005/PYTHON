"""
Написать функцию сезон - season, принимающую 1
аргумент — int номер месяца (от 1 до 12), и
возвращающую время года, которому этот месяц
принадлежит (зима, весна, лето или осень).
12/4=3 - на каждый сезон по 3 месяца
"""


def season(mounth: int):
    if mounth == 12 or 1 <= mounth <= 2:
        print("Зима")
    elif 3 <= mounth <= 5:
        print("Весна")
    elif 6 <= mounth <= 8:
        print("Лето")
    elif 9 <= mounth <= 11:
        print("Осень")
    else:
        print("1-12 ->", mounth)


for num in range(16):
    print(num, ": ", end="")
    season(num)
