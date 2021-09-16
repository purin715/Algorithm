# 60466175 36
# 10 2

n, b = map(int, input().split())
result_list = []

# q, r = divmod(n, b) # 10 2, 5 0
# result_list.append(r) # 0

# q, r = divmod(q, b) # 5 2, 2 1
# result_list.append(r) # 1

# q, r = divmod(q, b) # 2 2, 1 0
# result_list.append(r) # 0

# q, r = divmod(q, b) # 1 2, 0 1
# result_list.append(r) # 1

# ...
#

char_num_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

q = n
while q > 0:
    # q = q // b
    # r = q % b
    q, r = divmod(q, b)
    
    # 1)
    if r >= 10:
        result_list.append(chr(ord('A') + (r - 10)))
    else:
        result_list.append(str(r))

    # 2)
    # result_list.append(char_num_map[r])

print("".join(result_list[::-1]))