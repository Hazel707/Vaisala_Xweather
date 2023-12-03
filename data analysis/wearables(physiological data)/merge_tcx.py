import os
import xml.etree.ElementTree as ET

def merge_tcx_files(directory):
    # Create a new XML tree to store the merged data
    root = ET.Element("TrainingCenterDatabase", xmlns="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2")
    activities = ET.SubElement(root, "Activities")

    # Iterate through all TCX files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".tcx"):
            tree = ET.parse(os.path.join(directory, filename))
            for activity in tree.findall(".//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Activity"):
                # 检查 <Activity> 元素是否包含有用的信息
                if activity.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Lap") is not None:
                    activities.append(activity)

    # Save the merged data to a new TCX file
    merged_tree = ET.ElementTree(root)
    merged_tree.write(os.path.join(directory, "merged_data.tcx"), encoding="UTF-8", xml_declaration=True)

# Merge all TCX files in the same directory
merge_tcx_files("/Users/hazel/Desktop/23fall/540/data/wearables/GIX7")
