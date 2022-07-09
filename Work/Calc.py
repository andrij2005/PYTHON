# ValueError
var_1 = int()
var_2 = int()
while True:
    try:
        var_1 = int(input("A: "))
    except ValueError:
        continue
    except KeyboardInterrupt:
        print("Выход")
        exit()
    try:
        var_2 = int(input("B: "))
    except ValueError:
        continue
    except KeyboardInterrupt:
        print("Выход")
        exit()
    break

while True:
    try:
        menu = input("\n"
                     "1. +\n"
                     "2. -\n"
                     "3. *\n"
                     "4. /\n"
                     "5. ^2\n"
                     "6. ^3\n"
                     "7. Clear\n"
                     "8. Replay A\n"
                     "9. Replay B\n"
                     "0. Exit\n"
                     ">>> ")
        if menu == "1":
            print(f"{var_1} + {var_2} = {var_1 + var_2}")
        elif menu == "2":
            print(f"{var_1} - {var_2} = {var_1 - var_2}")
        elif menu == "3":
            print(f"{var_1} * {var_2} = {var_1 * var_2}")
        elif menu == "4":
            try:
                print(f"{var_1} / {var_2} = {var_1 / var_2}")
            except ZeroDivisionError:
                print(f"{var_1} / {var_2} = 0")
        elif menu == "5":
            print(f"{var_1}^2 {var_2}^2 = {var_1**2} {var_2**2}")
        elif menu == "6":
            print(f"{var_1}^3 {var_2}^3 = {var_1**3} {var_2**3}")
        elif menu == "7":
            print("\n"*10)
        elif menu == "8":
            try:
                var_1 = int(input("A: "))
            except ValueError:
                continue
            except KeyboardInterrupt:
                print("Выход")
                exit()
        elif menu == "9":
            try:
                var_2 = int(input("B: "))
            except ValueError:
                continue
            except KeyboardInterrupt:
                print("Выход")
                exit()
        elif menu == "0":
            break
        else:
            print("Не знайдено!")
        input()
    except KeyboardInterrupt:
        print("Выход")
        exit()
