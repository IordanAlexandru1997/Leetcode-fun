def find_repeated_sequences(s, k):
    d = {}
    for start in range(0, len(s) - k + 1):
        d[s[start:k]] = 1 + d.get(s[start:k], 0)
        k += 1
    return [k for k, v in d.items() if v >= 2]


s = "AGCTGAAAGCTTAGCTG"
s = "CCATATGTATGGATAT"
k = 6

print(find_repeated_sequences(s, k))
rttyuibnyujllliou tkuybm,ymfsfhk jk