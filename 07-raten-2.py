import random

gewonnen = False
versuche = 0
Name = raw_input("Name: ")
zufallszahl_minimal = input("Von: ")
zufallszahl_maximal = input("Bis: ")
zufallszahl = random.randint(zufallszahl_minimal, zufallszahl_maximal)

while gewonnen is False:
	benutzereingabe = input("Raten Sie eine Zahl zwischen %d und %d: " % (zufallszahl_minimal, zufallszahl_maximal)) 
	if benutzereingabe >= zufallszahl_minimal and benutzereingabe <= zufallszahl_maximal:
		versuche += 1

		if zufallszahl is benutzereingabe:
			print "Gewonnen! Herzlichen glueckwunsch %s" % Name
			print "Sie haben %d Versuche gebraucht." % versuche
			gewonnen = True
		else:
			print "Nicht ganz, versuchen sie es noch einmal."
			print
	else:
		print "Zwischen Minimal und Maximal !"