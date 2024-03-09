def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [0] * (amount + 1)
    coin_count = {}
    
    for i in range(1, amount + 1):
        min_coins[i] = float('inf')
        
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_count[i] = coin
    
    result = {}
    remaining_amount = amount
    
    while remaining_amount > 0:
        coin = coin_count[remaining_amount]
        result[coin] = result.get(coin, 0) + 1
        remaining_amount -= coin
    
    return result

# Приклад використання
amount = 113
print("Мінімальна кількість монет для видачі решти:", find_min_coins(amount))
