from heapq import *


def maximum_capital(k, w, capital, profits):
    curr_cap = w
    capital_minH = []
    profit_maxH = []

    for x in range(len(capital)):
        heappush(capital_minH, (capital[x], x))

    for _ in range(k):

        while capital_minH and capital_minH[0][0] <= curr_cap:
            heappush(profit_maxH, -profits[capital_minH[0][1]])
            heappop(capital_minH)
        if not profit_maxH:
            break
        curr_cap += -(heappop(profit_maxH))

    return curr_cap


k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print(maximum_capital(k, w, capital, profits))
