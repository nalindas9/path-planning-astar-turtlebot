import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Plotting the final map

fig = plt.figure()
plt.axes()
plt.xlim(0, 100)
plt.ylim(0, 100)
circle1 = plt.Circle((30, 20), radius=10, fill=False)
circle2 = plt.Circle((70, 20), radius=10, fill=False)
circle3 = plt.Circle((50, 50), radius=10, fill=False)
circle4 = plt.Circle((70, 80), radius=10, fill=False)
square1 = plt.Rectangle((22.5, 72.5), width=15, height=15, fill=False)
square2 = plt.Rectangle((2.5, 42.5), width=15, height=15, fill=False)
square3 = plt.Rectangle((82.5, 42.5), width=15, height=15, fill=False)

plt.gca().add_patch(circle1)
plt.gca().add_patch(circle2)
plt.gca().add_patch(circle3)
plt.gca().add_patch(circle4)
plt.gca().add_patch(square1)
plt.gca().add_patch(square2)
plt.gca().add_patch(square3)
plt.axis("scaled")


plt.grid(color='lightgray',linestyle='--')
plt.show()
