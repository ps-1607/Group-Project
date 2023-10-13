import pandas as pd
from math import sqrt

def dms_to_dd(full_coordinate):
  if full_coordinate[0] == '-':
    multiplier = -1
  else:
    multiplier = 1
  degrees_minutes_seconds = full_coordinate[1:]
  degrees, minutes, seconds = degrees_minutes_seconds.split(':')
  dd = int(degrees) + int(minutes)/60 + float(seconds)/3600
  dd = dd * multiplier 
  return dd


def prog():
  mon_lat = 44.3375 
  mon_lon = 11.7082
  df = pd.read_csv("coords.txt")
  current_best = 100000
  best_staid = -1
  print(df.head())
  for index, row in df.iterrows():
    current_lat = dms_to_dd(row['      LAT'])
    current_lon = dms_to_dd(row['       LON'])
    lat_dist = current_lat - mon_lat 
    lon_dist = current_lon - mon_lon
    if (current_best > sqrt(lat_dist ** 2 + lon_dist ** 2)):
      best_staid = row['STAID']
      current_best = sqrt(lat_dist ** 2 + lon_dist ** 2)
    #print(dms_to_dd(row['      LAT']))
    #print("LAT: ", row['      LAT'])
    #print("LON: ", row['       LON'])
  print(best_staid)
  print(current_best)

if __name__ == "__main__":
  prog()
