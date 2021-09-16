# 4 3 7 2 5 0 6 1
# 34 27 05 16
# 2347 0156
# 01234567

# 5 4 3 2 1 ?
# 4 5 2 3 1

n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

target_size = 1

while target_size < n:
    start_idx = 0

    while start_idx < n:
        mid_idx = min(start_idx + target_size - 1, n-1)
        end_idx = min(mid_idx + target_size, n-1)

        # front, start_idx ~ mid_idx
        # back, mid_idx+1 ~ end_idx

        f_idx = start_idx
        b_idx = mid_idx+1
        combined_list = []

        while f_idx <= mid_idx and b_idx <= end_idx:
            if num_list[f_idx] < num_list[b_idx]:
                combined_list.append(num_list[f_idx])
                f_idx += 1
            else:
                combined_list.append(num_list[b_idx])
                b_idx += 1

        combined_list = combined_list + num_list[f_idx:mid_idx+1] + num_list[b_idx:end_idx+1]
        num_list[start_idx:end_idx+1] = combined_list

        # print(combined_list)
        # print(num_list)

        start_idx = end_idx+1

    target_size *= 2

for num in num_list:
    print(num)