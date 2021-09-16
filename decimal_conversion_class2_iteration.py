# [iteration]

# n, b = input().split()
# decimal_num = 0

# # char_dict = {'0': 0, '1': 1, ..., 'Y': 34, 'Z': 35}
# # char_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# for i in range(len(n)):
#     pow_num = len(n)-1-i

#     if n[i].isnumeric():
#         num_val = int(n[i])
#     else:
#         num_val = ord(n[i]) - ord('A') + 10

#     decimal_num += num_val * (int(b) ** pow_num)
    
#     # decimal_num += char_dict[n[i]] * int(b) ** pow_num
#     # decimal_num += char_str.index(n[i]) * int(b) ** pow_num

# print(decimal_num)