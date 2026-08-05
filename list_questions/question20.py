runs = [45, 67, 102, 34, 88, 12, 115, 56, 73, 29, 100, 49, 81, 7, 64]

total = 0
for i in runs:
    total += i

print("Total Runs: ", total)

average = total / len(runs)

print("The average runs: ", average)

print("The highest run: ", max(runs))
print("The lowest run: ", min(runs))

half = 0
for i in runs:
    if i >= 50:
        half += 1
print("The number of half-centuries: ", half)

full = 0
for i in runs:
    if i >= 100:
        full += 1
print("The number of centuries: ", full)

