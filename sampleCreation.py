import pandas as pd

CSV_PATH = 'data/data.csv'

sample_df = pd.read_csv(CSV_PATH).sample(frac=1).iloc[0:100000]
sample_df.index = range(0,100000)
print(sample_df)
sample_df.to_csv("data/sample.csv",index=False)
