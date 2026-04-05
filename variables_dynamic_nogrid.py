import matplotlib.pyplot as plt


n = int(input("Enter number of data points: "))

x = []
y = []


for i in range(n):
    x_val = float(input(f"Enter X value {i+1}: "))
    y_val = float(input(f"Enter Y value {i+1}: "))
    
    x.append(x_val)
    y.append(y_val)


plt.plot(x, y, marker='o', linestyle='-', color='green')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Dynamic X-Y Plot")
plt.grid(False)

plt.show()