def merge(v):
    v.sort()
    rez = [v[0]]
    for interval in v:
        if rez[-1][1] >= interval[0]:
            rez[-1] = [min(rez[-1][0], interval[0]), max(rez[-1][1], interval[1])]
        else:
            rez.append(interval)
    return rez


v = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(v))
