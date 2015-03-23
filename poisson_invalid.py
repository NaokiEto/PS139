import csv
import pylab
import numpy as np
import math
import locale

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

frequency = np.zeros(100)
numrows = 0
totalpercentages = 0
with open('2011_Pres_Pstn.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[10] != '' and row[20] != '' and row[20] != 'INVALID':
            #print "The row is: ", row[10]
            registered = locale.atof(row[10])
            spoilt = locale.atof(row[20])
            percentage = int(math.floor(spoilt/registered * 100.0))
            totalpercentages += percentage
            numrows += 1
            frequency[percentage] += 1

print "The frequency table is: ", frequency

percentages = range(0, 100)

sum_frequency = sum(frequency)

probabilities = frequency / float(sum_frequency)

print "The total number of frequencies is: ", sum_frequency

print "The probabilities are: ", probabilities

average = float(totalpercentages)/float(numrows)

print "The average is: ", average

avg_prob = sum(probabilities)/len(probabilities)

print "Average probability is: ", avg_prob

ss_tot = 0.0

for i in range(len(percentages)):
    ss_tot += (probabilities[i] - avg_prob) ** 2

poisson = [float(average) ** int(x) / float(math.factorial(int(x))) * float(math.exp(-1.0 * average)) for x in percentages]

sum_res = 0.0

for i in range(len(percentages)):
    sum_res += (probabilities[i] - poisson[i])**2

print "The sum_res is: ", sum_res

print "The r^2 is: ", 1.0 - sum_res/ss_tot

pylab.plot(percentages, probabilities, '-r')
pylab.plot(percentages, poisson, '-b')

pylab.ylabel('Probability')
pylab.xlabel('K')
pylab.title('Poisson Fitting of Normalized Invalid Votes per Polling Station')
pylab.show()
