def registreren():
    import csv

    with open ('fietsFile.csv', 'r+',newline='') as myCSVFile:
        persoonelijkInfo = csv.writer(myCSVFile, delimiter=';')
        persoonelijkInfo.writerow({'fietsnum','naam','ov-num'})

        while True:
            naam = input('Voer jou naam in: ')
            if naam is '':
                break
            if len(naam) >= 21:
                print('Jij hebt te veel letters ingevoerd, probeer het opnieuw !')
                print(naam)
            fietsNum = input('Voer jou fiets nummer in: ')

            if len(fietsNum) < 4 and len(fietsNum)> 4 :
                print('Jij hebt een verkeerde fiets nummer ingvoerd, probeer het opnieuw !')
                print(fietsNum)
            ovNum = input('Voer je OV-Nummer in: ')
            if len(ovNum) > 16:
                print('Onjuist OV-nummer ingevoerd, probeer het opnieuw !')
            persoonelijkInfo.writerow({naam,ovNum,fietsNum})
