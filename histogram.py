import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data,bins=25,color='skyblue',edgecolor='black')
plt.title("fREQUENCY dISTRIBUTION")
plt.xlabel("Value Range")
plt.ylabel("Frequency (count")
plt.show()