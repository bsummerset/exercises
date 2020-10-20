list1 = [2,4,5]
list2 = [2,3,6]

products = []

for num1, num2 in zip(list1,list2):
    products.append(num1 * num2)

print(products)