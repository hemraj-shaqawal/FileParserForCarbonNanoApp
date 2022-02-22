import os
import logging as logger
import csv
from DB.db import databaseOpr

Logger = logger.basicConfig(filename="Log/appLog.log",level= logger.INFO,format="%(asctime)s %(levelname)s %(message)s")

class controller:

    def __init__(self,path):
        try:
            if os.path.exists(path):
                self.path = path
            else:
                raise Exception("Please provide valid file path")
        except Exception as e:
            logger.exception("Exception occur:"+str(e))


    def fileParser(self):
        """file parser, it will read a file and a make Dict, and it's list of it."""
        try:
            finalList = []
            with open(self.path) as f:
                 reader = csv.reader(f,delimiter=";")
                 input_file = csv.DictReader(f,delimiter=";")
                 for key,row in  enumerate(input_file):
                    distObj = dict()
                    for key1,item in enumerate(row.items()):
                        distObj[item[0]] = item[1]
                    if distObj.items():
                        finalList.append(distObj)

            return finalList
        except Exception as e:
            logger.exception("Exception occur:"+str(e))

    def insertDataFromFile(self,dataset):
        """Bulk insertion from file dataset"""
        opr = databaseOpr()
        msg = opr.batchInsertIntoCarbonColl(dataset)
        logger.info(msg)

    def updatevalue(self,updateVal):
        """This method will update a value based on filter"""
        opr = databaseOpr()
        msg = opr.updateValue(updateVal)
        logger.info(msg)

    def deleteData(self,filter):
        """This method will deleted a value based on filter"""
        opr = databaseOpr()
        msg = opr.deleteInstance(filter)
        logger.info(msg)

    def findData(self,key,val):
        """This method will find data based on filter
        return:list of result based on finding
        """

        filter = {key:val}
        logger.info(filter)
        opr = databaseOpr()
        res = opr.findInstance(filter)
        return res

