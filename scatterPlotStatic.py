import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [10, 15, 13, 17, 20, 25]

plt.scatter(x, y)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Static Scatter Plot")

plt.show()