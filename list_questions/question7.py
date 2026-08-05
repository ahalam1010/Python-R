num = [1 ,2 ,2 ,3 ,1 ,1]

checked = []

for i in num:
    if i not in checked:
        frequency = num.count(i)
        print(f"{i} -> {frequency}")
        checked.append(i)