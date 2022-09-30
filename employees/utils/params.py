from xml.dom import EMPTY_NAMESPACE


db_params = {
    "user": "postgres",
    "password": "postgres",
    "db": "postgres",
    "host": "localhost",
    "port": 5432,
}

insert_employee = """
insert into employees (
emp_name ,
emp_pos_id ,
emp_salary ,
date_of_start ,
employed ) values (

%s,(select id from positions where work_pos = %s),%s,%s,(select id from activity_flag where employed = %s))
"""

unemploy ="""
UPDATE employees 
SET employed = 2
    
WHERE emp_name ='{emp_name}';

"""