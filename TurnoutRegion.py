import csv
import pylab
import numpy as np
import math
from scipy.optimize import curve_fit
#import matplotlib as plt

def func(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2.0*sigma**2))

columns = range(11, 19)
names = ['Abed Bwanika', 'Besigye Kifefe Kizza', 'Beti Olive Kamya Namisango', \
         'Bidandissali Jaberi', 'Mao Norbert', 'Olara Otunnu', \
         'Samuel Lubega Mukaaku Walter', 'Yoweri Museveni Kaguta']

north = ['Abim', 'Adjumani', 'Agago', 'Alebtong', 'Amolatar', 'Amudat', \
         'Amuru', 'Apac', 'Arua', 'Dokolo', 'Gulu', 'Kaabong', 'Kitgum', \
         'Koboko', 'Kole', 'Kotido', 'Lamwo', 'Lira', 'Maracha', 'Moroto', \
         'Moyo', 'Nakapiripirit', 'Napak', 'Nebbi', 'Nwoya', 'Otuke', \
         'Oyam', 'Pader', 'Yumbe', 'Zombo']

central = ['Buikwe', 'Bukomansimbi', 'Butambala', 'Buvuma', 'Gomba', \
           'Kalangala', 'Kalungu', 'Kampala', 'Kayunga', 'Kiboga', \
           'Kyankwanzi', 'Luweero', 'Lwengo', 'Lyantonde', 'Masaka', \
           'Mityana', 'Mpigi', 'Mubende', 'Mukono', 'Nakaseke', \
           'Nakasongola', 'Rakai', 'Sembabule', 'Wakiso']

eastern = ['Amuria', 'Budaka', 'Bududa', 'Bugiri', 'Bukedea', 'Bukwa', \
           'Bulambuli', 'Busia', 'Butaleja', 'Buyende', 'Iganga', \
           'Jinja', 'Kaberamaido', 'Kaliro', 'Kamuli', 'Kapchorwa', \
           'Katakwi', 'Kibuku', 'Kumi', 'Kween', 'Luuka', 'Manafwa', \
           'Mayuge', 'Mbale', 'Namayingo', 'Namutumba', 'Ngora', 'Pallisa', \
           'Serere', 'Sironko', 'Soroti']

western = ['Buhweju', 'Buliisa', 'Bundibugyo', 'Bushenyi', 'Hoima', 'Ibanda', \
           'Isingiro', 'Kabale', 'Kabarole', 'Kamwenge', 'Kanungu', 'Kasese', \
           'Kibaale', 'Kiruhura', 'Kiryandongo', 'Kisoro', 'Kyegegwa', 'Kyenjojo', \
           'Masindi', 'Mbarara', 'Mitooma', 'Ntoroko', 'Ntungamo', 'Rubirizi', \
           'Rukungiri', 'Sheema']

northupper = [x.upper() for x in north]
centralupper = [x.upper() for x in central]
easternupper = [x.upper() for x in eastern]
westernupper = [x.upper() for x in western]

north_region = northupper + easternupper
south_region = centralupper + westernupper

index = 5
pylab.figure(figsize=(16, 12))
column = columns[index]
name = names[index]

Frequency = [0] * 101

nocount = 0
minimum = 200
maximum = 200

rownumber = 0
with open('2011_Pres_Pstn.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[10] != '' and row[19] != 'VALID':
	    #print row[10], row[19]
	    if row[column] != '' and row[column] != '?' and row[19] != ''\
	       and row[1] in south_region:
	        #print row
	        #print "district: ", row[0]
	        #valid = int(row[19][:1])
	        # Get the number of votes for a particular candidate
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
	        elif row[column][1] == ',':
	           thousands = int(row[column][0])
	           rest = int(row[column][2:])
	           num = thousands * 1000 + rest
	           if num > maximum:
	               maximum = num

	        #print row[19]
	        # Get the number of valid votes for the polling station
	        if len(row[19]) > 1 and row[19][1] != ',':
	            valid = int(row[19])
	        elif len(row[19]) == 1:
	            valid = int(row[19])
	            #if valid < 2:
	            #    print row
	        elif row[19][1] == ',':
	            thousands = int(row[19][0])
	            rest = int(row[19][2:])
	            valid = thousands * 1000 + rest


	        if len(row[20]) > 1 and row[20][1] != ',':
	            invalid = int(row[20])
	        elif len(row[20]) == 1:
	            invalid = int(row[20])
	            #if valid < 2:
	            #    print row
	        elif row[20][1] == ',':
	            thousands = int(row[20][0])
	            rest = int(row[20][2:])
	            invalid = thousands * 1000 + rest

	        # Get the number of registered voters for the polling station
	        if len(row[10]) > 0 and row[10][1] != ',':
	            registered = int(row[10])
	        elif len(row[10]) == 1:
	            registered = int(row[10])
	        elif row[10][1] == ',':
	            thousands = int(row[10][0])
	            rest = int(row[10][2:])
	            registered = thousands * 1000 + rest
	        
	        if valid + invalid > 100:
	            turnout = int(round((float(valid) + float(invalid))/float(registered) * 100.0))
	            Frequency[turnout] += 1
	            rownumber += 1
	        #print valid
	        #counter[valid-1] += 1
	    else:
	        nocount += 1

print "The maximum is: ", maximum
print "The minimum is: ", minimum



total = float(sum(Frequency))
normalized_freq = np.asarray(Frequency) / total

xcoord = np.arange(0, 101) * 0.01

print normalized_freq
print xcoord

pylab.bar(100.0 * xcoord, np.asarray(Frequency), color='g')

popt, pcov = curve_fit(func, xcoord, normalized_freq)

print popt

pylab.plot(100.0 * xcoord, func(xcoord, popt[0], popt[1], popt[2]) * total, '-r')

pylab.xlabel('Turnout')
pylab.ylabel('Frequency')
pylab.title('Turnout by Polling Station South of the Nile River')

#pylab.show()
pylab.savefig('SouthTurnout.png')

