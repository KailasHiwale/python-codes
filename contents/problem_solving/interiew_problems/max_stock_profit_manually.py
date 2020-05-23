"""
Proble Statement: Write an algo. for maximum profit a user can 
get by buying and saling the stock on perticular dates.
- Input: Share price list.
- Output: min price date, max price date and max profit
- Expected output:
    Algorithm should find date on which stock should buy and sale. So that
	Investor will get max profit.
- Constraint - Buying date should come befor saling date.
"""


def min_custom(lst):
	min_val = lst[0]
	for item in lst:
		if min_val > item:
			min_val = item
	return min_val


def max_custom(lst):
	max_val = lst[0]
	for item in lst:
		if max_val < item:
			max_val = item
	return max_val


# function return list len
def len_list(lst):
	count = 0
	for i in lst:
		count += 1
	return count


# function returns index of item in list
def index_of(item, lst):
	len_lst = len_list(lst)
	



def max_profit(price_lst):
	"""Function to get max profit for a stock."""
	min_price, max_price = min_custom(price_lst), max_custom(price_lst)
	min_price_date, max_price_date = index_of(min_price, price_lst), index_of(max_price, price_lst)
	# Condition - buying date must came before salling date.
	if min_price_date <= max_price_date:
		max_profit = max_price - min_price
	else:
		min_price = min_custom(price_lst[:max_price_date+1])
		min_price_date = pindex_of(min_price, price_lst)
		max_profit = max_price - min_price
	return min_price_date, max_price_date, max_profit


if __main__ = '__main__':
	number_of_days = 10
	price_lst = [120, 125, 140, 135, 133, 147, 145, 143, 101, 102]
	buy_date, sale_date, profit = max_profit(price_lst)
	print(buy_date, sale_date, profit)
