# 1)

def convert_from_dec(q, b):
    if q == 0:
        return ""

    q, r = divmod(q, b)

    if r >= 10:
        char_str = chr(ord('A') + (r - 10))
    else:
        char_str = str(r)

    return convert_from_dec(q, b) + char_str

n, b = map(int, input().split())
print(convert_from_dec(n, b))

# 2)

# def convert_from_dec_map(q, b, char_num_map):
#     if q == 0:
#         return ""

#     q, r = divmod(q, b)
#     return convert_from_dec_map(q, b, char_num_map) + char_num_map[r]

# char_num_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# n, b = map(int, input().split())
# print(convert_from_dec_map(n, b, char_num_map))
