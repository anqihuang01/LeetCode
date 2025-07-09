import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    Scores['rank'] = Scores['score'].rank(method ='dense',ascending=False)
    return Scores[['score','rank']].sort_values('score',ascending=False)    