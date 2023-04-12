def min_window(str1, str2):
    min_seq = float("inf")
    seq = ""
    j = 0
    if len(str2) > len(str1):
        return ""

    for idx in range(len(str1)):
        if str1[idx] == str2[j]:
            j += 1
            if j == len(str2):
                start, end = idx, idx + 1
                while j > 0:
                    if str1[start] == str2[j - 1]:
                        j -= 1
                    if j == 0 and end - start + 1 < min_seq:
                        min_seq = min(min_seq, (end - start + 1))
                        seq = str1[start:end]
                    start -= 1
    return seq


str1 = "abcdebdde"
str2 = "bde"
print(min_window(str1, str2))
