# Cricket statistics analysis.

runs = [45, 78, 102, 34, 56, 89, 12, 150, 67, 99, 23, 110, 5, 72, 48]

total_runs = 0
highest_score = runs[0]
lowest_score = runs[0]
half_centuries = 0
centuries = 0

for score in runs:
    total_runs += score

    if score > highest_score:
        highest_score = score

    if score < lowest_score:
        lowest_score = score

    if score >= 50:
        half_centuries += 1

    if score >= 100:
        centuries += 1

average_runs = total_runs / len(runs)

print("Runs:", runs)
print("Total runs:", total_runs)
print("Average runs:", average_runs)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Number of half-centuries:", half_centuries)
print("Number of centuries:", centuries)