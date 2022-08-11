def s(max: int = 5, char: str = "#"):
    a = 0  # Начало
    while a < max:  # цикл пока тру - правда
        a += 1
        print(char * a)


def hello(name):
    print("hello", name)


def hello_inp():
    hello(input("Name:"))


def revers(string: str):
    a = len(string) - 1
    while a >= 0:
        print(string[a], end="")
        a -= 1
    print()


def revers_str(string: str):
    print(string[::-1])


""" 
Значення + чи -
повертаэ try folse
"""


def chek(num: int):
    if num > 0:
        print(num, "- положительное!")
        return True
    else:
        print(num, "- отрицательное!")
        return False


chek(6)
chek(-6)
chek(-6)
chek(-6)
chek(6)

revers("123456789")
revers_str("123456789")
# hello("SAdsasd")
# hello_inp()
# s(4, "5")

# def rec_1(num: int):
#     if num != 1:
#         print(num)
#         rec_1(num+1)
#     else:
#         print("Ehhooo!", num)

#
# rec_1(2)

