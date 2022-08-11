# 0/0/0
# 0/0/0
# 0/0/0
# 1 - x
# 2 - o
pole = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def win(user: int):
    win_arr = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (3, 6, 9), (2, 5, 8))
    arr = []
    for x in pole:
        for y in x:
            arr.append(y)
    # print(arr)
    for win_pole in win_arr:
        if arr[win_pole[0] - 1] == arr[win_pole[1] - 1] == arr[win_pole[2] - 1] and arr[win_pole[0] - 1] != 0:
            if user == 1:
                print("ПЕРЕМОГА! X")
            else:
                print("ПЕРЕМОГА! O")
            info()
            exit()


def info():
    chek = 1
    for x in pole:
        for y in x:
            if y == 0:
                print("-", end=" ")
            elif y == 1:
                print("X", end=" ")
            elif y == 2:
                print("O", end=" ")
        print(" | ", end=" ")
        for _ in range(3):
            print(chek, end=" ")
            chek += 1
        print()


def logic(position: int, user: int):
    if position <= 0 or position > 9:
        print("Нету такой ячейки!")
        return True
    elif 1 <= position <= 3:
        # print("lvl 1")
        if pole[0][position - 1] == 0:
            pole[0][position - 1] = user
        else:
            print("Ячейка занята!")
            return True
    elif 4 <= position <= 6:
        # print("lvl 2")
        if pole[1][position - 4] == 0:
            pole[1][position - 4] = user
        else:
            print("Ячейка занята!")
            return True
    elif 7 <= position <= 9:
        # print("lvl 3")
        if pole[2][position - 7] == 0:
            pole[2][position - 7] = user
        else:
            print("Ячейка занята!")
            return True
    win(user)
    return False


gender = 0
info()
while True:
    if gender % 2 == 0:
        while logic(int(input("(Игрок X) Где ставим крестик? :> ")), 1):
            info()
    else:
        while logic(int(input("(Игрок O) Где ставим крестик? :> ")), 2):
            info()
    gender += 1
    info()
