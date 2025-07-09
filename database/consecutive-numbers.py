import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['rank']=logs.groupby('num').cumcount()+1
    logs['diff']=logs['id']-logs['rank']
    consecutive_counts=logs.groupby(['num','diff']).size()
    valid_nums = consecutive_counts[consecutive_counts >= 3].index.get_level_values('num')
    return pd.DataFrame({'ConsecutiveNums':valid_nums.unique()})    