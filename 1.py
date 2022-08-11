import random
with open("cs.txt", 'a') as file:
    for _ in range(100):
        file.write(str(random.randint(0, 999999))+"\n")
