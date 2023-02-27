from heapq import *


def maximum_capital(c, k, capitals, profits):
    curr_cap = c
    capital_minH = []
    profit_maxH = []

    for x in range(len(capitals)):
        heappush(capital_minH, (capitals[x], x))
    for _ in range(k):
        while capital_minH and capital_minH[0][0] <= curr_cap:
            c, i = heappop(capital_minH)
            heappush(profit_maxH, (-profits[i], i))
        if not profit_maxH:
            break

        j = -heappop(profit_maxH)[0]
        # print(f"\t\tUpdated capital = {current_capital} + {j}")
        curr_cap += j
    return curr_cap
