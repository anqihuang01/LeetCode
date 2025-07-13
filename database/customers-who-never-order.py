import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    join = pd.merge(customers,orders,
                    left_on = 'id',right_on = 'customerId',
                    how = 'left')
    join.rename(columns={'name':'Customers'},inplace=True)
    return join[['Customers']][join['customerId'].isnull()]
