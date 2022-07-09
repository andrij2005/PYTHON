# 2
num_res = 0
while True:
    num_input = int(input("Значення: "))
    if num_input != 0:
        num_res += num_input
    else:
        print(num_res)
        break
