# --- TEXT ---
# def funck(TEXT):
#     print(--- TEXT ---)
def print_new(txt):
    print("---", txt, "---")

# Створи мені ступеньки завдяки print та якось for чи while
# print("O"*3) #OOO
a = 5
while a > 0:
    print("0"*a)
    a -= 1


def s(num: int, subl: str):
    for a in range(1, num+1):
        print(subl*a)


if __name__ == '__main__':
    x = 5
    s(5, "x")
    s(int(input()), "X")