import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.random.randn(100)

# Create a dashboard layout with plt.subplots()
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
fig.suptitle("Matplotlib Dashboard Example", fontsize=16)

# Plot 1: Sine wave
axes[0, 0].plot(x, y1, color='blue')
axes[0, 0].set_title("Sine Wave")

# Plot 2: Cosine wave
axes[0, 1].plot(x, y2, color='red')
axes[0, 1].set_title("Cosine Wave")

# Plot 3: Scatter plot
axes[1, 0].scatter(x, y3, color='green')
axes[1, 0].set_title("Random Scatter")

# Hide empty subplot
axes[1, 1].axis('off')
axes[1, 1].text(0.5, 0.5, "Dashboard Layout", ha='center')

plt.tight_layout()
plt.savefig("dashboard_example.png")  # Save the figure
plt.show()
