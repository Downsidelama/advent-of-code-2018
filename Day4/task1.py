import datetime

file = "input.txt"

logs = list()

with open(file) as f:
    for line in f:
        logs.append(line)

# sorting
sorted_logs = [[datetime.datetime.strptime(ts.split(']')[0].strip('['), "%Y-%m-%d %H:%M"), ts.split(']')[1].strip()] for ts in logs]
sorted_logs = sorted(sorted_logs, key=lambda x: x[0])

minutes_asleep = dict()

current_guard = ""
min_fell_asleep = 0
min_woke_up = 0
asleep_min = dict()
for line in sorted_logs:
    if "begins shift" in line[1]:
        current_guard = line[1].split()[1]

    if "falls asleep" in line[1]:
        min_fell_asleep = line[0].minute

    if "wakes up" in line[1]:
        min_woke_up = line[0].minute
        if current_guard in asleep_min.keys():
            for i in range(min_fell_asleep, min_woke_up):
                asleep_min[current_guard][i] += 1
        else:
            asleep_min[current_guard] = [0 for x in range(0, 60)]
            for i in range(min_fell_asleep, min_woke_up):
                asleep_min[current_guard][i] += 1

max_asleep_minutes = 0
guard_id = ''
for k in asleep_min.keys():
    sum1 = sum(asleep_min[k])
    if sum1 > max_asleep_minutes:
        max_asleep_minutes = sum1
        guard_id = k

print(int(guard_id.strip('#')) * int(asleep_min[guard_id].index(max(asleep_min[guard_id]))))