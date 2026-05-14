# Gestore delle Spese Domestiche in Python

Progetto Python per registrare spese, generare report mensili e visualizzare le 10 transazioni più alte, sviluppato durante il Master in Data Engineering per consolidare le competenze di programmazione in Python.

## Funzionalità principali

- Aggiunta di nuove transazioni (data, descrizione, importo)
- Validazione degli input
- Report mensile delle spese
- Top 10 delle transazioni con importo più alto

## Tecnologie

- Python 3
- Modulo `csv`
- Modulo `datetime`

## Esecuzione

Clonare il repository o scaricare il file `gestione_spese.py` e avviare:

```bash
python gestione_spese.py
```

---

## Traccia del progetto

### Contesto del Progetto
In un'epoca in cui il controllo delle spese personali e familiari è diventato cruciale per una gestione finanziaria sostenibile, un'applicazione semplice ma efficace può rappresentare un importante valore aggiunto per i consumatori. Il progetto di un gestore delle spese domestiche mira a fornire uno strumento utile e immediato per il monitoraggio delle transazioni economiche quotidiane, con un'interfaccia utente chiara e funzionale.

### Obiettivo del Progetto
L'obiettivo è sviluppare un'applicazione in Python che consenta agli utenti di tracciare le loro spese, generare report mensili e identificare le spese più significative. Questo strumento fornirà una panoramica finanziaria trasparente, aiutando gli utenti a prendere decisioni consapevoli per migliorare la gestione del budget familiare.

### Funzionalità Chiave
- Aggiunta di una transazione: Gli utenti possono registrare facilmente ogni spesa, completando campi come data, descrizione e importo.

- Report Mensile: Generazione di un resoconto mensile che raggruppa le spese per anno e mese, fornendo una chiara visione delle transazioni effettuate nel periodo.

- Top 10 Transazioni: Visualizzazione delle 10 spese più importanti, utile per monitorare le voci di spesa più rilevanti.

### Valore Aggiunto
L'applicazione offre diversi benefici agli utenti:

- Monitoraggio immediato: Ogni transazione viene registrata in un file CSV, consentendo di tenere traccia in tempo reale delle spese quotidiane.
- Gestione consapevole del budget: Il report mensile fornisce una visione aggregata delle spese, aiutando l'utente a comprendere meglio come e dove vengono spesi i propri soldi.
- Identificazione delle spese principali: La funzione "Top 10" consente di individuare velocemente le spese di maggior impatto economico, favorendo il risparmio e una gestione più oculata delle finanze personali.

### Descrizione delle Funzionalità 
Menu delle Operazioni
L'applicazione presenta un menu interattivo che offre all'utente tre opzioni principali:

[1] Aggiungi una transazione: L'utente può registrare una nuova spesa fornendo data, descrizione e importo. I dati vengono salvati in un file CSV, che funge da registro delle spese.

[2] Report Mensile: Questa opzione genera un resoconto totale delle transazioni, raggruppate per anno e mese, permettendo all'utente di avere un quadro complessivo delle spese nel corso del tempo.

[3] Top 10 Transazioni: L'utente può visualizzare le dieci spese più alte, ordinate per importo, ottenendo così informazioni utili su quali siano state le transazioni di maggior impatto economico.

### Dettaglio delle Operazioni
- Aggiunta di una Transazione:

L'utente inserisce la data della transazione (formato GG/MM/AAAA), una breve descrizione e l'importo totale.
Il dato immesso (es. "18/05/2024 Cena al ristorante 45") viene salvato in un file CSV e l'applicazione ritorna al menu principale.

- Generazione del Report Mensile:

L'utente seleziona questa opzione per visualizzare un riepilogo delle spese suddivise per anno e mese.
Il report viene visualizzato nel seguente formato:
2024-05 324
2024-05 123
2024-06 834
Questo fornisce una visione chiara delle spese nel tempo, agevolando il monitoraggio dei flussi di cassa mensili.

- Top 10 Transazioni:

L'applicazione visualizza le dieci transazioni con l'importo più elevato, includendo data, descrizione e importo. Ad esempio:
18/06/2023 Rata mutuo 1231
15/02/2021 Acquisto scooter 4323
Questa funzionalità aiuta l'utente a identificare le spese maggiori e a monitorare potenziali aree di risparmio.

### Implementazione Tecnica 
L'applicazione sarà realizzata utilizzando Python e i dati saranno gestiti attraverso l'uso di file CSV, garantendo leggerezza e semplicità di utilizzo. La gestione delle operazioni avverrà tramite un menu interattivo che guiderà l'utente attraverso le varie opzioni.

### Commenti e Documentazione 
Il codice Python sarà ampiamente documentato, con commenti chiari che descrivono ogni blocco funzionale. Questo garantirà che sia facile da mantenere e migliorare nel tempo, in linea con gli standard di programmazione appresi durante il corso.

### Conclusione 
L'applicazione di gestione delle spese domestiche offre una soluzione semplice ma potente per il monitoraggio finanziario. Fornirà agli utenti gli strumenti per una gestione più consapevole delle spese e delle entrate, favorendo la trasparenza e l'efficienza nella pianificazione del budget personale o familiare.

---

##  Autrice
Marianna Gaccione — Master in Data Engineering  

