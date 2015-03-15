import csv
import pylab
import numpy as np
import math

x = pylab.arange(1, 10, 0.01)

benford = pylab.log10(1.0 + 1.0/x)

pylab.plot(x, benford, label='Benford\'s Law')

#pylab.show()

counter = [0] * 9
nocount = 0
minimum = 200
maximum = 200

nullifiedpoll = 0
notreceivedpoll = 0

with open('2011_Pres_Pstn.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[11] == 'X':
            nullifiedpoll += 1
        if row[11] == '?':
            notreceivedpoll += 1
        if row[10] != '' and row[19] != 'VALID':
            #print row[10], row[19]
            if row[19] != '':
                valid = int(row[19][:1])
                #print "wtf: ", row[19]
                #print "the length of the row is: ", len(row[19])
                if len(row[19]) > 1 and row[19][1] != ',' and row[19][1] != ' ':
                    num = int(row[19])
                    if num < minimum:
                        minimum = num
                    if num > maximum:
                        maximum = num
                elif len(row[19]) == 1:
                    num = int(row[19])
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


print nullifiedpoll
print notreceivedpoll

integerx = range(1, 10)

pylab.plot(integerx, counter, 'ro', label='Initial digit of Valid Number of Voters')

pylab.legend()

pylab.xlabel('Leading digit')
pylab.ylabel('Frequency')
pylab.title('Frequency Comparison Between Initial digit of Valid Number of Voters at Each Polling Station')
pylab.show()
