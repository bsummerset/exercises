list1 = [2,4,5]
list2 = [2,3,6]

result = []

# for num1, num2 in zip(list1,list2):
#     products.append(num1 * num2)

# print(products)

while i < len(list1):
    result.append(list1*list2[i])
    i += 1
print(result)