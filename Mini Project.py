import os
import csv

with open ('fietsFile.csv', 'w+',newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=',')
    writer.writerow(['fietsnum','naam','ov_num','e-mail','ww'])

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
        info_checken()
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
    gestalldeFietsen = {}

    with open('fietsStalling.txt') as file:
        for info in file.readlines():
            ovnummer, fietsNum = info.split(';')
            gestalldeFietsen[ovnummer] = fietsNum.strip()

    return gestalldeFietsen

def nieuweFietsToevoegen(gestaldeFietsen):
    lines = []

    for ovNummer, fietsNummer in gestaldeFietsen.items():
        lines.append('{};{}'.format(ovNummer,fietsNummer.strip()))

    with open('fietsStalling.txt') as file:
        file.write('\n'.join(lines))


def registreren():

    with open ('fietsFile.csv', 'a',newline='') as myCSVFile:
        fieldnames = ['fietsnum','naam','ov_num','e-mail','ww']
        writer = csv.DictWriter(myCSVFile,fieldnames=fieldnames)

        naam = input('Voer jou (voor en achter) naam in: ')

        if naam is '':
            print('Ongeldige invoer, type je naam opnieuw')

        if len(naam) >= 51:
            print('Jij hebt te veel letters ingevoerd, probeer het opnieuw !')

        fietsNum = input('Voer jou fiets nummer(4 cijfers) in: ')

        if len(fietsNum) != 4:
            print('Jij hebt een verkeerde fiets nummer ingvoerd, probeer het opnieuw !')

        ovNum = input('Voer je OV-Nummer(16 cijfers) in: ')

        if len(ovNum) > 16:
            print('Onjuist OV-nummer ingevoerd, probeer het opnieuw !')

        e_mail = input('Schrijf je e-mail adres: ')

        for karakter in e_mail:
            if '@' not in e_mail:
                print('Het is ongeldig e-mail, probeer het opnieuw')

        wW = input('Vul een wacht woord in(bestaat uit 4 tekens): ')

        if len(wW) != 4:
            print('Onjuist invoer, probeer het opnieuw !')

        writer.writerow({'ov_num':ovNum,'naam':naam,'fietsnum':fietsNum,'e-mail':e_mail,'ww':wW})
    #return to start
    startScreen()

def zoek_gegevens():
    gegevens = {}
    with open('fietsFile.csv', 'r+') as myCSVFile:
        for info in myCSVFile.readlines():
            fietsnum, naam, ov_num, email, ww = info.split(",")
            gegevens[ov_num] = [fietsnum, naam, ov_num, email, ww]

    return gegevens


def info_checken():
    ov_num = input('geef je ov nummer: ')
    gegevens = zoek_gegevens()
    if ov_num in gegevens:
        print('fiets gevonden')
        print('naam van de beheerder:',gegevens[ov_num][1])
        print('Fiets nummer is:',gegevens[ov_num][2])

    else:
        print("")

    startScreen()

def fietsOphalen():
    gestalldeFietsen = zoek_gegevens()

    ovNum = input('Wat is je OVnummer: ')
    if ovNum not in gestalldeFietsen:
        print('Jou OVnummer {} kan niet gevonden worden'.format(ovNum))
        return

    wachtwoord = input('Voer jou wachtwoord in: ')
    juisteWachtwoord = gestalldeFietsen[wachtwoord]
    if wachtwoord != juisteWachtwoord:
        print('Jij hebt de verkeerde wachtwoord opgegeven, probeer het opnieuw!')
        return

    del gestalldeFietsen[zoek_gegevens()][1]
    print('{} Jij mag je fiets ophalen'.format(gestalldeFietsen[zoek_gegevens()][1]))

startScreen()