import pandas as pd


def fill_missing_coordinates(df):
#  This function fills missing 'latitude' and 'longitude' values in a DataFrame.
#  It checks each row, and if either 'latitude' or 'longitude' is missing, it looks for
#  a row with the same 'city' that has valid coordinates and fills in the missing values. 
  for index, row in df.iterrows():
    if pd.isna(row['latitude']) or pd.isna(row['longitude']):
      city = row['city']
      valid_coordinates = df[(df['city'] == city) & (~df['latitude'].isna()) & (~df['longitude'].isna())]
      if not valid_coordinates.empty:
        valid_row = valid_coordinates.iloc[0]  
        df.at[index, 'latitude'] = valid_row['latitude']
        df.at[index, 'longitude'] = valid_row['longitude'] 