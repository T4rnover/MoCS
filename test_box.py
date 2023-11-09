# Calculate the fractal dimension using the box-counting method
box_sizes = np.arange(1, size // 2, 1)
num_boxes = []

# Loop through different box sizes and count the number of occupied boxes
for box_size in box_sizes:
    num_boxes.append(np.sum(grid[::box_size, ::box_size]))

# Plot the results on a log-log plot
plt.loglog(box_sizes, num_boxes)
plt.title('Fractal Dimension of DLA Structure')
plt.xlabel('Box Size')
plt.ylabel('Number of Boxes')
plt.show()