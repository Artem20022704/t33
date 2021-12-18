import math

from datetime import datetime


with open(filename) as file:
    lines = file.readlines()

numbers = []

for line in lines:
    line_numbers_string = line.strip().split()
    numbers.extend(line_numbers_string)

numbers_string = numbers.copy()
numbers = list(map(float, numbers))

min_N = min(numbers)

max_N = max(numbers)

sum_all = sum(numbers)

print("Минимальное: ", min_N)
print("Максимальное: ", max_N)
print("Сумма: ", sum_all)

N_numbers = len(numbers)
N_max = 100000
if N_numbers < N_max:
    prod_all = math.prod(numbers)
    print("Произведение: ", prod_all)
else:
    print("Чисел больше, чем ", N_max)

