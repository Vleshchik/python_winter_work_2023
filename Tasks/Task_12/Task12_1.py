lst = list(map(int, input().split())) #1 2 3 4 1 2 3 4 1 4
def min_max_pos(lst):
    max_pos = [i for i in range(len(lst)) if lst[i] == max(lst)]
    min_pos = [i for i in range(len(lst)) if lst[i] == min(lst)]
    return min_pos, max_pos
print(*min_max_pos(lst))