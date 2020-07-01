import json
import os
from pymongo import MongoClient


def json_to_mongodb(collections_lst, db_name):
	try:
		client = MongoClient('localhost', 27017)
		db = client[db_name]
		for collection in collections_lst:
			db_collection = db[collection]
			with open(collection + '.json') as file:
				file_data = json.load(file)
			db_collection.insert(file_data)
		return 'completed'
	except Exception as e:
		print(e)
		return 'failed'
	finally:
		client.close()


if __name__ == '__main__':
	collections = ['test1', 'test2', 'test3']
	db_name = 'testdb'
	status = json_to_mongodb(collections, db_name)
	print(status)

