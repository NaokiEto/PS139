import csv
import pylab
import numpy as np
import math
import locale

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

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

percent_max = 20

frequency = np.zeros(100)
numrows = 0
totalpercentages = 0
with open('2011_Pres_Pstn.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[10] != '' and row[20] != '' and row[20] != 'INVALID'\
            and row[1] in south_region:
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

avg_prob = sum(probabilities[:percent_max])/len(probabilities[:percent_max])

print "Average probability is: ", avg_prob

ss_tot = 0.0

for i in range(len(percentages[:percent_max])):
    ss_tot += (probabilities[i] - avg_prob) ** 2


poisson_fit = [float(average) ** int(x) / float(math.factorial(int(x))) * float(math.exp(-1.0 * average)) for x in percentages]

sum_res = 0

for i in range(len(percentages[:percent_max])):
    sum_res += (probabilities[i] - poisson_fit[i])**2

print "The sum_res is: ", sum_res

print "The r^2 is: ", 1.0 - sum_res/ss_tot

pylab.plot(percentages[:percent_max], probabilities[:percent_max], '-r')
pylab.plot(percentages[:percent_max], poisson_fit[:percent_max], '-b')


pylab.ylabel('Probability')
pylab.xlabel('K')
pylab.title('Poisson Fitting of Normalized Invalid Votes per Polling Station South of the Nile River')
pylab.show()
