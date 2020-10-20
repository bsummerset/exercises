list1 = [[2,-2], [5,3]]

new = []

for list1[0], list1[1] in zip(list1[0], list1[1]):
    new.append(list1[0] + list1[1])

print(new)


# new = [sum(i) for i in zip(list1[0], list1[1])]