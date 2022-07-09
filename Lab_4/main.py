x = 100
num = 5
spisoc = []
# range(от_елемента, до_елемента, шаг)
for number in range(x + 1):
    spisoc.append(number * 15)

# for елемент in(из) список:
print(spisoc)
for elem in spisoc:
    print(elem, end=" ")

print()
x = 30
while x <= len(spisoc):
    print(x, end=" ")
    if x == 50:
        break
    x += 1
    # x = x + 1

print()
for num in range(0, 100, 1):
    print(num, num % 2, num % 2 == 0)
