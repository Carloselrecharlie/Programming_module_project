# Carlos Montes code for the project of the module "Programming and scripting"

import csv
import numpy
import matplotlib.pyplot as mpl

print()
print('sep_len  sep_wid  pet_len  pet_wid (cm)')
print()


with open('data/iris.csv', newline='') as csvFile:

  for line in csvFile:

    line = line.replace(',', ' ') #removes comma separating the numbers

    a = float (line.split()[0]) #converts strings into values
    b = float (line.split()[1])
    c = float (line.split()[2])
    d = float (line.split()[3])

    print('  ' + line[:3]+ '      ' + line[4:7]+ '      ' + line[8:11]+ '      ' + line[12:15])

data = numpy.genfromtxt('data/iris.csv', delimiter = ',')

meancol1 = numpy.mean(data[:,0])
meancol2 = numpy.mean(data[:,1])
meancol3 = numpy.mean(data[:,2])
meancol4 = numpy.mean(data[:,3])

print('sep_len  sep_wid  pet_len  pet_wid (cm)')
print()
print("AVERAGES (cm)")
print('  '+ '{0:.2f}'.format(meancol1) + "     " + '{0:.2f}'.format(meancol2) + "     " + '{0:.2f}'.format(meancol3) + "     " + '{0:.2f}'.format(meancol4))

col1 = data[:,0]
mpl.hist(col1)
# mpl.show()

col2 = data[:,1]
mpl.hist(col2)
# mpl.show()

col3 = data[:,2]
mpl.hist(col3)
# mpl.show()

col4 = data[:,3]
mpl.hist(col4)
# mpl.show()

# means by flower class: sepal length
meanSetSL= numpy.mean(data[0:50,0])
meanVerSL= numpy.mean(data[51:100,0])
meanVirSL= numpy.mean(data[101:150,0])
# means sepal width
meanSetSW= numpy.mean(data[0:50,1])
meanVerSW= numpy.mean(data[51:100,1])
meanVirSW= numpy.mean(data[101:150,1])
# means petal length
meanSetPL= numpy.mean(data[0:50,2])
meanVerPL= numpy.mean(data[51:100,2])
meanVirPL= numpy.mean(data[101:150,2])
# means petal width
meanSetPW= numpy.mean(data[0:50,3])
meanVerPW= numpy.mean(data[51:100,3])
meanVirPW= numpy.mean(data[101:150,3])

print()
print('AVERAGES by flower class (cm)')
print('Iris Setosa')
print('  '+ '{0:.2f}'.format(meanSetSL) + "     " + '{0:.2f}'.format(meanSetSW) + "     " + '{0:.2f}'.format(meanSetPL) + "     " + '{0:.2f}'.format(meanSetPW))
print('Iris Versicolor')
print('  '+ '{0:.2f}'.format(meanVerSL) + "     " + '{0:.2f}'.format(meanVerSW) + "     " + '{0:.2f}'.format(meanVerPL) + "     " + '{0:.2f}'.format(meanVerPW))
print('Iris Virginica')
print('  '+ '{0:.2f}'.format(meanVirSL) + "     " + '{0:.2f}'.format(meanVirSW) + "     " + '{0:.2f}'.format(meanVirPL) + "     " + '{0:.2f}'.format(meanVirPW))
print()

# medians by flower class: sepal length
medianSetSL= numpy.median(data[0:50,0])
medianVerSL= numpy.median(data[51:100,0])
medianVirSL= numpy.median(data[101:150,0])
# medians sepal width
medianSetSW= numpy.median(data[0:50,1])
medianVerSW= numpy.median(data[51:100,1])
medianVirSW= numpy.median(data[101:150,1])
# medians petal length
medianSetPL= numpy.median(data[0:50,2])
medianVerPL= numpy.median(data[51:100,2])
medianVirPL= numpy.median(data[101:150,2])
# medians petal width
medianSetPW= numpy.median(data[0:50,3])
medianVerPW= numpy.median(data[51:100,3])
medianVirPW= numpy.median(data[101:150,3])

print()
print('MEDIANS by flower class (cm)')
print('Iris Setosa')
print("  ", medianSetSL, "     ", medianSetSW, "     ", medianSetPL, "     ", medianSetPW)
print('Iris Versicolor')
print("  ", medianVerSL, "     ", medianVerSW, "     ", medianVerPL, "     ", medianVerPW)
print('Iris Virginica')
print("  ", medianVirSL, "     ", medianVirSW, "     ", medianVirPL, "     ", medianVirPW)
print()