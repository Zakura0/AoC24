with open ("input.txt", "r") as file:
    reports = file.read().strip().split("\n")
    safe = 0
for report in reports:
    report = list(map(int, report.split()))
    for i in range(len(report)):
        report_copy = report.copy()
        report_copy.pop(i)
        if all(first < next and abs(first - next) >= 1 and abs(first - next) <= 3 for first, next in zip(report_copy, report_copy[1:])):
            safe += 1
            break
        elif all(first > next and abs(first - next) >= 1 and abs(first - next) <= 3 for first, next in zip(report_copy, report_copy[1:])):
            safe += 1
            break
        else:
            continue
print(safe)
        