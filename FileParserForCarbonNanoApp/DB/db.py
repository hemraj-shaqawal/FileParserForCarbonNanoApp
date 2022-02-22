import pymongo
import logging as logger
logger.basicConfig(filename="Log/appLog.log",level= logger.INFO,format="%(asctime)s %(levelname)s %(message)s")

class databaseOpr:

        def __init__(self):
                """Please Provide a path mongo DB"""
                self.client = pymongo.MongoClient("")
                self.db = self.client["NanotubeDB"]

        def batchInsertIntoCarbonColl(self,dataset):
                """This method will receive dataset and inset into Carbon collection"""
                try:
                        coll = self.db["carbon"]
                        res = coll.insert_many(dataset)
                        inserted_IDs = res.inserted_ids
                        logger.info(inserted_IDs)
                        return "File data has been inserted successfully!"
                except Exception as e:
                        logger.exception("Exception occur:" + str(e))

        def updateValue(self,updateValue):
                """This method will update a value based on filter"""
                try:
                        coll = self.db["carbon"]
                        filter = {"Chiral indice n":"3"}
                        newvalues = {"$set": {'Chiral indice n': str(updateValue)}}
                        res = coll.update_one(filter,newvalues)
                        logger.info(res)
                        return "data has been updated successfully!"
                except Exception as e:
                        logger.exception("Exception occur:" + str(e))


        def deleteInstance(self,filter):
                """This method will deleted a value based on filter"""
                try:
                        coll = self.db["carbon"]
                        filter = {"Chiral indice n":str(filter)}
                        res = coll.delete_one(filter)
                        logger.info(res)
                        return "data has been deleted successfully!"
                except Exception as e:
                        logger.exception("Exception occur:" + str(e))


        def findInstance(self,filter):
                """This method will find data based on filter
                return:list of result based on finding
                """
                try:
                        coll = self.db["carbon"]
                        res = coll.find(filter)
                        logger.info(res)
                        return res
                except Exception as e:
                        logger.exception("Exception occur:" + str(e))
