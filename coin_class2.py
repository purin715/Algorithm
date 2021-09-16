result_coin_cnt = 0

coins_list = [500, 100, 50, 10, 5, 1]
charge_money = 1000 - int(input())

# iteration

for coin in coins_list:
    result_coin_cnt += charge_money // coin
    charge_money %= coin

print(result_coin_cnt)

# recursion

def calc_coin(charge_money, i, coins_list):
    if i == len(coins_list):
        return 0

    return charge_money // coins_list[i] + calc_coin(charge_money % coins_list[i], i+1, coins_list)

print(calc_coin(charge_money, 0, coins_list))