import math


filename = "data_word.dat"

with open(filename) as file:
    lines = file.readlines()

numbers = []

for line in lines:
    line_numbers_string = line.strip().split()
    numbers.extend(line_numbers_string)

numbers_string = numbers.copy()

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
only_digits_True_False = True
for number in numbers_string:
    for letter in number:
        if letter not in digits:
            only_digits_True_False = False

if only_digits_True_False is True:
    numbers = list(map(float, numbers))
    min_N = min(numbers)
    max_N = max(numbers)
    sum_all = sum(numbers)
    sum_string = "(" + "+".join(numbers_string) + ")"
    prod_all = math.prod(numbers)
    prod_string = "(" + "*".join(numbers_string) + ")"
    print("Минимальное: ", min_N)
    print("Максимальное: ", max_N)
    print("Сумма: ", sum_all, sum_string)
    print("Произведение: ", prod_all, prod_string)
else:
    print("В файле содержатся буквы (ошибка)")
