# 12
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 12
# 8 11
# 2 13
# 14 14
# 12 14

n = int(input())
meet_time = []

for _ in range(n):
    start_time, end_time = map(int, input().split())
    # meet_time.append((start_time, end_time))
    # meet_time.append({"st_time": start_time, "ed_time": end_time})

    meet_time.append((end_time, start_time))

print(meet_time)
# meet_time.sort(key=lambda row: [row[1], row[0]])
# meet_time.sort(key=lambda row: [row["st_time"], row["ed_time"]])
meet_time.sort()
print(meet_time)

result_meet_cnt = 1
booked_meet_end_time = meet_time[0][0]

for meet in meet_time[1:]:
    end_time, start_time = meet

    if booked_meet_end_time <= start_time:
        result_meet_cnt += 1
        booked_meet_end_time = end_time
        # print((start_time, end_time))

print(result_meet_cnt)
