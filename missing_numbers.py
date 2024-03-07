maximum_number = int(input(''))
numbers = input("")
number_list = numbers.split()
total = sum(map(int, number_list))
sum_number=0
sum_test=0
for i in range(maximum_number):
    sum_number += 1
    sum_test += sum_number
print(sum_test-total)
