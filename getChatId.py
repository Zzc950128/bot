from telethon import TelegramClient
from pymongo import MongoClient

app_id = 237708
app_hash = '500d225c06f5427ac74c38c69fb24686'
phone_number = '+8613020305798'

client = TelegramClient('zhangzhicong', app_id, app_hash)
client.start()

mongo = MongoClient('localhost',27017)
db = mongo.zzc
user_col = db.list
#mes_col = db.mes

for item in user_col.find():
	if item['type'] != 'User':
#		print(item)
		msg = client.get_entity(item['title'])
		print(msg)
