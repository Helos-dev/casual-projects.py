from turtledemo.clock import datum

#variabili
nome_assistente=("AleBot")
Drink_Speciale=("DigitalVodka")
Prezzo_Drink= 5.5

#Inizio Codice
nome_cliente=input("inserisci il tuo nome")
print ("benvenuto "+(nome_cliente)+(" al pub drink&programmazione"))
print ("salve sono Alebot oggi sono qui per assisterla :)")
print ("il nostro drink piu famoso e: "+str (Drink_Speciale))
print ("alla modica cifra di: " +str (Prezzo_Drink))
print ("\ninserisci il tuo anno di nascita")
dati_cliente=int(input())
anni_cliente= 2025-dati_cliente
print ("hai "+str(anni_cliente)+" anni")
if anni_cliente<18:
    print ("sei minorenne puoi ordinare solo analcolici")

elif anni_cliente>80:
    print ("non sarebbe meglio una briscola?")
else:
    print("sei maggiorenne puoi ordinare alcolici e analcolici")
alcolici = ["Mojito" , "White Russian" , "Caipirinha"]
alcolici.append("Daiquiri")
alcolici.insert(0, "Martini")
print ("ecco gli alcolici disponibili:")
for alcolico in alcolici:
    print(alcolico)
analcolici=["Limonata","Gazosa"]
for analcolico in analcolici:
    print(analcolico)
