import matplotlib.pyplot as plt
import numpy as np

# Sample data
speed = np.arange(5, 37, 0.5)
response_time = [
2500, 2450, 2430, 2300, 2360, 2380, 2390, 2400, 2260, 2240, 2200, 2100, 2140, 2060,
2000, 1950, 1900, 1840, 1800, 1760, 1730, 1700, 1630, 1600, 1540, 1520, 1500, 1490, 1480,
1450, 1400, 1370, 1350, 1330, 1300, 1280 ,1250, 1240, 1200, 1190, 1170, 1140, 1100, 1070, 1040, 1010,
1000, 950, 900, 880, 850, 800, 780, 750, 730, 700, 680, 650, 630, 600,
580, 570, 550, 530 ]
sadfxc
# Plot the line graph
plt.plot(speed, response_time, linestyle='-')

# Set labels for x and y axes
plt.xlabel('Network Speed (Mbps)')
plt.ylabel('Response Time (ms)')

# Set title for the graph
plt.title('Network Speed vs Response Time Graph')

# Display grid lines
plt.grid(True)

# Set x-axis ticks with smaller intervals
plt.xticks(np.arange(5, 37, 1))  # Adjust the interval as needed

# Display the graph
plt.show()
