def circular_array_loop(arr):
    s = 0
    f = 0
    for i in range(len(arr)):
        direction = arr[i] >= 0
        s = next_step(arr, i, direction)
        f = next_step(arr, s, direction)
        while s != f and s != -1 and f != -1:
            f = next_step(arr, f, direction)
        if s == f and s != -1:
            return True
    return False


def next_step(arr, i, direction):
    nextStep = (i + arr[i]) % len(arr)
    current_direction = arr[nextStep] >= 0
    if direction != current_direction:
        return -1
    if nextStep == i:
        return -1
    return nextStep


arr = [1, 3, -2, -4, 1]
arr = [2, 1, -1, -2, 2]
arr = [1, 4, 3, 2, 1]
arr = [3, -3, 2, -2]
arr = [-2, -3, 1, -3, 2]
arr = [5, -1, 1, 1, -7, -9]
arr = [2, 5, -4, 3, -1, 4]
print(circular_array_loop(arr))
