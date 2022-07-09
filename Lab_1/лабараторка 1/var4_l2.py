# 2. Дано тризначне число. Перевірити чи
# a) містить воно цифру 2;
# b) складається лише з парних чисел;
# c) сума його цифр дорівнює 18
num = int ( input ( "тризнач число: " ) )

# a) містить воно цифру 2;
num_a = num
for x in range ( 3 ):
    if num_a % 10 == 2 :
        print ( "знайшов" )
    num_a = int(num_a / 10)

# b) складається лише з парних чисел;
num_b = num
parnoe = True
for x in range ( 3 ) :
    if (num_b % 10) % 2 != 0 :
        print ( "не парне", num_b % 10 )
        parnoe = False
    num_b = int(num_b / 10)
if parnoe:
    print("Всі парні")

# c) сума його цифр дорівнює 18
num_c = num
sum = 0
for x in range ( 3 ) :
    sum = sum + num_c % 10
    num_c = int(num_c / 10)
if sum == 18:
    print("равно 18")