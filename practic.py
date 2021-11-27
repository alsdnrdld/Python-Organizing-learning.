from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

all_movies = list(db.movies.find({}))  #여러 개를 보려면 list로 묶어 줘야한다!!!


title = db.movies.find_one({'title':'매트릭스'})  # 한 개만 보려면 list로 묶으면 안된다.
print(title['point'])
t1 = title['point']



title2 = list(db.movies.find({'point':t1}))  # 여러 개를 볼꺼면 list를 씌워줘야 한다.

for movieC in title2:
    print(movieC['title'])


db.movies.update_one({'title':'매트릭스'},{'$set':{'point':0}})