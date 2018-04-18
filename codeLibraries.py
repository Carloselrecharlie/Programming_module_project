# Carlos Montes code for the project of the module "Programming and scripting"

import csv
import numpy



with open('data/iris.csv', newline='') as csvFile:

  for line in csvFile:

    line = line.replace(',', ' ') #removes comma separating the numbers

    a = float (line.split()[0]) #converts strings into values
    b = float (line.split()[1])
    c = float (line.split()[2])
    d = float (line.split()[3])

    print(line[:3]+ '      ' + line[4:7]+ '      ' + line[8:11]+ '      ' + line[12:15])

data = numpy.genfromtxt('data/iris.csv', delimiter = ',')

meancol1 = numpy.mean(data[:,0])
meancol2 = numpy.mean(data[:,1])
meancol3 = numpy.mean(data[:,2])
meancol4 = numpy.mean(data[:,3])

# print("Averages")
# print('{0:.2f}'.format(meancol1), +'   '+ {0:.2f}'.format(meancol2), '{0:.2f}'.format(meancol3), '{0:.2f}'.format(meancol4))

print("Average of the sepal length is: ", '{0:.2f}'.format(meancol1))
print("Average of the sepal width is: ", '{0:.2f}'.format(meancol2))
print("Average of the petal length is: ", '{0:.2f}'.format(meancol3))
print("Average of the petal length is: ", '{0:.2f}'.format(meancol4))