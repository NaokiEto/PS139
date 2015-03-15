import csv
import pylab
import numpy as np
import math
#import matplotlib as plt

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

for index in range(8):
    pylab.figure(figsize=(16, 12))
    column = columns[index]
    name = names[index]

    VE = [0] * 27472
    Turnout = [0] * 27472

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
                        VE[rownumber] = float(num)/float(registered)
                        Turnout[rownumber] = (float(valid) + float(invalid))/float(registered)
                        rownumber += 1
                    #print valid
                    #counter[valid-1] += 1
                else:
                    nocount += 1

    print "The maximum is: ", maximum
    print "The minimum is: ", minimum


    integerx = range(1, 10)

    pylab.plot(Turnout[:rownumber], VE[:rownumber], 'bo', label='V/E')

    pylab.legend(loc='upper middle')

    pylab.xlabel('Turnout')
    pylab.ylabel('V/E')
    pylab.title('V/E VS. Turnout per Polling Station with > 100 Valid Votes South of the Nile River for ' + name)

    npturnout = np.asarray(Turnout[:rownumber])
    #npVE = np.asarray(VE[:rownumber])

    print "the number of terms is: ", npturnout.shape

    linearnpturnout = np.array([npturnout, np.ones(npturnout.shape[0])])
    # Getting the coefficients of the linear regression line and the residuals for the r^2
    w, resid = np.linalg.lstsq(linearnpturnout.T, VE[:rownumber])[:2]

    line = w[0] * npturnout + w[1] # regression line
    pylab.plot(npturnout, line, 'r-')

    y = np.asarray(VE[:rownumber])

    r2 = 1 - resid / (y.size * y.var())
    print r2

    fo = open("SouthVEturnoutCoefficients.txt", "a")
    fo.write( name + "\n" + "slope: " + str(w[0]) )
    fo.write("\ny-intercept: " + str(w[1]) )
    fo.write("\nr^2: " + str(r2[0]) )
    fo.write("\n\n")

    fo.close()


    #pylab.show()
    pylab.savefig('South_VETurnout' + name + '100.png')


