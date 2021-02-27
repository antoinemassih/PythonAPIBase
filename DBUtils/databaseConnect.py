import pandas as pd
from DataTransformUtils.tradesData import TradesDF
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnect():

    def __init__(self):
        self.engine = create_engine('postgresql://postgres:monkeyxx@192.168.1.135:5432/postgres')
        self.database = self.engine.connect()
        self.Session = sessionmaker(bind=self.engine)
        s = self.Session()

    def writeToDB(self,data,table):
        data.to_sql(table, con=self.database, if_exists='replace', index=False)
        return true

    def getWriteSQL(self,data,table):
        return pd.io.sql.get_schema(data.reset_index(), table)

    def closeDB(self):
        self.database.close()