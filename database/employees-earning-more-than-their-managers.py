import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    join = pd.merge(employee,employee,left_on='managerId',right_on='id')
    join.rename({'name_x':'Employee'},axis=1,inplace=True)
    return pd.DataFrame(join['Employee'][join['salary_x']>join['salary_y']])    