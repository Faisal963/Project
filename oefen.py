uurloon = input('Wat verdien je per uur: ')
aantalUur = input('Hoeveel uur heb je gewerkt :')
verdien = float(uurloon) * float(aantalUur)

afgerondNummerNaarTweeDecimalen = verdien
afgerondNummerNaarTweeDecimalen = round(verdien, 2)

print(aantalUur + ' uur werken levert '+ str(afgerondNummerNaarTweeDecimalen) + ' Euro op.')
