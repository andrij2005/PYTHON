# s = input("Text: ")
# print(s.split(","))
# print(tuple(string.split(",")))

# s = input("Text: ")


def set_list(string: str, spl: str = " "):
    return string.split(spl)


def set_tuple(string: str, spl: str = " "):
    return tuple(string.split(spl))


def add(ls: list, item):
    ls.append(item)


# print(5)
# print("5")


def int_to_str(num: int):
    return str(num)


if __name__ == '__main__':
    s = "a sdasdsad asdasd 45 45 45 4 54 512 12 136 5"
    x = set_list(s)
    print(x)
    # x.append(99999999999)
    # print(x)
    print(set_tuple(s))
    add(x, "UA")
    print(x)
    print(5 + 6)
    print(int_to_str(5) + "6")
