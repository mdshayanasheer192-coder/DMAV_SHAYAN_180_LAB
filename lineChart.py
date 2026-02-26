import matplotlib.pyplot as plt
import numpy as np

x_points = ([1,2,6,8])
y_points = ([3,5,7,9])

plt.plot(x_points,y_points,marker='o')

plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.title("Line Chart")
plt.show()