"""
:Created on: May 27th, 2020
:Company: NTTDATA
:Proble Statement: Write an algo. for maximum profit a user can 
get by buying and saling the stock on perticular dates.
- Input: Share price list.
- Output: min price date, max price date and max profit
- Expected output:
    Algorithm should find date on which stock should buy and sale. So that
	Investor will get max profit.
- Constraint - Buying date should come befor saling date.
"""


def max_profit(price_lst):
	"""Function to get max profit for a stock."""
	min_price, max_price = min(price_lst), max(price_lst)
	min_price_date, max_price_date = price_lst.index(min_price), price_lst.index(max_price)
	# Condition - buying date must came before salling date.
	if min_price_date <= max_price_date:
		max_profit = max_price - min_price
	else:
		min_price = min(price_lst[:max_price_date+1])
		min_price_date = price_lst.index(min_price)
		max_profit = max_price - min_price
	
	return min_price_date, max_price_date, max_profit


if __name__ == '__main__':
	price_lst = [120, 125, 140, 135, 133, 147, 145, 143, 101, 102]
	buy_date, sale_date, profit = max_profit(price_lst)
	print(buy_date, sale_date, profit)