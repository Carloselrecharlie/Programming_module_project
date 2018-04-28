# Carlos Montes 
# Charts code for the project of the module "Programming and scripting"

import csv
import numpy as np
import matplotlib.pyplot as plt

# array that stores data from the csv file
data = np.genfromtxt('data/iris.csv', delimiter = ',')

col1 = data[:,0]
plt.violinplot(col1)
# plt.show()

col2 = data[:,1]
plt.hist(col2)
# plt.show()

col3 = data[:,2]
plt.hist(col3)
# plt.show()

col4 = data[:,3]
plt.hist(col4)
# plt.show()

#x = col1
#y = col2
plt.plot(col1,2)
plt.show()

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
For some reason, getting two scatter plots like this in a row leads to a 
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