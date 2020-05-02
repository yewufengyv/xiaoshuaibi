#!/usr/bin/python3
from pymongo import MongoClient

class search(object):
	def _init_(self):
		pass

	def mongo(self):
		mon=MongoClient('127.0.0.1:27017')
		db=mon["xiao"]
		jiaocheng=db["jiaocheng"]
		return jiaocheng

	def search_func(self,char_,db):
		symbol={'neirong':{"$regex":char_}}
		a=db.find(symbol)
		print('Start query')
		for i in a:
			print(i)
if __name__ == '__main__':
	s=search()
	jiaocheng=s.mongo()
	char_=input('Please enter a query field:')
	s.search_func(char_,jiaocheng)
