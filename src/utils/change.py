def get_change(amount, coins):
    change = {}
    remaining = amount
    for coin in coins:
        count, remaining = divmod(remaining, coin)
        if count:
            change[coin] = count
        if remaining == 0:
            break
    return change
