def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
        
        if amount == 0:
            break
    
    return result

# Приклад використання
amount = 113
print("Результат використання жадібного алгоритму:", find_coins_greedy(amount))
