import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import date2num
from datetime import datetime, timedelta

# Define the project tasks and their durations
tasks = [
    {"Task": "Requirement Gathering", "Start": "2024-01-01", "End": "2024-01-15"},
    {"Task": "Design Phase", "Start": "2024-01-16", "End": "2024-01-31"},
    {"Task": "Frontend Development", "Start": "2024-02-01", "End": "2024-02-28"},
    {"Task": "Backend Development", "Start": "2024-02-15", "End": "2024-03-15"},
    {"Task": "Integration", "Start": "2024-03-16", "End": "2024-03-25"},
    {"Task": "Testing & QA", "Start": "2024-03-26", "End": "2024-03-31"},
    {"Task": "Deployment", "Start": "2024-04-01", "End": "2024-04-05"}
]

# Convert task data to a DataFrame
df = pd.DataFrame(tasks)

# Convert dates to datetime format
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])

# Create a Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))

# Add bars for each task
for index, row in df.iterrows():
    start_date = date2num(row['Start'])
    end_date = date2num(row['End'])
    duration = end_date - start_date
    ax.barh(row['Task'], duration, left=start_date, align='center')

# Format the x-axis to show dates
ax.set_xlabel("Timeline")
ax.set_ylabel("Tasks")
ax.xaxis_date()
ax.set_title("E-commerce System Development Gantt Chart")

# Add grid for better visualization
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the chart
plt.tight_layout()
plt.show()
