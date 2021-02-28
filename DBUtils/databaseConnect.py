import pandas as pd
from DataTransformUtils.tradesData import ET_Transactions
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


class DBConnect():

    def __init__(self,databaseToLoad,tablesToLoad):
        self.engine = db.create_engine('postgresql://postgres:monkeyxx@192.168.1.135:5432/'+databaseToLoad)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.Session = sessionmaker(bind=self.engine)
        self.tables = {}
        for table in tablesToLoad:
            self.tables[table] = db.Table(table, self.metadata, autoload=True, autoload_with=self.engine)

    def writeToDB(self, data, table):
        data.to_sql(table, con=self.connection, if_exists='replace', index=False)
        return True

    def readDB(self, table):
        query = db.select([self.tables[table]])
        return self.connection.execute(query)

    def readDBasDataFrane(self, table):
        query = db.select([self.tables[table]])
        cols = self.metadata.tables[table].columns.keys()
        return pd.DataFrame(self.connection.execute(query).fetchall(),columns=cols)

    def getWriteSQL(self, data, table):
        return pd.io.sql.get_schema(data.reset_index(), table)

    def closeDB(self):
        self.connection.close()
