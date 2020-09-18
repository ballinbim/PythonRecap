import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20,100)
plt.plot(x, np.sin(x))

plt.show()

print("HELLO WORLD")

# virtualenv -p python3 <desired-path> #Create Virtual Environment
# pip3 install matplotlib