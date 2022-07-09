num_1 = int(input ( "Введіть значення num_1: " ))
num_2 = int(input ( "Введіть значення num_2: " ))
num_3 = int(input ( "Введіть значення num_3: " ))

if num_1 % 2 == 0 and num_2 % 2 == 0 and num_3 % 2 == 0:
    print(num_1*num_2*num_3)
else:
    print((num_1+num_2+num_3)** 2 )
