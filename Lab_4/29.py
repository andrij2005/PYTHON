# 29. Напишіть програму, яка обчислює частку студентів, які отримали оцінку A.
# Використовується п’ятибальна система оцінювання з оцінками A, B, C, D, F.
# Вводиться рядок, в якому через пропуск записані оцінки студентів. Оцінок
# завжди не менш однієї. Виводиться дробове число з рівно двома знаками після
# коми.
# Вхідні дані:
# A B A A B C A D F
# A A A A A
# A F
# B B C B F F B C F

# Бескінечний цикл завдяки True
while True:
    # Створили список із вводу де перевели у верхній регістр та прибрали усі пробіли
    # a b a A b C A d F
    # ABAABCADF
    # A, B, A, A, B, C, A, D, F
    rating = list(input("Оцінки: ").upper().replace(" ", ""))
    # Далі просто рахуемо скільки в списку елементів А та ділемо на загальну кількість елементів
    # рахувати А завдяки count
    # загальна кількість завдяки len
    # 2 цифри після крапки - :.<Цифра>f
    print(f"{rating.count('A')/len(rating):.2f}")

# Вихідні дані:
# 0.44
# 1.00
# 0.50
# 0.00
