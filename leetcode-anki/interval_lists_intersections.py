def intervalIntersection(A, B):
    i, j = 0, 0
    rez = []
    while i < len(A) and j < len(B):
        start_A, end_A = A[i][0], A[i][1]
        start_B, end_B = B[j][0], B[j][1]

        if start_A <= end_B and start_B <= end_A:
            rez.append([max(start_A, start_B), min(end_A, end_B)])
        if end_A < end_B:
            i += 1
        else:
            j += 1

    return rez


b = [[0, 2], [5, 10], [13, 23], [24, 25]]
a = [[1, 30]]
print(intervalIntersection(a, b))
