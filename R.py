# while i>=n:
# suma += i # suma = suma + i
# i=i+1
# print(suma)'''
# #Написати програму, яка при довільній послідовності
# #любих цілих чисел визначає кількість чисел більшу 6.
# # Ввід чисел закінчуємо 0. (3 8 15 24 36 3 8 45 0)
num = input("Числа: ")
num = num.split(" ")

for nam in num:
    if int(nam) % 2 == 0 and int(nam) >= 6:
        nam = len(num)
        print(" ".join(num), ":", nam)
    elif "0" == nam:
        break

