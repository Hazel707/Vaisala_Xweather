import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime


with open("firebase/converted_data_GIX6.json", "r") as json_file:
    json_data = pd.read_json(json_file).T  
    json_data['timestamp'] = pd.to_datetime(json_data['timestamp'])

# parse TCX files
tree = ET.parse('wearables/GIX6/merged_data.tcx')
root = tree.getroot()

# XML namespace
ns = {'ns0': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}

trackpoints = []
for trackpoint in root.findall(".//ns0:Trackpoint", namespaces=ns):
    time = trackpoint.find("ns0:Time", namespaces=ns).text
    heart_rate = trackpoint.find("ns0:HeartRateBpm/ns0:Value", namespaces=ns).text


    dt_obj = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f%z')
    formatted_time = dt_obj.strftime('%Y-%m-%d %H:%M:%S')


    trackpoints.append({
        'timestamp': formatted_time,
        'heart_rate': heart_rate
    })

tcx_data = pd.DataFrame(trackpoints)
tcx_data['timestamp'] = pd.to_datetime(tcx_data['timestamp'])

# Sort the timestamp column
json_data = json_data.sort_values('timestamp')
tcx_data = tcx_data.sort_values('timestamp')

# Merge data using a 2-minute time tolerance
merged_data = pd.merge_asof(json_data, tcx_data, on='timestamp', direction='nearest', tolerance=pd.Timedelta(minutes=2))

# Delete unmatched rows
merged_data = merged_data.dropna(subset=['heart_rate'])

# Save the merged data to a CSV file
merged_data.to_csv("merged_data/2min_GIX6_merged_data.csv", index=False)#---------------

print("Merged data saved to matched_data.csv")



# # 调整 TCX 时间戳
# tcx_data['adjusted_timestamp'] = tcx_data['timestamp'] + pd.Timedelta(hours=4.87)

# # 使用调整后的时间戳进行合并
# merged_data_adjusted = pd.merge_asof(json_data, tcx_data.sort_values('adjusted_timestamp'), left_on='timestamp', right_on='adjusted_timestamp', direction='nearest', tolerance=pd.Timedelta(minutes=5))

# # 删除未匹配的行
# merged_data_adjusted = merged_data_adjusted.dropna(subset=['heart_rate'])

# # 保存调整后的合并数据到CSV文件
# merged_data_adjusted.drop(columns=['adjusted_timestamp']).to_csv("merged_data/GIX6_adjusted_matched_data.csv", index=False)#---------------

# print("Adjusted merged data saved to adjusted_matched_data.csv")



# # Filter JSON data to only include the overlapping period
# overlap_json = json_data[(json_data['timestamp'] >= '2023-07-28') & (json_data['timestamp'] <= '2023-08-07')]

# # Filter TCX data to only include the overlapping period
# overlap_tcx = tcx_data[(tcx_data['timestamp'] >= '2023-07-28') & (tcx_data['timestamp'] <= '2023-08-07')]

# print(f"Number of rows in JSON during overlap: {len(overlap_json)}")
# print(f"Number of rows in TCX during overlap: {len(overlap_tcx)}")

# # 对于 JSON 中的每一个时间戳，找到 TCX 中的最近时间戳，并计算时间差
# time_diffs = []
# for timestamp in overlap_json['timestamp']:
#     closest_time = overlap_tcx['timestamp'].iloc[(overlap_tcx['timestamp'] - timestamp).abs().argsort()[:1]]
#     time_diff = (closest_time - timestamp).iloc[0].total_seconds()
#     time_diffs.append(time_diff)

# 打印平均时间差
#print(f"Average time difference: {sum(time_diffs) / len(time_diffs)} seconds")

# # Filter datasets for overlapping period
# json_overlap = json_data[(json_data['timestamp'] >= "2023-07-28 17:23:34") & (json_data['timestamp'] <= "2023-08-07 16:18:59")]
# tcx_overlap = tcx_data[(tcx_data['timestamp'] >= "2023-07-28 17:23:34") & (tcx_data['timestamp'] <= "2023-08-07 16:18:59")]

# # Print number of rows in the overlapping datasets
# print("Number of rows in JSON overlap:", len(json_overlap))
# print("Number of rows in TCX overlap:", len(tcx_overlap))

# # Attempt the merge on this overlapping period
# merged_overlap = pd.merge_asof(json_overlap, tcx_overlap, on='timestamp', direction='nearest', tolerance=pd.Timedelta(minutes=30))
# print("Number of rows in merged overlap:", len(merged_overlap))

# # Merging JSON and TCX data for overlapping period
# merged_overlap = pd.merge_asof(json_overlap, tcx_overlap, on='timestamp', direction='nearest', tolerance=pd.Timedelta(minutes=30))

# # Calculate time differences between JSON and TCX timestamps
# merged_overlap['time_difference'] = (merged_overlap['timestamp'] - merged_overlap['timestamp']).abs()

# # Print average time difference
# print("Average time difference:", merged_overlap['time_difference'].mean())


# sample_timestamp = json_data.iloc[60]['timestamp']
# closest_timestamps = tcx_data[(tcx_data['timestamp'] > (sample_timestamp - pd.Timedelta(minutes=30))) & (tcx_data['timestamp'] < (sample_timestamp + pd.Timedelta(minutes=30)))]
# print("Sample Timestamp from JSON:", sample_timestamp)
# print("\nClosest Timestamps from TCX:\n", closest_timestamps)



# print("JSON Timestamp Range:", json_data['timestamp'].min(), "-", json_data['timestamp'].max())
# print("TCX Timestamp Range:", tcx_data['timestamp'].min(), "-", tcx_data['timestamp'].max())

# print("Number of rows in JSON:", len(json_data))
# print("Number of rows in TCX:", len(tcx_data))


