import pymongo
import logging
try:
    with myclient:
        print(mydb.Collection1.find())
except:
    logging.basicConfig(filename='app.log',filemode='w',format='%(name)s-%(levelname)s-%(message)s')
    logging.error('error in collections')
    logging.info('info')