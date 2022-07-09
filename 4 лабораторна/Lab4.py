# 1. Виведіть на екран квадрати всіх чисел з проміжку від 1 до 100.
# Цикл for
# for елемент in(з) список:
for num in range(1, 101):
    # Друк (елемент+1)^2, end - закінчення друку \n
    print((num + 1) ** 2, end=" ")
print()  # перехід на наступний рядок

# 2. Дано натуральне число n. Надрукуйте всі n-значні парні натуральні числа
# в порядку зростання.
# limit = 100  # Наш ліміт

# for елемент in(із) список(range(від_елемента, до_елемента, крок)):
# for num in range(0, limit + 1, step):
#     # елемент не має дорівнювати 0
#     if num != 0:
#         # При діленні на 2 не повинно бути остачі - парне значення
#         if num % 2 == 0:
#             #  якщо наш шаг не парний, то друкуємо до 10
#             if step % 2 != 0 and num <= 10:
#                 print(num, end=" ")
#             # якщо наш шаг парний, то друкуємо до 100
#             elif step % 2 == 0 and num >= 10:
#                 print(num, end=" ")
# num = 0
# diapazon = int(input("Діапазон: "))
# print(len(str(30)))
# while True:
#     num = num + step
#     if num % 2 == 0:
#         if len(str(num)) == step:
#             print(num, end=" ")

# //////////////////////////////////////
# n = step
# i = 10 ** n
# print("i = 10**n:", i)
# while i > 10 ** (n - 1):
#
#     print("10**n:", 10 ** (n - 1))
#     e = i - 1
#     print("e:", e)
#     if e % 2 == 0:
#         print("e:", e)
#     i = i - 1
#     print("i:", i)
# ///////////////////////////////////////////
n = int(input("Натур: "))  # крок в int
minimum = 10 ** (n - 1)
Maximum = 10 ** n
while minimum < Maximum:
    # if minimum % 2 == 0:
    #     print(minimum, end= " ")
    # minimum = minimum + 1
    print(minimum, end=" ")
    minimum = minimum + 2
