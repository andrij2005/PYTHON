# for num in range(1, 6):
#     print(num, end=" ")
# num = 0
# while num < 7:
#     num += 1
#     print(num, end=" ")
# print()
#
# num = 8
# while num > 1:
#     num -= 1
#     print(num, end=" ")
# print()

# a = {'wwww': 234, "asd": 111}
# print(a['wwww'])
# a['wwww'] = 555
# print(a)
# print(a['wwww'])

while True:
    x = input("1. Войти\n"
              "2. Выйти\n"
              "3. Продолжить\n"
              ">>> ")
    if x == "1":
        print("Вошёл")
    elif x == "2":
        break
    elif x == "3":
        continue
    else:
        print("Не понимаю!")

    print("Конец while\n\n")
