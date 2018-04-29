# Carlos Montes 
# Charts code for the project of the module "Programming and scripting"

import csv
import numpy as np
import matplotlib.pyplot as plt

# array that stores data from the csv file
data = np.genfromtxt('data/iris.csv', delimiter = ',')

# variables per column
col1 = data[:,0]
col2 = data[:,1]
col3 = data[:,2]
col4 = data[:,3]

# variables per parameter and flower class
setSL = data[0:50,0] # it selects the first 50 measures from the first colum
setSW = data[0:50,1]
setPL = data[0:50,2]
setPW = data[0:50,3]

verSL = data[50:100,0] # it selects the second 50 measures from the first colum
verSW = data[50:100,1]
verPL = data[50:100,2]
verPW = data[50:100,3]

virSL = data[100:150,0] # it selects the third and last 50 measures from the first colum
virSW = data[100:150,1]
virPL = data[100:150,2]
virPW = data[100:150,3]

# sample and comparison between a box plot and a violin plot
plt.boxplot(col1)
plt.show()

plt.violinplot(col1)
plt.show()


# histogram subplot per column
plt.figure()
plt.subplot(1,4,1) # (1 single row, 4 columns, item 1)
plt.hist(col1, edgecolor='black')
plt.title('SEPAL LENGTH')
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.ylabel("# samples")
plt.xlabel("range (cm)")

plt.subplot(1,4,2) # item 2 of this single row
plt.hist(col2, edgecolor='black')
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.title('SEPAL WIDTH')

plt.subplot(1,4,3) # item 3
plt.hist(col3, edgecolor='black')
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.title('PETAL LENGTH')

plt.subplot(1,4,4) # fourth and last item
plt.hist(col4, edgecolor='black')
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.title('PETAL WIDTH')
plt.show()

# histograms subplots. For iris setosa row
plt.figure()
plt.subplot(3,4,1)
plt.hist(setSL, edgecolor='black')
plt.title('SEPAL LENGTH')
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.ylabel("setosa (# samples)")


plt.subplot(3,4,2)
plt.hist(setSW, edgecolor='black')
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.title('SEPAL WIDTH')

plt.subplot(3,4,3)
plt.hist(setPL, edgecolor='black')
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.title('PETAL LENGTH')

plt.subplot(3,4,4)
plt.hist(setPW, edgecolor='black')
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.title('PETAL WIDTH')

# versicolor row

plt.subplot(3,4,5)
plt.hist(verSL, edgecolor='black')
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.ylabel("versicolor (# samples)")


plt.subplot(3,4,6)
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.hist(verSW, edgecolor='black')

plt.subplot(3,4,7)
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.hist(verPL, edgecolor='black')

plt.subplot(3,4,8)
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.hist(verPW, edgecolor='black')

# virginica row
plt.subplot(3,4,9)
plt.hist(virSL, edgecolor='black')
plt.ylabel("virginica (# samples)")
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.xlabel("range (cm)")


plt.subplot(3,4,10)
plt.hist(virSW, edgecolor='black')
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.xlabel("range (cm)")


plt.subplot(3,4,11)
plt.hist(virPL, edgecolor='black')
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.xlabel("range (cm)")


plt.subplot(3,4,12)
plt.hist(virPW, edgecolor='black')
plt.xlabel("range (cm)")
plt.grid(color='g', linestyle=':', linewidth=0.4)
plt.show()

"""
A simple individual scatter plot is:

x = data[0:50,0]
y = data[0:50,1]

plt.scatter(x,y)
plt.show()

"""

# scatter plot to show the relation between sepal length and sepal width

# Adapted from https://pythonspot.com/matplotlib-scatterplot/

# Create data
g1 = (data[0:50,0], data[0:50,1])
g2 = (data[51:100,0], data[51:100,1])
g3 = (data[101:150,0],data[101:150,1])
 
data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("setosa", "versicolor", "virginica") 
 
# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor="w")
 
for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
 
plt.title('SEPAL')
plt.xlabel('length (cm)')
plt.ylabel('width (cm)')
plt.legend(loc=2)
plt.show()


# relation between petal length and petal width

"""
For some reason, getting two scatter plots like the previous one in a row leads to a 
TypeError (tuple indices must be integers or slices, not tuple)  g1 = (data[0:50,2], data[0:50,3])


# Create data
g1 = (data[0:50,2], data[0:50,3])
g2 = (data[51:100,2], data[51:100,3])
g3 = (data[101:150,2],data[101:150,3])
 
data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("setosa", "versicolor", "virginica") 
 
# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor="w")
 
for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
 
plt.title('PETAL')
plt.xlabel('length (cm)')
plt.ylabel('width (cm)')
plt.legend(loc=2)
plt.show()

"""