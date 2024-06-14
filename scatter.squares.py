import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c = y_values, cmap =plt.cm.Blues ,s =10)

#Set Chart Title and Label Axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel("Squares of values", fontsize=14)

#Set size of tick labels
ax.tick_params(axis="both", which="major", labelsize=4)

ax.axis([0, 1100, 0,110000])
#plt.savefig("squares_plot.png", bbox_inches = "tight") >>> to automatically save
plt.show()
