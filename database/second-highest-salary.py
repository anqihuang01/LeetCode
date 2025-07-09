import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(['salary']).sort_values(['salary'],ascending=False)
    if len(employee['salary'])<2:
        return pd.DataFrame({'SecondHighestSalary':[np.NaN]})
    
    #employee.rename({'salary':'SecondHighestSalary'},axis=1,inplace=True)
    #employee.drop(['id'],axis=1,inplace=True)
    return pd.DataFrame({'SecondHighestSalary':[employee.iloc[1,1]]})
                