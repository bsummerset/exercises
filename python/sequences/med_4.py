num = [1,4,6,8,4,1,9,7]

new = []
for i in num:
    if i not in new:
        new.append(i)
print(new)