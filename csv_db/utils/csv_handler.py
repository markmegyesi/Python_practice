import os
import pandas as pd
from sqlalchemy import create_engine


from config import CSV_URI, DB_URI

class CsvToSql:
    def __init__(self,db_uri, csv_uri):
        self.engine = create_engine(db_uri)
        for i in os.listdir(csv_uri):
            df = pd.read_csv(os.path.join(csv_uri,i))
            df.to_sql(name=i[:-4], con= self.engine, if_exists='append')

if __name__ == '__main__':
    from config import CSV_URI, DB_URI

    test = CsvToSql(DB_URI,CSV_URI)
