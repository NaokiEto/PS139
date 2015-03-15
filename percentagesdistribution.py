import csv
import pylab
import numpy as np
import math
import locale

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

frequency = [0] * 100
with open('2011_Pres_Pstn.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[10] != '' and row[20] != '' and row[20] != 'INVALID':
            print "The row is: ", row[10]
            registered = locale.atof(row[10])
            spoilt = locale.atof(row[20])
            percentage = int(math.floor(spoilt/registered * 100.0))

            frequency[percentage] += 1

print "The frequency table is: ", frequency

percentages = range(0, 100)

pylab.plot(percentages, frequency)

pylab.legend()

pylab.xlabel('Percentage')
pylab.ylabel('Frequency')
pylab.title('Frequency of a percentage of invalid votes per polling station, floored to the nearest percentage')
pylab.show()
