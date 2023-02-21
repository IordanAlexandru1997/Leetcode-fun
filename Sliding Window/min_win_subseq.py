

def min_window(str1, str2):
    min_len = float('inf')
    min_seq = ""
    j = 0
    for i in range(len(str1)):
        if str1[i] == str2[j]:
            j+=1
        if j == len(str2):

