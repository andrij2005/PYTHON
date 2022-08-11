while True:
    num = int(input("вкажіть свій вік >> "))
    if num <= 17:
        print("ви ще не доросли до цього відео")
        break
    else: print("добре дивись")


def sss(a: int, b: int):
    return a/b

print(sss(15,5))

for i in range(15, 100, 15):
    print( "hello")
    if i == 15:
        print (f"i <<< {i}")
    elif i == 30:
        print(f"{i} <<< i")

