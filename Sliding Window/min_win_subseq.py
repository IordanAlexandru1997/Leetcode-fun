def min_window(str1, str2):
    j = 0
    min_length = float("inf")
    min_seq = ""
    for i in range(len(str1)):
        if str2[j] == str1[i]:
            j += 1
        if j == len(str2):
            start, end = i, i
            while j > 0:
                if str2[j - 1] == str1[start]:
                    j -= 1
                start -= 1
            curr_len = end - start
            if curr_len < min_length:
                min_length = min(curr_len, min_length)
                min_seq = str1[start + 1 : end + 1]
    return min_seq


str1 = "abcdebdde"
str2 = "bde"

print(min_window(str1, str2))
