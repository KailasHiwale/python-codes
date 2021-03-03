import pickle


westeros = {
	'starks': ['ned', 'rob', 'branden', 'arya', 'sansa'],
	'lannisters': ['tywin', 'jaime', 'tyrian', 'cersei'],
} 

# function dump data
def pickle_dump(fpath):
	with open(fpath, 'wb') as file:
		pickle.dump(westeros, file)
	return True


# function to load data
def pickle_load(fpath):
	with open(fpath, 'rb') as file:
		westeros = pickle.load(file)
	return westeros


# start
if __name__ == '__main__':
	file_path = 'data/westeros.pickle'

	# step 1
	# status = pickle_dump(file_path)
	# print(status)

	# step 2
	westeros = pickle_load(file_path)
	print(westeros)

