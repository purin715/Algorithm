# 3 1

# 1
# 2
# 3

# ------

# 4 2

# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3

def get_combination(now_idx, n, m, result_list, used_list):
    if now_idx == m:
        print(" ".join(map(str, result_list)))
        return
    
    for i in range(1, n+1):
        if not used_list[i]:
            used_list[i] = True
            get_combination(now_idx+1, m, result_list + [i], used_list)
            used_list[i] = False

n, m = map(int, input().split())
used_list = [False] * (n+1)

get_combination(0, n, m, [], used_list)