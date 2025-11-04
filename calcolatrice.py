#inizio codice
print ("quiz matematica")
nome_utilizzatore=input("inserisci il tuo nome")
print ("Benvenuto!"+(nome_utilizzatore)+ (" Nella calcolatrice di Alebot"))
primo_dato=float(input("inserisci il primo numero"))
secondo_dato=float(input("inserisci il secondo numero"))
print ("addizione=1  Sottrazione=2  Moltiplicazione=3 Divisione=4")
operatore=input("inserisci il simbolo che vuoi utilizzare:")
if (operatore=="1"):
    print (primo_dato+secondo_dato)
elif (operatore=="2"):
    print (primo_dato-secondo_dato)
elif (operatore=="3"):
    print (primo_dato*secondo_dato)
elif (operatore=="4"):
    print (primo_dato/secondo_dato)