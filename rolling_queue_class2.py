from collections import deque

n, m = map(int, input().split())
target_list = map(int, input().split())

num_list = deque([i for i in range(1, n+1)])
min_total_move_cnt = 0

# print(num_list)

for find_num in target_list:
    move_cnt = -(num_list.index(find_num))
    
    # if move_cnt > len(num_list) // 2:
    # if move_cnt > int(len(num_list) / 2):
    if abs(move_cnt) > len(num_list) + move_cnt:
        move_cnt = len(num_list) + move_cnt

    # print(move_cnt)

    min_total_move_cnt += abs(move_cnt)

    # num_list.append(num_list.pop(0)) # left 1칸
    # num_list.insert(0, num_list.pop()) # right 1칸

    # num_list.append(num_list.popleft())
    # num_list.appendleft(num_list.pop())

    num_list.rotate(move_cnt)
    # print(num_list)
    num_list.popleft()
    # print(num_list)

print(min_total_move_cnt)