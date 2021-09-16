# 8
# 1 1 0 0 0 0 1 1
# 1 1 0 0 0 0 1 1
# 0 0 0 0 1 1 0 0
# 0 0 0 0 1 1 0 0
# 1 0 0 0 1 1 1 1
# 0 1 0 0 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1

# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1

def check_same_color(start_y, start_x, length, paper_map):
    for y in range(start_y, start_y+length):
        for x in range(start_x, start_x+length):
            if paper_map[y][x] != paper_map[start_y][start_x]:
                return False

    return True

def split_paper(start_y, start_x, length, paper_map):
    if check_same_color(start_y, start_x, length, paper_map):
        if paper_map[start_y][start_x] == 0:
            return [1, 0]
        
        return [0, 1]
    
    total_paper_cnt = [0, 0]
    half_len = int(length/2)

    start_locs = [
        [start_y, start_x],
        [start_y, start_x+half_len],
        [start_y+half_len, start_x],
        [start_y+half_len, start_x+half_len]
    ]

    for y, x in start_locs:
        white_cnt, blue_cnt = split_paper(y, x, half_len, paper_map)
        total_paper_cnt[0] += white_cnt
        total_paper_cnt[1] += blue_cnt

    return total_paper_cnt

n = int(input())
paper_map = []

for _ in range(n):
    paper_map.append(list(map(int, input().split())))

for num in split_paper(0, 0, n, paper_map):
    print(num)