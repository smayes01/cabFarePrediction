import pandas as pd
import time 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

CSV_PATH = 'data/sample.csv'

data_df = pd.read_csv(CSV_PATH)
data_df = data_df.drop(labels=['vendorid','Ehail_fee', 'MTA_tax', 'Improvement_surcharge', 
                               'Total_amount', "Extra", "Tip_amount"],
                       axis=1)


# print('before: ',data_df.shape)

# we exclude instances that don't make sense
data_df = data_df.loc[data_df.Trip_type.notna()] # exclude where trip_type is null
data_df = data_df.loc[data_df.Passenger_count >= 0] # exclude where passangers is less than 1
data_df = data_df.loc[data_df.Fare_amount > 0] # Fare_amount has to be higher than zero
data_df = data_df.loc[data_df.Pickup_longitude != 0]
data_df = data_df.loc[data_df.Pickup_latitude != 0]
data_df = data_df.loc[data_df.Dropoff_longitude != 0]
data_df = data_df.loc[data_df.Dropoff_longitude != 0]
data_df = data_df.loc[data_df.rate_code != 99]

# convert dates to ordinal
data_df['pickup_datetime'] = pd.to_datetime(data_df['pickup_datetime'])
data_df['pickup_datetime']=data_df['pickup_datetime'].apply(lambda x: time.mktime(x.timetuple()))
data_df['dropoff_datetime'] = pd.to_datetime(data_df['dropoff_datetime'])
data_df['dropoff_datetime']=data_df['dropoff_datetime'].apply(lambda x: time.mktime(x.timetuple()))

# convert nominal to binary
data_df = pd.concat([data_df,pd.get_dummies(data_df['Store_and_fwd_flag'], prefix='Store_and_fwd_flag')],axis=1) 
data_df = pd.concat([data_df,pd.get_dummies(data_df['rate_code'], prefix='rate_code')],axis=1) 
data_df = pd.concat([data_df,pd.get_dummies(data_df['Payment_type'], prefix='Payment_type')],axis=1) 
data_df = pd.concat([data_df,pd.get_dummies(data_df['Trip_type'], prefix='Trip_type')],axis=1) 
data_df = data_df.drop(['Store_and_fwd_flag','rate_code','Payment_type','Trip_type'], axis=1)
print(data_df)

# # We separate X and Y
# X = data_df.drop('Fare_amount', axis=1)
# y = data_df.Fare_amount

