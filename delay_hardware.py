import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.interpolate import make_interp_spline

# Sample data
speed = np.arange(5, 37, 0.5)

# Generate response times in descending order from 1000 to 500
response_time = [
1500, 940, 804, 1403, 930, 1302, 840, 665, 740, 740, 549, 610, 640, 620,
860, 540, 1203, 843, 1230, 320, 340, 230, 1203, 320, 320, 540, 430, 430, 850,
540, 1202, 403, 230, 420, 230, 320 ,430, 1304, 540, 605, 430, 705, 750, 405, 650, 403,
960, 430, 900, 880, 850, 800, 780, 750, 730, 700, 680, 650, 630, 600,
580, 240, 550, 230 ]
response_time.sort(reverse=True)

# Plot the line graph
plt.plot(speed, response_time, linestyle='-')

# Set labels for x and y axes
plt.xlabel('Network Speed (Mbps)')
plt.ylabel('Response Time (ms)')

# Set title for the graph
plt.title('The Response Time of Device Receive Signal From IOT Server with Network Speed')

# Display grid lines
plt.grid(True)

# Set x-axis ticks with smaller intervals
plt.xticks(np.arange(5, 37, 1))  # Adjust the interval as needed

# Display the graph
plt.show()

