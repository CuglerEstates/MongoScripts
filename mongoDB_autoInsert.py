#Python2.7 Script for Ubuntu 16.04

import os
from pprint import pprint

try:
    import pip
except ImportError:
    os.system('sudo apt install python-pip -y')
    os.system('sudo pip install --upgrade pip')
    import pip
    
try:
    import pymongo
    from pymongo import MongoClient
except ImportError:
    pip.main(['install', 'pymongo'])
    import pymongo
    from pymongo import MongoClient
    
try:
    import alpha_vantage
    from alpha_vantage.timeseries import TimeSeries
except ImportError:
    pip.main(['install', 'alpha_vantage'])
    import alpha_vantage
    from alpha_vantage.timeseries import TimeSeries

    
####################################################################

#installing MongoDB
os.system('sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5')
os.system('echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list')
os.system('sudo apt-get update')
os.system('sudo apt-get install -y mongodb-org')
os.system('sudo service mongod start')

####################################################################

# Connection to the MongoDB program at specific URLs & Ports
# default is localhost:27017
connection = MongoClient('localhost:27017')

# Switching to a specific Database within MongoDB
db = connection.StockMarketDB

# Switching to a specific Collection(table) within the DB
mo = db.monthlyStatistics

####################################################################

# Personal issued key from alpha_vantage
ts = TimeSeries(key='II0VU3FTX7AAEU99')

# Calling an individual company's monthly stock data
data, meta_data  = ts.get_monthly(symbol='MSFT')

# Will display that data
#pprint(data)

parsed_data = {}

# formatting nested dictionary keys for mongoDB
for date, stock in data.iteritems():
    parsed_data[date] = {}
    for price in stock.iterkeys():
        parsed_data[date][price[3:]] = data[date][price]

# adding 'date' dictionary key as a value to
# nested dictionary, then inserting to MongoDB
for date, stock in parsed_data.iteritems():
    stock['date'] = date
    mo.insert_one(stock)

########################################
#            Data break down           #
########################################
# data/parsed_data                     #
# |                                    #
# -----------                          #
# |         |                          #
# date      stock                      #
#               |                      #
# ---------------------------------    #
# |     |      |     |    |       |    #
# open  close  high  low  volume  date #
########################################


###################################################################
# Looking at documents inside the collection
# results = mo.find()
# for documents in results:
#     pprint(documents)


# to delete all date in the collection
# mo.delete_many({})
