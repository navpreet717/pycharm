import pymongo
import logging
try:
    myclient=pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient["navpreetAssignment"]
    print(mydb)
except:
    logging.basicConfig(filename='app.log',filemode='w',format='%(name)s-%(levelname)s-%(message)s')
    logging.error('error in db creation')
    logging.info('db created')
#update document
try:

    with myclient:
     mycol=mydb["Collection1"]
    myquery={"city":"brampton"}
    newvalue={"$set":{"city":"Love"}}
    x= mycol.update_one(myquery)
    print(x,"document updated")

except:
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s-%(levelname)s-%(message)s')
    logging.error('error in updation of document')
    logging.info('document updated')


