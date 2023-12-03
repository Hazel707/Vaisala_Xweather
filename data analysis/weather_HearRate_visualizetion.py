import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("merged_data/2min_GIX5_merged_data.csv", parse_dates=['timestamp'])


fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15, 18))
fig.suptitle('Heart Rate vs. Weather Parameters')

# Relationship between heartbeat and temperature
axes[0].scatter(df['temperature'], df['heart_rate'], color='blue', edgecolor='black', alpha=0.5)
axes[0].set_title('Heart Rate vs. Temperature')
axes[0].set_xlabel('Temperature (°C)')
axes[0].set_ylabel('Heart Rate (bpm)')

# Relationship between heartbeat and humidity
axes[1].scatter(df['humidity'], df['heart_rate'], color='green', edgecolor='black', alpha=0.5)
axes[1].set_title('Heart Rate vs. Humidity')
axes[1].set_xlabel('Humidity (%)')
axes[1].set_ylabel('Heart Rate (bpm)')

# Relationship between heart rate and pressure
axes[2].scatter(df['pressure'], df['heart_rate'], color='red', edgecolor='black', alpha=0.5)
axes[2].set_title('Heart Rate vs. Pressure')
axes[2].set_xlabel('Pressure (hPa)')
axes[2].set_ylabel('Heart Rate (bpm)')

# Optimize layout and display graphics
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
