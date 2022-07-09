line = input("Рядок: ")
line_list = line.split(" ")
# print(line_list)

nam = 0
print(line)
for num in line_list:
    # Змінити останю на велику
    # порахувати наші слова
    nam = nam + 1
    print(f"{num[:len(num)-1]}{num[-1:].upper()}", end=" ")


print("\nСлова що змінені:", nam)
