import requests


def get_usernames(threshold):
	"""
	Function performs -
		1. REST API call and 
		2. Processing on api response to get the list denoting the usernames of
		   the users whose submission count is strictly greater than the given
		   threshold.

	:param int threshold: threshold value to list usernames
	:return: List denoting the usernames
	:rtype: list
	"""
	active_user_lst, total_pages  = [], 1
	status, count = True, 1
	while status and count <= total_pages:
		uri = 'https://jsonmock.hackerrank.com/api/article_users/search?page={}'.format(count)
		api_response = requests.get(uri)
		if api_response.status_code != 200:
			status = False
			global reason
			reason = api_response.reason
			continue
		else:
			count += 1
			data_dict = api_response.json()
			total_pages = data_dict['total_pages']
			tmp = [user['username'] for user in data_dict['data'] \
				   if user['submission_count'] > threshold]
			active_user_lst.extend(tmp)	
	return active_user_lst


def run():
	"""Gets threshold value from terminal and prints the result."""
	try:
		threshold = int(input('Enter threshold number: '))
		if threshold >= 0:
			most_active_user_lst = get_usernames(threshold)
			if most_active_user_lst:
				for username in most_active_user_lst:
					print(username)
			else:
				print(reason)
		else:
			print("Invalid threshold value.")
	except Exception as e:
		print(e)


# Start
if __name__ == '__main__':
	run()
	
