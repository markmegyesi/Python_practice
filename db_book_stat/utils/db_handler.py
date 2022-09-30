import psycopg2 as sql

def get_connection(connection_params):
    return sql.connect(user = connection_params['user'],
                        password = connection_params['password'],
                        database = connection_params['db'],
                        host = connection_params['host'],
                        port = connection_params['port'],
                      )

def run_sql(connection_params,sql_script,data=None):
    with get_connection(connection_params) as conn:
        with conn.cursor() as cur:
            try:
                if data :
                    cur.execute(sql_script,data)
                else:
                    cur.execute(sql_script)
            except Exception as e:
                conn.rollback()
                print(e)
            conn.commit()


if __name__=='__main__':
    from params import book_stat_insert, db_params

    run_sql(db_params,book_stat_insert,('teszt', 1, 'teszt',1,1,'teszt','teszt'))
                