import custom_var
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create a new client and connect to the server
client = MongoClient(custom_var.db_uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.website # 選擇操作 test 的資料庫 (不存在的話會創建一個)
collection = db.users # 選擇操作 users 集合

# 把資料新增到集合中
result = collection.insert_many(
    [{
        "name": "洛可可",
        "email": "rococo@wuwa.com",
        "password": "rocaille",
        "level": 3
    },{
        "name": "椿",
        "email": "tsubaki@wuwa.com",
        "password": "camellia",
        "level": 2
    }]
)
print("資料新增成功")
print(result.inserted_ids)