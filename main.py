import random
# Legge le righe del file e le memorizza in una lista
with open("domande.txt", "r", encoding="utf-8") as file:
    righe = file.readlines()  # Lista con tutte le righe

# Rimuove eventuali newline alla fine di ogni riga
righe = [riga.strip() for riga in righe]
print("ciao")
dizionario = {}

for i in range(0, len(righe), 7):  # Cambia step a seconda del file
    chiave = righe[i]
    valori = righe[i + 1:i + 6] if i + 1 < len(righe) else []  # Prendi 2 valori successivi
    dizionario[chiave] = valori

print(dizionario)

class Domanda:
    def __init__(self, testo, livello, rispCorretta, risposte):
        self.testo = testo
        self.livello = livello
        self.rispCorretta = rispCorretta
        self.risposte = risposte

domandeTotali = []
domandeScelte = []

for chiave, valori in dizionario.items():
    risposte = [valori[1], valori[2], valori[3], valori[4]]
    d = Domanda(chiave, valori[0], valori[1], risposte)
    domandeTotali.append(d)

def mescola_e_estrai(domande):
    random.shuffle(domande)  # Mescola la lista in modo casuale
    return domande[0] if domande else None  # Ritorna la prima domanda (o None se lista vuota)

def mescola_risposte(domanda):
    risposte_casuali = domanda.risposte[:]  # Copia della lista per non modificarla direttamente
    random.shuffle(risposte_casuali)  # Mescola la copia della lista
    return risposte_casuali

def cercaDomande(domandeTotali, nLivello):
    for element in domandeTotali:
        if int(element.livello) == nLivello:
            domandeScelte.append(element)
    return domandeScelte

def Giochiamo(nLivello):
    corretto = False
    domandeScelte = cercaDomande(domandeTotali, nLivello)
    d1 = mescola_e_estrai(domandeScelte)
    r1 = mescola_risposte(d1)

    print(f"Livello: {nLivello}) {d1.testo}")
    print(f"1. {r1[0]}")
    print(f"2. {r1[1]}")
    print(f"3. {r1[2]}")
    print(f"4. {r1[3]}")
    numero = input("Inserisci la risposta: ")
    if numero == "1" and r1[0] == d1.rispCorretta:
        nLivello += 1
        corretto = True
        print("Risposta corretta!\n")
    if numero == "2" and r1[1] == d1.rispCorretta:
        nLivello += 1
        corretto = True
        print("Risposta corretta!\n")
    if numero == "3" and r1[2] == d1.rispCorretta:
        nLivello += 1
        corretto = True
        print("Risposta corretta!\n")
    if numero == "4" and r1[3] == d1.rispCorretta:
        nLivello += 1
        corretto = True
        print("Risposta corretta!\n")
    if not corretto or (corretto and nLivello == 5):
        print("Fine dei giochi")
        nick = input("Inserisci il tuo nickname: ")

            # Legge il file e memorizza i dati in una lista
        with open("punti.txt", "r", encoding="utf-8") as file2:
            righe2 = file2.readlines()
        classifica = []
        for riga in righe2:
            dati = riga.strip().split()
            if len(dati) == 2:  # Assicura che ci sia un nome e un punteggio
                nome, punteggio = dati[0], int(dati[1])
                classifica.append((nome, punteggio))

        # Aggiunge il nuovo giocatore alla classifica
        classifica.append((nick, nLivello))

        # Ordina la classifica in base al punteggio in ordine decrescente
        classifica.sort(key=lambda x: x[1], reverse=True)

        # Scrive la classifica aggiornata nel file
        with open("punti.txt", "w", encoding="utf-8") as file3:
            for nome, punteggio in classifica:
                file3.write(f"{nome} {punteggio}\n")

        exit()
    else:
        return nLivello
i = 1
s = 0
while(i>0):
    s = Giochiamo(s)
    domandeScelte = []
    d1 = ""
    r1 = []
