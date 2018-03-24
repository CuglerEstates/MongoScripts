

import pymongo
import numpy
import datetime

#database config settings
connection = pymongo.MongoClient('localhost:27017')
db = connection.StockMarketDB
col = db.hourlyStatistics #this is where you select the table (to be redone)

current_day = datetime.date
delta = datetime.timedelta(days = 2) #also needs to be redone, 5 should be a var
past_day = current_day - delta

for doc in col.find().sort('date'):
    a = 1
    
