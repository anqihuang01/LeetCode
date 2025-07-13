import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    n = person['email'].value_counts()
    n = n[n>1]
    n = n.index
    return pd.DataFrame(n)