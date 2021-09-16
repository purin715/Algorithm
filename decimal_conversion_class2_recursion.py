def decimal_conv(idx, before_num_str, before_cipher_num):
    if idx == len(before_num_str):
        return 0

    pow_num = len(before_num_str)-1-idx

    if before_num_str[idx].isdigit():
        num_val = int(before_num_str[idx])
    else:
        num_val = ord(before_num_str[idx]) - ord('A') + 10
    
    return num_val * (before_cipher_num ** pow_num) + decimal_conv(idx+1, before_num_str, before_cipher_num)

# def decimal_conv_dict(idx, before_num_str, before_cipher_num, char_dict):
#     if idx == len(before_num_str):
#         return 0

#     pow_num = len(before_num_str)-1-idx

#     return char_dict[before_num_str[idx]] * (before_cipher_num ** pow_num) + decimal_conv_dict(idx+1, before_num_str, before_cipher_num, char_dict)

n, b = input().split()

# 1)
print(decimal_conv(0, n, int(b)))

# 2)
# char_dict = {}

# for i in range(0, 36):
#     if i < 10:
#         char_dict[str(i)] = i
#     else:
#         char_dict[chr(i + ord('A') - 10)] = i

# print(decimal_conv_dict(0, n, int(b), char_dict))