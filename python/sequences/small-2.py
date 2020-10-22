my_list = [30, 43,12,45]
largest = float("-inf")

for num in my_list:
    if num > largest:
        largest = num

print(largest)