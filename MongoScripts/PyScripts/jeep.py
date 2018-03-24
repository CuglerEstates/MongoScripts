#spline hill climb algo

import pymongo 
import numpy as np
import datetime
from scipy.interpolate import UnivariateSpline as US

#database config settings 
connection = pymongo.MongoClient('localhost:27017')
db = connection.StockMarketDB
col = db.hourlyStatistics #this is where you select the table (to be redone)

prices = []
time = []

for doc in col.find().sort('date', pymongo.ASCENDING):
    prices.append(doc['low'])
    time.append(doc['date'])

xaxis = np.linspace(0,lin(time),1)

spl = US(time,prices)

##Useful loop for debugging
#for i in range(1,len(prices)):
#   print(prices[i])
#   print(timep[i])
