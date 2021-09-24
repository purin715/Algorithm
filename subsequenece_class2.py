# 5 0
# -7 -3 -2 5 8

def get_cnt_same_as_s(now_idx, subset_sum, num_list, s):
    if now_idx == len(num_list):
        if subset_sum == s:
            return 1

        return 0

    not_include_cnt = get_cnt_same_as_s(now_idx+1, subset_sum, num_list, s)
    include_cnt = get_cnt_same_as_s(now_idx+1, subset_sum+num_list[now_idx], num_list, s)

    return include_cnt + not_include_cnt

n, s = map(int, input().split())
num_list = list(map(int, input().split()))

same_cnt = get_cnt_same_as_s(0, 0, num_list, s)

if s == 0:
    same_cnt -= 1

print(same_cnt)