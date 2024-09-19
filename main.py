import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='sin(x)')
plt.title('Scatter Plot of sin(x)', fontsize=16)
plt.xlabel('x values', fontsize=12)
plt.ylabel('sin(x)', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()