import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [2, 1, 6, 15, 10]

plt.plot(x, y, marker='o', linestyle='-', color='blue')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple X-Y Plot")

plt.grid(True)

plt.show()