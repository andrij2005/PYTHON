class Printer:
    def __init__(self, color=""):
        _pass = "1111"
        if color == "":
            self._color = input("Color: ")
        else:
            self._color = color

    def print(self):
        print(self._color)

    def __str__(self):
        return self._color

    @staticmethod
    def circle(self):
        print("hello")



print("Hello world!")

if __name__ == '__main__':
    printer_1 = Printer()
    printer_2 = Printer("Black")
    printer_2.print()
    print(printer_1)