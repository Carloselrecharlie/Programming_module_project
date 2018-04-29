# Carlos Montes code for the project of the module "Programming and scripting"
# Data visualization and parameters

import csv
import numpy as np
import matplotlib.pyplot as mpl
from scipy import stats # to calculate the mode

print()
print('sep_len  sep_wid  pet_len  pet_wid (cm)')
print()


with open('data/iris.csv', newline='') as csvFile:

  for line in csvFile:

    line = line.replace(',', ' ') #removes comma separating the numbers

    print('  ' + line[:3]+ '      ' + line[4:7]+ '      ' + line[8:11]+ '      ' + line[12:15])
    # This line prints in groups of 3 positions because the 4th value is excluded. 
    # F.i. the first instruction prints the positions 0, 1st and 2nd but 3rd position (the white space) is excluded

data = np.genfromtxt('data/iris.csv', delimiter = ',')

# defining VARIABLES
# column variables
col1 = data[:,0]
col2 = data[:,1]
col3 = data[:,2]
col4 = data[:,3]

# flower class variables
setSL = data[0:50,0]
setSW = data[0:50,1]
setPL = data[0:50,2]
setPW = data[0:50,3]

verSL = data[51:100,0]
verSW = data[51:100,1]
verPL = data[51:100,2]
verPW = data[51:100,3]

virSL = data[101:150,0]
virSW = data[101:150,1]
virPL = data[101:150,2]
virPW = data[101:150,3]


# Parameters from the file ingnoring flower classes. Means:
meancol1 = np.mean(col1)
meancol2 = np.mean(col2)
meancol3 = np.mean(col3)
meancol4 = np.mean(col4)

print('sep_len  sep_wid  pet_len  pet_wid (cm)')
print()
print("1) PARAMETERS taken out of the file data IGNORING the flower classes:")
print()
print("MEANS (cm)")
print('  '+ '{0:.2f}'.format(meancol1) + "     " + '{0:.2f}'.format(meancol2) + "     " + '{0:.2f}'.format(meancol3) + "     " + '{0:.2f}'.format(meancol4))

# Medians
mediancol1 = np.median(col1)
mediancol2 = np.median(col2)
mediancol3 = np.median(col3)
mediancol4 = np.median(col4)

print()
print("MEDIANS (cm)")
print('  '+ '{0:.2f}'.format(mediancol1) + "     " + '{0:.2f}'.format(mediancol2) + "     " + '{0:.2f}'.format(mediancol3) + "     " + '{0:.2f}'.format(mediancol4))
print()

# modes 
modecol1 = stats.mode(col1)
modecol2 = stats.mode(col2)
modecol3 = stats.mode(col3)
modecol4 = stats.mode(col4)

print('MODES (cm) (sep_len  sep_wid  pet_len  pet_wid)') # The second attribute, count, is the number of times it occurs in the data set.
print("", modecol1, "\n", modecol2, "\n", modecol3, "\n", modecol4)
print()

# maximums
maxCol1= np.amax(col1)
maxCol2= np.amax(col2)
maxCol3= np.amax(col3)
maxCol4= np.amax(col4)

print('MAXIMUMS (cm)')
print("  ", maxCol1, "    ", maxCol2, "    ", maxCol3, "    ", maxCol4)
print()
print(' sep_len  sep_wid  pet_len  pet_wid (cm)')
print()

# minimums
minCol1= np.amin(col1)
minCol2= np.amin(col2)
minCol3= np.amin(col3)
minCol4= np.amin(col4)

print('MINIMUMS (cm)')
print("  ", minCol1, "    ", minCol2, "    ", minCol3, "    ", minCol4)
print()

# standard deviation
stdcol1 = np.std(col1)
stdcol2 = np.std(col2)
stdcol3 = np.std(col3)
stdcol4 = np.std(col4)

print("STANDARD DEVIATIONS (cm)")
print('   '+ '{0:.2f}'.format(stdcol1) + "     " + '{0:.2f}'.format(stdcol2) + "     " + '{0:.2f}'.format(stdcol3) + "     " + '{0:.2f}'.format(stdcol4))
print()

# correlation coefficient between leaf length and width 
corCcol1_2 = np.corrcoef(col1, col2)[1,0] # [1,0] added to obtain just one value
corCcol3_4 = np.corrcoef(col3, col4)[1,0]

print('CORRELATION COEFFICITENT')
print(' - Between sepal length and sepal width', '{0:.2f}'.format(corCcol1_2))
print(' - Between petal length and petal width', '{0:.2f}'.format(corCcol3_4))
print()
print()


print("2) PARAMETERS taken out of the file data CONSIDERING the flower classes:")

# means by flower class: sepal length
meanSetSL= np.mean(setSL)
meanVerSL= np.mean(verSL)
meanVirSL= np.mean(virSL)
# means sepal width
meanSetSW= np.mean(setSW)
meanVerSW= np.mean(verSW)
meanVirSW= np.mean(virSW)
# means petal length
meanSetPL= np.mean(setPL)
meanVerPL= np.mean(verPL)
meanVirPL= np.mean(virPL)
# means petal width
meanSetPW= np.mean(setPW)
meanVerPW= np.mean(verPW)
meanVirPW= np.mean(virPW)

print()
print('MEANS by flower class (cm)')
print()

print('Iris Setosa')
print('    '+ '{0:.2f}'.format(meanSetSL) + "     " + '{0:.2f}'.format(meanSetSW) + "     " + '{0:.2f}'.format(meanSetPL) + "     " + '{0:.2f}'.format(meanSetPW))
print('Iris Versicolor')
print('    '+ '{0:.2f}'.format(meanVerSL) + "     " + '{0:.2f}'.format(meanVerSW) + "     " + '{0:.2f}'.format(meanVerPL) + "     " + '{0:.2f}'.format(meanVerPW))
print('Iris Virginica')
print('    '+ '{0:.2f}'.format(meanVirSL) + "     " + '{0:.2f}'.format(meanVirSW) + "     " + '{0:.2f}'.format(meanVirPL) + "     " + '{0:.2f}'.format(meanVirPW))
print()
print('  sep_len  sep_wid  pet_len  pet_wid (cm)')


# medians by flower class: sepal length
medianSetSL= np.median(setSL)
medianVerSL= np.median(verSL)
medianVirSL= np.median(virSL)
# medians sepal width
medianSetSW= np.median(setSW)
medianVerSW= np.median(verSW)
medianVirSW= np.median(virSW)
# medians petal length
medianSetPL= np.median(setPL)
medianVerPL= np.median(verPL)
medianVirPL= np.median(virPL)
# medians petal width
medianSetPW= np.median(setPW)
medianVerPW= np.median(verPW)
medianVirPW= np.median(virPW)

print()
print('MEDIANS by flower class (cm)')
print()
print('Iris Setosa') 
print("    ", medianSetSL, "    ", medianSetSW, "    ", medianSetPL, "    ", medianSetPW)
print('Iris Versicolor')
print("    ", medianVerSL, "    ", medianVerSW, "    ", medianVerPL, "    ", medianVerPW)
print('Iris Virginica')
print("    ", medianVirSL, "    ", medianVirSW, "    ", medianVirPL, "    ", medianVirPW)
print()

# modes by flower class: sepal length 
modeSetSL= stats.mode(setSL)
modeVerSL= stats.mode(verSL)
modeVirSL= stats.mode(virSL)
# modes sepal width
modeSetSW= stats.mode(setSW)
modeVerSW= stats.mode(verSW)
modeVirSW= stats.mode(virSW)
# modes petal length
modeSetPL= stats.mode(setPL)
modeVerPL= stats.mode(verPL)
modeVirPL= stats.mode(virPL)
# modes petal width
modeSetPW= stats.mode(setPW)
modeVerPW= stats.mode(verPW)
modeVirPW= stats.mode(virPW)

print()
print('MODES by flower class (cm) (sep_len  sep_wid  pet_len  pet_wid)') # The second attribute, count, is the number of times it occurs in the data set.
print()
print('Iris Setosa') # The \n introduces a break line
print("", modeSetSL, "\n", modeSetSW, "\n", modeSetPL, "\n", modeSetPW)
print()
print('Iris Versicolor')
print("", modeVerSL, "\n", modeVerSW, "\n", modeVerPL, "\n", modeVerPW)
print()
print('Iris Virginica')
print("", modeVirSL, "\n", modeVirSW, "\n", modeVirPL, "\n", modeVirPW)
print()

# maximum values by flower class: sepal length
maxSetSL= np.amax(setSL)
maxVerSL= np.amax(verSL)
maxVirSL= np.amax(virSL)
# maximums sepal width
maxSetSW= np.amax(setSW)
maxVerSW= np.amax(verSW)
maxVirSW= np.amax(virSW)
# maximums petal length
maxSetPL= np.amax(setPL)
maxVerPL= np.amax(verPL)
maxVirPL= np.amax(virPL)
# maximums petal width
maxSetPW= np.amax(setPW)
maxVerPW= np.amax(verPW)
maxVirPW= np.amax(virPW)

print()
print('MAXIMUMS by flower class (cm)')
print()
print('Iris Setosa') 
print("  ", maxSetSL, "    ", maxSetSW, "    ", maxSetPL, "    ", maxSetPW)
print('Iris Versicolor')
print("  ", maxVerSL, "    ", maxVerSW, "    ", maxVerPL, "    ", maxVerPW)
print('Iris Virginica')
print("  ", maxVirSL, "    ", maxVirSW, "    ", maxVirPL, "    ", maxVirPW)
print()
print(' sep_len  sep_wid  pet_len  pet_wid (cm)')

# minimum values by flower class: sepal length
minSetSL= np.amin(setSL)
minVerSL= np.amin(verSL)
minVirSL= np.amin(virSL)
# minimums sepal width
minSetSW= np.amin(setSW)
minVerSW= np.amin(verSW)
minVirSW= np.amin(virSW)
# minimums petal length
minSetPL= np.amin(setPL)
minVerPL= np.amin(verPL)
minVirPL= np.amin(virPL)
# minimums petal width
minSetPW= np.amin(setPW)
minVerPW= np.amin(verPW)
minVirPW= np.amin(virPW)

print()
print('MINIMUMS by flower class (cm)')
print()
print('Iris Setosa') 
print("  ", minSetSL, "    ", minSetSW, "    ", minSetPL, "    ", minSetPW)
print('Iris Versicolor')
print("  ", minVerSL, "    ", minVerSW, "    ", minVerPL, "    ", minVerPW)
print('Iris Virginica')
print("  ", minVirSL, "    ", minVirSW, "    ", minVirPL, "    ", minVirPW)
print()

# standard deviations by flower class: sepal length
stdSetSL= np.std(setSL)
stdVerSL= np.std(verSL)
stdVirSL= np.std(virSL)
# standard deviations sepal width
stdSetSW= np.std(setSW)
stdVerSW= np.std(verSW)
stdVirSW= np.std(virSW)
# standard deviations petal length
stdSetPL= np.std(setPL)
stdVerPL= np.std(verPL)
stdVirPL= np.std(virPL)
# standard deviations petal width
stdSetPW= np.std(setPW)
stdVerPW= np.std(verPW)
stdVirPW= np.std(virPW)

print()
print('STANDARD DEVIATIONS by flower class (cm)')
print()
print(' sep_len  sep_wid  pet_len  pet_wid (cm)')
print()

print('Iris Setosa')
print('   '+ '{0:.2f}'.format(stdSetSL) + "     " + '{0:.2f}'.format(stdSetSW) + "     " + '{0:.2f}'.format(stdSetPL) + "     " + '{0:.2f}'.format(stdSetPW))
print('Iris Versicolor')
print('   '+ '{0:.2f}'.format(stdVerSL) + "     " + '{0:.2f}'.format(stdVerSW) + "     " + '{0:.2f}'.format(stdVerPL) + "     " + '{0:.2f}'.format(stdVerPW))
print('Iris Virginica')
print('   '+ '{0:.2f}'.format(stdVirSL) + "     " + '{0:.2f}'.format(stdVirSW) + "     " + '{0:.2f}'.format(stdVirPL) + "     " + '{0:.2f}'.format(stdVirPW))
print()

# Correlation coefficient between length and width flower leaf 
setCorSepal = np.corrcoef(setSL, setSW)[1,0]
setCorPetal = np.corrcoef(setPL, setPW)[1,0]

verCorSepal = np.corrcoef(verSL, verSW)[1,0]
verCorPetal = np.corrcoef(verPL, verPW)[1,0]

virCorSepal = np.corrcoef(virSL, virSW)[1,0]
virCorPetal = np.corrcoef(virPL, virPW)[1,0]

print('The correlation coefficient between length and leaf from every leaf from every flower is:')
print()
print(' - setosa sepal', '{0:.2f}'.format(setCorSepal))
print(' - setosa petal', '{0:.2f}'.format(setCorPetal))
print()
print(' - versicolor sepal', '{0:.2f}'.format(verCorSepal))
print(' - versicolor petal', '{0:.2f}'.format(verCorPetal))
print()
print(' - virginica sepal', '{0:.2f}'.format(virCorSepal))
print(' - virginica petal', '{0:.2f}'.format(virCorPetal))
print()

"""
Sample of output from this code:

  5.8      2.7      5.1      1.9
  6.8      3.2      5.9      2.3
  6.7      3.3      5.7      2.5
  6.7      3.0      5.2      2.3
  6.3      2.5      5.0      1.9
  6.5      3.0      5.2      2.0
  6.2      3.4      5.4      2.3
  5.9      3.0      5.1      1.8
sep_len  sep_wid  pet_len  pet_wid (cm)

1) PARAMETERS taken out of the file data IGNORING the flower classes:

MEANS (cm)
  5.84     3.05     3.76     1.20

MEDIANS (cm)
  5.80     3.00     4.35     1.30

MODES (cm) (sep_len  sep_wid  pet_len  pet_wid)
 ModeResult(mode=array([ 5.]), count=array([10]))
 ModeResult(mode=array([ 3.]), count=array([26]))
 ModeResult(mode=array([ 1.5]), count=array([14]))
 ModeResult(mode=array([ 0.2]), count=array([28]))

MAXIMUMS (cm)
   7.9      4.4      6.9      2.5

 sep_len  sep_wid  pet_len  pet_wid (cm)

MINIMUMS (cm)
   4.3      2.0      1.0      0.1

STANDARD DEVIATIONS (cm)
   0.83     0.43     1.76     0.76

CORRELATION COEFFICITENT
 - Between sepal length and sepal width -0.11
 - Between petal length and petal width 0.96


2) PARAMETERS taken out of the file data CONSIDERING the flower classes:

MEANS by flower class (cm)

Iris Setosa
    5.01     3.42     1.46     0.24
Iris Versicolor
    5.91     2.76     4.25     1.32
Iris Virginica
    6.59     2.97     5.54     2.02

  sep_len  sep_wid  pet_len  pet_wid (cm)

  """