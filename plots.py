# Carlos Montes 
# Charts code for the project of the module "Programming and scripting"

import csv
import numpy
import matplotlib.pyplot as mpl

# array that stores data from the csv file
data = numpy.genfromtxt('data/iris.csv', delimiter = ',')

col1 = data[0:50,0]
mpl.violinplot(col1)
mpl.show()

col2 = data[:,1]
mpl.hist(col2)
# mpl.show()

col3 = data[:,2]
mpl.hist(col3)
# mpl.show()

col4 = data[:,3]
mpl.hist(col4)
# mpl.show()