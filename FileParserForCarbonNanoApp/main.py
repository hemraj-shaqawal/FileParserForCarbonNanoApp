from Controller.controller import controller
from DB.db import databaseOpr
import logging as logger
logger.basicConfig(filename="Log/appLog.log",level= logger.INFO,format="%(asctime)s %(levelname)s %(message)s")

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        """Note: 
        press 1 for insert data
        press 2 for update data
        press 3 for delete data
        press 4 for find data
        press 5 for exit
        """
        logger.info("Note: press 1 for insert data. press 2 for update data. press 3 for delete data. press 4 for find data. press 5 for exit")

        app = controller("dataset\carbon_nanotubes.csv")

        while True:
            inp = eval(input("press 1 for insert data. press 2 for update data. press 3 for delete data. press 4 for find data. press 5 for exit => "))
            if(type(inp) == int and inp == 1):
                """This is option for bulk insert"""
                getDataSet = app.fileParser()
                app.insertDataFromFile(getDataSet)
                break
            elif(type(inp) == int and inp == 2):
                """This is option for update data"""
                app.updatevalue(30)
                break
            elif (type(inp) == int and inp == 3):
                """This is option for delete data"""
                app.deleteData(30)
                break
            elif (type(inp) == int and inp == 4):
                """This is option for find data"""
                res = app.findData("Initial atomic coordinate u", "0,591598")
                for item in enumerate(res):
                    logger.info(item)
                break
            elif (type(inp) == int and inp == 5):
                """This is option for exit"""
                break
            else :
                logger.info("Please enter a valid input!")

    except Exception as e:
        logger.exception("Exception occur:"+str(e))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
