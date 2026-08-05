num = [1 ,2 ,2 ,3 ,3 ,4]
checked = []

for i in num:
    if i not in checked:
        checked.append(i)

print(checked)