import time
from collections import defaultdict

def find_coins_greedy(money_sum):
    available_money = [50, 25, 10, 5, 2, 1]

    change = {}

    for num in available_money:

        # скільки разів монета влазить в суму
        count = money_sum // num 

        if count > 0:
            change[num] = count
            money_sum  -= num * count

    return change


def find_min_coins(money_sum):

    available_money = [50, 25, 10, 5, 2, 1]

    minimum_money = [0] + [float("inf")] * money_sum

    last_coin = [0] * (money_sum + 1)

    for s in range(1, money_sum + 1):
        for coin in available_money:
            if s >= coin and minimum_money[s - coin] + 1 < minimum_money[s]:
                minimum_money[s] = minimum_money[s - coin] + 1
                last_coin[s] = coin

    change = {}
    current = money_sum
    while current > 0:
        coin = last_coin[current]
        change[coin] = change.get(coin, 0) + 1
        current -= coin

    return change


def test(amounts):
    for s in amounts:
        print(f"\nСума: {s}")

        start = time.time()
        greedy = find_coins_greedy(s)
        greedy_time = time.time() - start
        print(f"Greedy: {greedy} | час: {greedy_time:.6f} c")

        start = time.time()
        dp = find_min_coins(s)
        dp_time = time.time() - start
        print(f"DP: {dp} | час: {dp_time:.6f} c")


if __name__ == "__main__":
    test([113, 3456, 65738, 987654])