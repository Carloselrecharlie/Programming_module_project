
# Carlos Montés Parra

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

    print(line[:3]+ '      ' + line[4:7]+ '      ' + line[8:11]+ '      ' + line[12:15]) 

    A = a + A # update the value of the column summatory 
    B = b + B
    C = c + C
    D = d + D

  print('The sepal length median is ', "{0:.1f}".format(A/count)) #result formatted so only one decimal is shown
  print('The sepal width median is ', "{0:.1f}".format(B/count))
  print('The petal length median is ', "{0:.1f}".format(C/count))
  print('The petal width median is ', "{0:.1f}".format(D/count))

  