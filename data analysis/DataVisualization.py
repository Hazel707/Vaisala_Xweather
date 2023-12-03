import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read data and parse timestamps
df = pd.read_csv("merged_data/2min_GIX5_merged_data.csv", parse_dates=['timestamp'])

# Set size and title
fig, ax1 = plt.subplots(figsize=(15, 6))
fig.suptitle('Data Visualization Over Time')

# Set up dual axes
ax2 = ax1.twinx()

# plot temperature, humidity and pressure data
line1, = ax1.plot(df['timestamp'], df['temperature'], 'b-', label='Temperature (°C)')
line2, = ax1.plot(df['timestamp'], df['humidity'], 'g-', label='Humidity (%)')
line3, = ax1.plot(df['timestamp'], df['pressure'], 'r-', label='Pressure (hPa)')

# Plot Heart Rate data
line4, = ax2.plot(df['timestamp'], df['heart_rate'], 'orange', label='Heart Rate (bpm)')

# Set the Y-axis label
ax1.set_ylabel('Temperature, Humidity, Pressure')
ax2.set_ylabel('Heart Rate (bpm)')

# Set up X-axis labels and time formats
ax1.set_xlabel('Time')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H'))

# Add Legend
lines = [line1, line2, line3, line4]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc=0)


plt.tight_layout()
plt.show()
