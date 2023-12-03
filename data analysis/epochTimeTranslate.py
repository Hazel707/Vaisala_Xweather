import json
from datetime import datetime

import os
print(os.getcwd())

# def convert_timestamp(data):
#     for key, value in data.items():
#         if "timestamp" in value:
#             epoch_time = int(value["timestamp"])
#             human_readable_time = datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
#             value["timestamp"] = human_readable_time
#     return data
# def convert_timestamp(data):
#     for user_key, user_data in data.items():
#         readings = user_data.get("readings", {})
#         for reading_key, reading_data in readings.items():
#             if "timestamp" in reading_data:
#                 epoch_time = int(reading_data["timestamp"])
#                 human_readable_time = datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
#                 reading_data["timestamp"] = human_readable_time
#     return data
def convert_timestamp(readings_data):
    for key, value in readings_data.items():
        if "timestamp" in value:
            epoch_time = int(value["timestamp"])
            human_readable_time = datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
            value["timestamp"] = human_readable_time
    return readings_data



with open('/Users/hazel/Desktop/23fall/540/data/firebase/GIX8.json', 'r') as file:
    data = json.load(file)

# Convert timestamps
converted_data = convert_timestamp(data["readings"])
# for key, value in list(converted_data.items())[:10]:  #  Print the first 10 entries
#     print(key, value)

with open('/Users/hazel/Desktop/23fall/540/data/firebase/converted_data_GIX8.json', 'w') as file:
    json.dump(converted_data, file, indent=4)
