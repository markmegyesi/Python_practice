import psycopg2 as sql
from params import db_params, insert_employee, unemploy

class Db_Connect:
    def __init__(self):
        
        self.conn = sql.connect(user = db_params['user'],
                        password = db_params['password'],
                        database = db_params['db'],
                        host = db_params['host'],
                        port = db_params['port'],
                      ) 
        self.cur = self.conn.cursor()

class RunSql(Db_Connect):
    def __init__(self):
        super().__init__()
        

    def run_sql(self, sql_script, data=None):
        cur = self.cur
        conn = self.conn
        try:
            if data :
                cur.execute(sql_script,data)
            else:
                cur.execute(sql_script)
        except Exception as e:
            conn.rollback()
            print(e)
        conn.commit()



if __name__ == '__main__':

    from params import insert_employee, unemploy,db_params

    run_sql = RunSql()
    # employee = ['Dean Winchester', 2, 8000,'2022.07.23',1]
    # run_sql.run_sql(insert_employee,employee)
    employee='Dean Winchester'
    
    run_sql.run_sql(unemploy.format(emp_name=employee))