import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [10, 15, 13, 17, 20]

x2 = [1, 2, 3, 4, 5]
y2 = [5, 7, 9, 11, 13]

plt.subplot(1, 2, 1)
plt.scatter(x1, y1)
plt.title("Scatter Plot 1")
plt.xlabel("X1")
plt.ylabel("Y1")

plt.subplot(1, 2, 2)
plt.scatter(x2, y2)
plt.title("Scatter Plot 2")
plt.xlabel("X2")
plt.ylabel("Y2")

plt.tight_layout()
plt.show()
