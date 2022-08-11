
class Car:
    # def __init__(self, color=""):
    #     if color == "":
    #         self._color = input("Color: ")
    #     else:
    #         self._color = color

    def __init__(self, color: str = "", engine: float = "", brand: str = ""):
        if color == "":
            self.color = input("Color: ")
        else:
            self.color = color

        if engine == "":
            self.engine = float(input("Engine: "))
        else:
            self.engine = engine

        if brand == "":
            self.brand = input("Brand: ")
        else:
            self.brand = brand

    def __str__(self):
        return f"Color: {self.color}\n" \
               f"Engine: {self.engine}\n" \
               f"Brand: {self.brand}\n"


if __name__ == '__main__':
    x = Car("Black", 1.7, "BMW")
    print(x.brand, x.engine, x.color)
    print(x)
    l = []
    for i in range(5):
        l.append(Car("Black", i*2+2, f"{i*3.3}"))

    print(l)

    for i in l:
        print(i)

# Сделать класс котика и собачки у которых будет свой цвет +
#  + при печати говорило он мяу или гав
# сделай мне 3 функции, 1 - умножение, 2- деление, 3 - просто +