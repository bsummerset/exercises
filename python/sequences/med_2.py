list1 = [[2,-2], [5,3]]
lsit2 = [[1,4], [3,2]]
new_list = []

# for list1[0], list1[1] in zip(list1[0], list1[1]):
#     new.append(list1[0] + list1[1])

# print(new)


# new = [sum(i) for i in zip(list1[0], list1[1])]
i = 0

while i < len(list1):
    j = 0
    n = []
    while j < len(list1[i]):
        n.append(list1[i][j]+lsit2[i][j])
        j += 1
    print(new_list)