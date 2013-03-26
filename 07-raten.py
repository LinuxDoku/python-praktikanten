import random

print "======================="
print "===== ZAHLENRATEN ====="
print "======================="
print

gewonnen = False
bereich_start = 0
bereich_ende = 5
bereich = range(bereich_start, bereich_ende)
zahl = random.randint(bereich_start, bereich_ende)
versuche = 0

print "Sie suchen eine Zahl zwischen %d und %d. Viel Spass" % (bereich_start, bereich_ende)
print

while gewonnen is False:
	eingabe = input("Raten Sie: ")
	versuche += 1
	if zahl is eingabe:
		print "Yay, Sie haben gewonnen!"
		print "Sie haben %d Versuche gebraucht" % versuche
		print
		gewonnen = True
	elif eingabe < bereich_start or eingabe > bereich_ende:
		print "Sie muessen eine Zahl zwischen %d und %d eingeben" % (bereich_start, bereich_ende)
		print
	else:
		print "Versuchen Sie es noch einmal!"
		print