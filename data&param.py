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

# Parameters from the file ingnoring flower classes. Means:
meancol1 = np.mean(data[:,0])
meancol2 = np.mean(data[:,1])
meancol3 = np.mean(data[:,2])
meancol4 = np.mean(data[:,3])

print('sep_len  sep_wid  pet_len  pet_wid (cm)')
print()
print("1) PARAMETERS taken out of the file data IGNORING the flower classes:")
print()
print("MEANS (cm)")
print('  '+ '{0:.2f}'.format(meancol1) + "     " + '{0:.2f}'.format(meancol2) + "     " + '{0:.2f}'.format(meancol3) + "     " + '{0:.2f}'.format(meancol4))

# Medians
mediancol1 = np.median(data[:,0])
mediancol2 = np.median(data[:,1])
mediancol3 = np.median(data[:,2])
mediancol4 = np.median(data[:,3])

print()
print("MEDIANS (cm)")
print('  '+ '{0:.2f}'.format(mediancol1) + "     " + '{0:.2f}'.format(mediancol2) + "     " + '{0:.2f}'.format(mediancol3) + "     " + '{0:.2f}'.format(mediancol4))
print()

# modes 
modecol1 = stats.mode(data[:,0])
modecol2 = stats.mode(data[:,1])
modecol3 = stats.mode(data[:,2])
modecol4 = stats.mode(data[:,3])

print('MODES (cm) (sep_len  sep_wid  pet_len  pet_wid)') # The second attribute, count, is the number of times it occurs in the data set.
print("", modecol1, "\n", modecol2, "\n", modecol3, "\n", modecol4)
print()

# maximums
maxCol1= np.amax(data[:,0])
maxCol2= np.amax(data[:,1])
maxCol3= np.amax(data[:,2])
maxCol4= np.amax(data[:,3])

print('MAXIMUMS (cm)')
print("  ", maxCol1, "    ", maxCol2, "    ", maxCol3, "    ", maxCol4)
print()
print(' sep_len  sep_wid  pet_len  pet_wid (cm)')
print()

# minimums
minCol1= np.amin(data[:,0])
minCol2= np.amin(data[:,1])
minCol3= np.amin(data[:,2])
minCol4= np.amin(data[:,3])

print('MINIMUMS (cm)')
print("  ", minCol1, "    ", minCol2, "    ", minCol3, "    ", minCol4)
print()

# standard deviation
stdcol1 = np.std(data[:,0])
stdcol2 = np.std(data[:,1])
stdcol3 = np.std(data[:,2])
stdcol4 = np.std(data[:,3])

print("STANDARD DEVIATIONS (cm)")
print('   '+ '{0:.2f}'.format(stdcol1) + "     " + '{0:.2f}'.format(stdcol2) + "     " + '{0:.2f}'.format(stdcol3) + "     " + '{0:.2f}'.format(stdcol4))
print()
print()


print("2) PARAMETERS taken out of the file data CONSIDERING the flower classes:")

# means by flower class: sepal length
meanSetSL= np.mean(data[0:50,0])
meanVerSL= np.mean(data[51:100,0])
meanVirSL= np.mean(data[101:150,0])
# means sepal width
meanSetSW= np.mean(data[0:50,1])
meanVerSW= np.mean(data[51:100,1])
meanVirSW= np.mean(data[101:150,1])
# means petal length
meanSetPL= np.mean(data[0:50,2])
meanVerPL= np.mean(data[51:100,2])
meanVirPL= np.mean(data[101:150,2])
# means petal width
meanSetPW= np.mean(data[0:50,3])
meanVerPW= np.mean(data[51:100,3])
meanVirPW= np.mean(data[101:150,3])

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
medianSetSL= np.median(data[0:50,0])
medianVerSL= np.median(data[51:100,0])
medianVirSL= np.median(data[101:150,0])
# medians sepal width
medianSetSW= np.median(data[0:50,1])
medianVerSW= np.median(data[51:100,1])
medianVirSW= np.median(data[101:150,1])
# medians petal length
medianSetPL= np.median(data[0:50,2])
medianVerPL= np.median(data[51:100,2])
medianVirPL= np.median(data[101:150,2])
# medians petal width
medianSetPW= np.median(data[0:50,3])
medianVerPW= np.median(data[51:100,3])
medianVirPW= np.median(data[101:150,3])

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
modeSetSL= stats.mode(data[0:50,0])
modeVerSL= stats.mode(data[51:100,0])
modeVirSL= stats.mode(data[101:150,0])
# modes sepal width
modeSetSW= stats.mode(data[0:50,1])
modeVerSW= stats.mode(data[51:100,1])
modeVirSW= stats.mode(data[101:150,1])
# modes petal length
modeSetPL= stats.mode(data[0:50,2])
modeVerPL= stats.mode(data[51:100,2])
modeVirPL= stats.mode(data[101:150,2])
# modes petal width
modeSetPW= stats.mode(data[0:50,3])
modeVerPW= stats.mode(data[51:100,3])
modeVirPW= stats.mode(data[101:150,3])

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
maxSetSL= np.amax(data[0:50,0])
maxVerSL= np.amax(data[51:100,0])
maxVirSL= np.amax(data[101:150,0])
# maximums sepal width
maxSetSW= np.amax(data[0:50,1])
maxVerSW= np.amax(data[51:100,1])
maxVirSW= np.amax(data[101:150,1])
# maximums petal length
maxSetPL= np.amax(data[0:50,2])
maxVerPL= np.amax(data[51:100,2])
maxVirPL= np.amax(data[101:150,2])
# maximums petal width
maxSetPW= np.amax(data[0:50,3])
maxVerPW= np.amax(data[51:100,3])
maxVirPW= np.amax(data[101:150,3])

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
minSetSL= np.amin(data[0:50,0])
minVerSL= np.amin(data[51:100,0])
minVirSL= np.amin(data[101:150,0])
# minimums sepal width
minSetSW= np.amin(data[0:50,1])
minVerSW= np.amin(data[51:100,1])
minVirSW= np.amin(data[101:150,1])
# minimums petal length
minSetPL= np.amin(data[0:50,2])
minVerPL= np.amin(data[51:100,2])
minVirPL= np.amin(data[101:150,2])
# minimums petal width
minSetPW= np.amin(data[0:50,3])
minVerPW= np.amin(data[51:100,3])
minVirPW= np.amin(data[101:150,3])

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
stdSetSL= np.std(data[0:50,0])
stdVerSL= np.std(data[51:100,0])
stdVirSL= np.std(data[101:150,0])
# standard deviations sepal width
stdSetSW= np.std(data[0:50,1])
stdVerSW= np.std(data[51:100,1])
stdVirSW= np.std(data[101:150,1])
# standard deviations petal length
stdSetPL= np.std(data[0:50,2])
stdVerPL= np.std(data[51:100,2])
stdVirPL= np.std(data[101:150,2])
# standard deviations petal width
stdSetPW= np.std(data[0:50,3])
stdVerPW= np.std(data[51:100,3])
stdVirPW= np.std(data[101:150,3])

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
