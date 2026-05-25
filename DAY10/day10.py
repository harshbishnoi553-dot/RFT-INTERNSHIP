from collections import Counter

logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW",
    "INFO PROCESS RUNNING",
    "WARNING CPU HIGH",
    "ERROR NETWORK FAILED"
]

types = []

for log in logs:
    if "error" in log.lower():
        types.append("ERROR")
    elif "info" in log.lower():
        types.append("INFO")
    elif "warning" in log.lower():
        types.append("WARNING")

count = Counter(types)

print("ERROR:", count["ERROR"])
print("INFO:", count["INFO"])
print("WARNING:", count["WARNING"])

most_frequent = count.most_common(1)[0]
print("Most Frequent Log Type:", most_frequent[0])

