# 5
# 5
# 4
# 3
# 2
# 1

# 9
# 5
# 3
# 8
# 4
# 9
# 1
# 6
# 2
# 7

# 1 3 2 4 [5] 9 6 8 7
# 1 2 3 4 5 6 7 8 9

# 5 4 3 2 1

def quicksort(start_idx, end_idx, num_list):
    if end_idx - start_idx + 1 <= 1:
        return

    # [select pivot]

    pivot_vals = []
    pivot_idxes = [
        start_idx,
        (start_idx+end_idx)//2,
        end_idx,
    ]

    for idx in pivot_idxes:
        pivot_vals.append(num_list[idx])
    
    mid_val = sum(pivot_vals) - max(pivot_vals) - min(pivot_vals)
    mid_idx = pivot_idxes[pivot_vals.index(mid_val)]

    num_list[mid_idx], num_list[start_idx] = num_list[start_idx], num_list[mid_idx]

    pivot_idx = start_idx
    f = start_idx+1
    r = end_idx

    while f <= r:
        while num_list[r] > num_list[pivot_idx]:
            r -= 1

        while f <= r and num_list[f] < num_list[pivot_idx]:
            f += 1

        if f <= r:
            num_list[f], num_list[r] = num_list[r], num_list[f]

    print(num_list)
    num_list[r], num_list[pivot_idx] = num_list[pivot_idx], num_list[r]

    quicksort(start_idx, r-1, num_list)
    quicksort(r+1, end_idx, num_list)


n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

quicksort(0, n-1, num_list)

for num in num_list:
    print(num)