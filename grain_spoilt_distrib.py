import csv
import pylab
import numpy as np
import math
import locale

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

frequency = [0] * 1000
with open('2011_Pres_Pstn.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[10] != '' and row[21] != '' and row[21] != 'SPOILT':
            #print "The row is: ", row[10]
            registered = locale.atof(row[10])
            spoilt = locale.atof(row[21])
            percentage = round(spoilt/registered * 100.0, 1)

            if percentage != 0.0:
                print percentage, int(percentage * 10)
            frequency[int(percentage * 10)] += 1

print "The frequency table is: ", frequency

percentages = np.arange(0, 1000) * 0.1

pylab.plot(percentages, frequency)

pylab.legend()

pylab.xlabel('Percentage')
pylab.ylabel('Frequency')
pylab.title('Frequency of a percentage of spoilt votes per polling station, floored to the nearest percentage')
pylab.show()
