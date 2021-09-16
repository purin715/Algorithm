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

def quicksort(num_list):
    if len(num_list) <= 1:
        return num_list
        
    pivot_idx = 0

    less_list = []
    more_list = []

    for num in num_list[pivot_idx+1:]:
        if num < num_list[pivot_idx]:
            less_list.append(num)
        else:
            more_list.append(num)
    
    # print(f"{less_list} + {[num_list[pivot_idx]]} + {more_list}")

    return quicksort(less_list) + [num_list[pivot_idx]] + quicksort(more_list)

n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

for num in quicksort(num_list):
    print(num)