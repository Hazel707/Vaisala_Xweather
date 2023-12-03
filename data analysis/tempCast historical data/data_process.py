import pandas as pd
import matplotlib.pyplot as plt

station_names = {
    14635: "UW Ranier Vista",
    14636: "UW College of Environment",
    14637:  "UW Red Square / By George",
    14638: "UW Tower South Plaza"
}

data=pd.read_csv('obs_data_GIX_Jul-Aug-2023.csv')
print(data.head())

data['station_id']=data['station_id'].map(station_names)
data['available_time'] = pd.to_datetime(data['available_time'])
data['valid_time'] = pd.to_datetime(data['valid_time'])

# print(data.describe())

# for station_id in data['station_id'].unique():
#     station_data = data[data['station_id'] == station_id]
#     print(f"Data for Station {station_id}")
#     print(station_data.describe())


for station_names in data['station_id'].unique():
    station_data=data[data['station_id']==station_names]
    plt.plot(station_data['valid_time'], station_data['air_temperature'], label=f"Station {station_names}")

plt.xlabel('Time')
plt.ylabel('Air Temperature')
plt.title('Air Temperature Trends by Station')
plt.legend()
plt.show()