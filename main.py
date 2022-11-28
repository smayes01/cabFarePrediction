import pandas as pd

CSV_PATH = 'data/sample.csv'

data_df = pd.read_csv(CSV_PATH).drop(labels=["Ehail_fee"],axis=1).drop(labels="Unnamed: 0",axis=1)

print(data_df)