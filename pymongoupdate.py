from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})   # 고치려는 곳에 {'$set':{'항목명': -바꾸려는 내용- } 형태로 써준다.