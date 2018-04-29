
# Carlos Montés Parra
# Own code to calculate the mean

import csv


with open('data/iris.csv', newline='') as csvFile:

  A = 0
  B = 0
  C = 0
  D = 0

  count = 0

  for line in csvFile:
    count += 1

    line = line.replace(',', ' ') #removes comma separating the numbers

    a = float (line.split()[0]) #converts strings into values
    b = float (line.split()[1])
    c = float (line.split()[2])
    d = float (line.split()[3])

    A = a + A # update the value of the column summatory 
    B = b + B
    C = c + C
    D = d + D

  print('The sepal length mean is ', "{0:.2f}".format(A/count), "cm") #result formatted so only two decimals are shown
  print('The sepal width mean is ', "{0:.2f}".format(B/count), "cm")
  print('The petal length mean is ', "{0:.2f}".format(C/count), "cm")
  print('The petal width mean is ', "{0:.2f}".format(D/count), "cm")
print()

"""
Sample of output from this script:

The sepal length mean is  5.84 cm
The sepal width mean is  3.05 cm
The petal length mean is  3.76 cm
The petal width mean is  1.20 cm

"""
  