import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(['salary']).sort_values('salary',ascending=False)
    employee.drop(['id'],axis=1,inplace=True)

    if len(employee['salary']) < N or N<1:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})

    employee.rename({'salary':f'getNthHighestSalary({N})'},axis=1,inplace=True)
    return employee.head(N).tail(1)