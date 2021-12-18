import math

from datetime import datetime
time_understandable = datetime.today().strftime("%H:%M:%S")

time_begin = time_understandable

filename = "data_big.dat"
N = 5000000
numbers = [i for i in range(1,N)]
numbers_string = list(map(str, numbers))
numbers_string_to_file = " ".join(numbers_string)

with open(filename,'w') as file:
    file.write(numbers_string_to_file)
    


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

prod_all = math.prod(numbers)



print("Минимальное: ", min_N)
print("Максимальное: ", max_N)
print("Сумма: ", sum_all)
print("Произведение: ", prod_all)


time_end = datetime.today().strftime("%H:%M:%S")

print("Время начала:   ", time_begin)
print("Время окончания:", time_end)
