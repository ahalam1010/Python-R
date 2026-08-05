num = []

for i in range(1, 21):
    num.append(i)
print("Numbers: ", num)

even = []

for i in range(1, 21):
    if i % 2 == 0:
        even.append(i)
print("Even Numbers: ", even)

odd = []

for i in range(1, 21):
    if i % 2 != 0:
        odd.append(i)
print("odd Numbers: ", odd)

sq = []

for i in range(1, 11):
    sq.append(i**2)
print("Squared: ", sq)