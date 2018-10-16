import os
import csv

def startScreen():
    print()
    print('Welcome to NS Fietsen Stalling')
    print('1. Ik wil mijn fiets stallen')
    print('2. Ik wil me registreren')
    print('3. Ik wil mijn fiets ophalen')
    print('4. Ik wil informatie opvragen')
    print('5. Ik wil stoppen')
    print()

    choice = input('Voer je keus in: ')
    if choice == '1':
        Stallen()
    elif choice == '2':
        registreren()
    elif choice == '3':
        fietsOphalen()
    elif choice == '4':
        infoOpvragen()
    elif choice == '5':
        stoppen()
    else:
        os.system('CLS')
        print('['+choice+'] - is onbekend kies opnieuw')
        print('__________')
        startScreen()


def stoppen():
    print('Tot ziens')
    grapje = input('Houd je van grappen ?anwoord op j/n:').capitalize()
    if grapje == 'J':
        startScreen()
    else:
        print('Jij mag weg\nTotziens !!')




def stallen():
    with open ('fietsFile.csv', 'r+') as myCSVFile:
        persoonelijkInfo = csv.reader(myCSVFile)
        ovnummer = input('Vul je OV-nummer in: ')
        for ovNum in persoonelijkInfo:
            if ovNum in persoonelijkInfo:
                print('Ga maar je fiets stallen')
            else:
                print('Jij moet je eerst registreren')
                startScreen()



def registreren():
    import csv

    with open ('fietsFile.csv', 'w',newline='') as myCSVFile:
        persoonelijkInfo = csv.writer(myCSVFile, delimiter=';')
        persoonelijkInfo.writerow({'fietsnum','naam','ov_num','e-mail','ww'})

        naam = input('Voer jou (voor en achter) naam in: ')

        if naam is '':
            print('Ongeldige invoer, type je naam opnieuw')
            print(naam)

        elif len(naam) >= 31:
            print('Jij hebt te veel letters ingevoerd, probeer het opnieuw !')
            print(naam)

        fietsNum = input('Voer jou fiets nummer in: ')

        if len(fietsNum) < 4 and len(fietsNum)> 4 :
            print('Jij hebt een verkeerde fiets nummer ingvoerd, probeer het opnieuw !')
            print(fietsNum)

        ovNum = input('Voer je OV-Nummer in: ')

        if len(ovNum) > 16:
            print('Onjuist OV-nummer ingevoerd, probeer het opnieuw !')

        e_mail = input('Schrijf je e-mail adres: ')

        for mail in e_mail:
            mail = '@'
            if mail not in e_mail:
                print('Het is ongeldig e-mail, probeer het opnieuw')
                print(e_mail)

        ww = input('Vul een wacht woord in(bestaat uit 4 tekens): ')

        if len(ww) < 4 and len(ww) > 4 :
            print('Onjuist invoer, probeer het opnieuw !')
            print(ww)

        persoonelijkInfo.writerow({ovNum,naam,fietsNum,e_mail,ww})
    #return to start
    startScreen()

def infoLezen():
    gegevens = {}
    with open('fietsFile.csv', 'r+') as myCSVFile:
        for info in myCSVFile.readlines():
            ov_num, naam = info.split(",")
            gegevens[ov_num] = naam.strip()

    return gegevens

