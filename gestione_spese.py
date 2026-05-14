# --- Importazione dei moduli necessari e costanti ---

# csv per leggere e scrivere file csv
import csv

# datetime per validare e gestire le date
from datetime import datetime


# Nome del file csv in cui verranno salvate tutte le transazioni
FILE_CSV = "spese.csv"


MESI = {
    1: "Gennaio", 2: "Febbraio", 3: "Marzo", 4: "Aprile",
    5: "Maggio", 6: "Giugno", 7: "Luglio", 8: "Agosto",
    9: "Settembre", 10: "Ottobre", 11: "Novembre", 12: "Dicembre"
}




def aggiungi_transazione() -> None:

    """ Funzione che aggiunge una transazione """

    print("\n--- Aggiungi una transazione ---")



    # --- Validazione data ---

    #Ciclo per richiedere la data finchè non è valida

    while True:
        data_input = input("Inserisci la data (GG/MM/AAAA) oppure 'q' per annullare: ").strip()
        if data_input.lower() == "q":
          print("Operazione annullata.")
          return

        # Verifica che la data sia valida
        try:

          # prova a convertire la stringa in un oggetto datetime
          data = datetime.strptime(data_input, "%d/%m/%Y")

          # controlla se la data è futura
          if data > datetime.today():
                print("La data inserita è futura. Riprova con una data valida.")
                continue  # richiede una data valida all'utente

          break  # esce dal ciclo quando la data è valida

        except ValueError:
          # l'utente ha inserito una data in formato errato
          print("Formato data non valido. Usa GG/MM/AAAA.")



    # --- Validazione descrizione ---

    #Ciclo per richiedere la descrizione finchè non è valida

    while True:
        descrizione = input("Inserisci la descrizione oppure 'q' per annullare: ").strip()

        if descrizione.lower() == "q":
          print("Operazione annullata.")
          return


        # Verifica che la descrizione non sia vuota

        if descrizione == "":
            print("La descrizione non può essere vuota. Riprova.")
            continue  # richiede una descrizione all'utente

        break  #e sce dal ciclo quando la descrizione è valida



    # --- Validazione importo ---

    #Ciclo per richiedere l'importo finchè non è valido

    while True:
        importo_input = input("Inserisci l'importo oppure 'q' per annullare: ").strip()
        if importo_input.lower() == "q":
          print("Operazione annullata.")
          return


        # Verifica che l'importo sia valido
        try:

            # prova a convertire l'importo in float
            importo = float(importo_input)

            # controlla importo negativo o pari a 0
            if importo <= 0:
                print("L'importo deve essere un valore positivo. Riprova.")
                continue # richiede un importo valido all'utente

            break  # esce dal ciclo quando l'importo è valido"

        except ValueError:
            # l'utente ha inserito un importo non valido
            print("Importo non valido. Riprova inserendo un numero.")


    # --- Scrittura su CSV ---

    with open(FILE_CSV, "a", newline="", encoding="utf-8") as file:
        #scrive la transazione nel file csv
        writer = csv.writer(file)
        writer.writerow([data_input, descrizione, importo])

    print(" Transazione aggiunta correttamente!")




def report_mensile() -> None:

    """ Funzione che crea il report mensile """

    print("\n--- Report Mensile ---")



    try:
        with open(FILE_CSV, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            # converte il reader in lista
            spese = list(reader)

    except FileNotFoundError:
        # se il file non esiste ancora notifica all'utente nessuna spesa registrata
        print("Nessuna spesa registrata. Il file CSV non esiste ancora.")
        return

    #crea un dizionario vuoto che verrà usato per sommare tutte le spese per mese
    report = {}

    # scorre tutte le righe del CSV
    for riga in spese:

        data_str, descrizione, importo_str = riga

        # converte la data in un oggetto datetime
        data = datetime.strptime(data_str, "%d/%m/%Y")

        # crea una chiave nel formato "YYYY-MM"
        chiave = f"{MESI[data.month]} {data.year}"

        # converte l'importo in float per poterlo sommare
        importo = float(importo_str)

        # se un mese non è ancora presente nnel dizionario, lo inizializza a zero
        # questo evita errori quando porva a sommare un importo a una chiave insesistente
        if not chiave in report:
            report[chiave] = 0

        # somma l'importo al totale del mese corrispondente
        report[chiave] += importo

    # Stampa il report ordinato per mese
    print("\nSpese per mese:")

    # ordina le coppie chiave valore in ordine crescente di chiavi
    for mese, totale in sorted(report.items()):

        # stanmpa il mese e il totale formattato con due decimali
        print(f"{mese} {totale:.2f}")



def top_10_transazioni() -> None:

    """ Funzione che crea la TOP 10 delle transazioni più alte """

    print("\n--- Top 10 Transazioni ---")


    try:

        with open(FILE_CSV, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            # lista che conterrà solo le transazioni valide
            spese = []

            # ciclo che legge ogni riga del CSV
            for riga in reader:

                # ogni riga deve avere esattamente 3 elementi
                if len(riga) != 3:
                    continue

                data, descrizione, importo_str = riga


                try:
                    importo = float(importo_str)
                except ValueError:
                    continue

                # aggiunge la transazione valida alla lista
                spese.append((data, descrizione, importo))

    except FileNotFoundError:
        print("Nessuna spesa registrata. Il file CSV non esiste ancora.")
        return

    # se non ci sono transazioni informa l'utente
    if not spese:
        print("Non ci sono transazioni da mostrare.")
        return

    # ordina la lista delle spese per importo decrescente
    spese_ordinate = sorted(spese, key=lambda x: x[2], reverse=True)

    #Stampa solo le prime 10 transazioni
    print("\nLe 10 spese più alte:")
    for data, descrizione, importo in spese_ordinate[:10]:
        print(f"{data} {descrizione} {importo:.2f} €")




def mostra_menu()-> None:

    """ Funzione che mostra le opzioni del menu all'utente """

    print("\nGESTORE DELLE SPESE DOMESTICHE\n")
    print("[1] Aggiungi una transazione")
    print("[2] Report mensile")
    print("[3] Top 10 transazioni")
    print("[0] Esci")



def main() -> None:

    """ Funzione che gestisce il flusso principale del programma """

    print("Benvenuto/a nel gestore delle spese domestiche!")

    # Ciclo infinito finchè l'utente non sceglie di uscire
    while True:

      mostra_menu()

      #l'utente sceglie un'opzione
      scelta = input("\nSeleziona un'opzione: ")

      if scelta == "1":
        # richiama la funzione per aggiungere una transazione
        aggiungi_transazione()

      elif scelta == "2":
        # richiama la funzione per il report
        report_mensile()

      elif scelta == "3":
        # richiama la funzione per la top 10 transazioni
        top_10_transazioni()

      elif scelta == "0":
        # esce dal programma
        print("Uscita dal programma.")
        break

      else:
            # gestisce scelte non valide
            print("Scelta non valida. Riprova.")




# --- Avvio del programma ---
main()

