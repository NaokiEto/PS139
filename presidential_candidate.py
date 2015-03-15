import csv
import pylab
import numpy as np
import math

column = 15

x = pylab.arange(1, 10, 0.01)

benford = pylab.log10(1.0 + 1.0/x)

pylab.plot(x, benford, label='Benford\'s Law')

#pylab.show()

counter = [0] * 9
nocount = 0
minimum = 200
maximum = 200

with open('2011_Pres_Pstn.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[10] != '' and row[19] != 'VALID':
            #print row[10], row[19]
            if row[column] != '' and row[column] != '?' and row[19] != '':
                #print "district: ", row[0]
                #print "huh, ", row[column]
                valid = int(row[column][:1])
                #print "wtf: ", row[19]
                #print "the length of the row is: ", len(row[19])
                if len(row[column]) > 1 and row[column][1] != ',' and row[column][1] != ' ':
                    num = int(row[column])
                    if num < minimum:
                        minimum = num
                    if num > maximum:
                        maximum = num
                elif len(row[column]) == 1:
                    num = int(row[column])
                    #print num
                    #print row
                    if num < minimum:
                        minimum = num
                #print valid
                counter[valid-1] += 1
            else:
                nocount += 1

print counter
total = sum(counter)
counter = [float(x)/float(total) for x in counter]
print counter
print "The number of blanks at valid voters column: ", nocount

print "The maximum is: ", maximum
print "The minimum is: ", minimum


integerx = range(1, 10)

pylab.plot(integerx, counter, 'ro', label='Initial digit of Valid Number of Voters')

pylab.legend(loc='upper middle')

pylab.xlabel('Leading digit')
pylab.ylabel('Frequency')
pylab.title('Frequency Comparison Between Initial digit of Valid Number of Voters at Each Polling Station for Mao Norbert')
pylab.show()
