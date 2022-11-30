import pandas as pd

CSV_PATH = 'data/data.csv'

sample_df = pd.read_csv(CSV_PATH)
# we exclude instances that don't make sense
sample_df = sample_df.loc[sample_df.Trip_type.notna()] # exclude where trip_type is null
sample_df = sample_df.loc[sample_df.Passenger_count >= 0] # exclude where passangers is less than 1
sample_df = sample_df.loc[sample_df.Fare_amount > 0] # Fare_amount has to be higher than zero
sample_df = sample_df.loc[sample_df.Pickup_longitude != 0]
sample_df = sample_df.loc[sample_df.Pickup_latitude != 0]
sample_df = sample_df.loc[sample_df.Dropoff_longitude != 0]
sample_df = sample_df.loc[sample_df.Dropoff_longitude != 0]
sample_df = sample_df.loc[sample_df.rate_code != 99]


sample_df = sample_df.sample(frac=1).iloc[0:100000]
print(sample_df.shape)

print(sample_df)
sample_df.to_csv("data/sample.csv",index=False)
