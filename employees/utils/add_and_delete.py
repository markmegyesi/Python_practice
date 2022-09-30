from db_handling import RunSql
from params import insert_employee, unemploy

class AddAndDelete(RunSql):
    def __init__(self):
        super().__init__()

    def add(self,emp_dict):
        employee = [item for item in emp_dict.values() ]
        
        self.run_sql(insert_employee,employee)

    def delete(self,emp_dict):
        
        self.run_sql(unemploy.format(emp_name = emp_dict['name']))


    


if __name__ == '__main__':

    test_dict = {
        'name': 'Sam Winchester',
        'position': 'Developer',
        'salary' : 8000,
        'date_of_start' : '2022.07.24',
        'employed' : 'Yes'
    }

    # add= AddAndDelete()
    # add.add(test_dict)

    delete = AddAndDelete()
    delete.delete(test_dict)
