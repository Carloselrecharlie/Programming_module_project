# Carlos Montes code for the project of the module "Programming and scripting"

import csv
import numpy
import matplotlib.pyplot as mpl



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