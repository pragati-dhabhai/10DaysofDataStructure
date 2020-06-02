def buy_and_sell_stock_once(prices):
    p_max=0
    for i in range(0,len(prices)):
        for  j in range(i+1,len(prices)):
            profit=prices[j]-prices[i]
            p_max=max(profit,p_max)
    return p_max
    
    
