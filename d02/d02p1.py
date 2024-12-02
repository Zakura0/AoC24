with open ("input.txt", "r") as file:
    reports = file.read().strip().split("\n")
    safe = 0
for report in reports:
    report = list(map(int, report.split()))
    if all(first < next and abs(first - next) >= 1 and abs(first - next) <= 3 for first, next in zip(report, report[1:])):
        safe += 1
    elif all(first > next and abs(first - next) >= 1 and abs(first - next) <= 3 for first, next in zip(report, report[1:])):
        safe += 1

print(safe)
        