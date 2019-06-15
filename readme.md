# Software utilizzato
* **Python** 3.7
* **Visual Studio Code**, per l'implementazione del codice Python
* **LibreOffice**, per la visione dei file .csv
* **GitHub**, per la sincronizzazione del codice

# Abstract 
La nostra idea di progetto è quella di realizzare un modello unificato di dati che permetta di riunire in un unico posto i sinistri stradali che sono avvenuti in Italia in un determinato anno. Tale modello è pensato prendendo come riferimento quattro città, ciascuna delle quali situata in una zona diversa di Italia, da Nord, al Centro, al Sud fino alle isole, confrontando la struttura di ciascun dataset e unendoli in un unico modello che li rappresenti tutti  seguendo la medesima struttura.
Ad una prima analisi molti portali comunali di open data in Italia pubblicano dati sugli incidenti stradali nei vari anni, ma le tabelle presentano discordanze, il che  non le rende immediatamente compatibili.
Il nostro modello conterrà le informazioni principali di dove e come è avvenuto il sinistro, ovvero: 
* città;
* data e ora;
* luogo;
* numero di persone coinvolte suddivise in: illesi, feriti, prognosi riservata e deceduti;
* coordinate;
* dinamica dell’incidente.

Una volta implementato, questo modello potrà essere preso come riferimento dai comuni per la pubblicazione dei dati e per l’unificazione con i dati distribuiti da altri comuni, con la possibilità di creare un unico database nazionale, facilmente consultabile e accessibile.
Un possibile utilizzo del nostro modello può essere quello di rappresentare i dati su una mappa interattiva utilizzando le coordinate contenute nel modello, con la possibilità anche di filtrare i risultati secondo diversi criteri.

*Per problemi di disponibilità di dataset aggiornati, alcuni modelli si riferiscono all'anno 2017, altri all'anno 2018.*


Our idea for this project is that of realize an unified model which allows to unify in a single file, all the accidents occured in Italy in a certain year. Such model is imagined taking into account four city, every each of them located on different zone of Italy, from North, to Center, to South and the islands, comparing the structure of each of those datasets and merging them into one unified model which represent them all, following the same structure .
At a first look these portals report informations of accidents in many year, but the tables present discrepancies, which does not make them immediately compatible.
Our model will contain informations about where and how the accident occurred:
* City;
* Date and hour;
* Location;
* Number of people involved: unharmed, hurt, reserved prognosis and deceased;
* Coordinates;
* Dynamic of the accident;

Once implemented, this model could be use as reference by the municipalites for the publication of data and merging of those data with other from other municipalities, with the possibility  of creating a unified database on national level, easily consultable and accessible. Another possible use of this model is the representation of data through an interactive map, using coordinates stored in model, which gave the possibilities to filter the result following determined criteria.

*Due to availability problem of updated datasets, some models refers to 2017, others to 2018.*

# 1. Raccolta dati
* palermo.csv (http://opendata.comune.palermo.it)
  * Licenza CC BY-SA 4.0
* matera.csv (http://dati.comune.matera.it)
  * Licenza CC BY 4.0
* bergamo.csv (http://dati.lombardia.it)
  * Licenza IODL 2.0
* *2018.json (http://dati.comune.roma.it)
  * Licenza CC BY 4.0
  * Dati divisi mese per mese
  
# 2. Elaborazione dei dati
* Input -> palermo.csv / Output -> newPalermo.csv
  * Luogo: Ci interessa prendere solo la via e non altri dati come il numero civico. Alcune vie non sono indicate e da un primo confronto contengono coordinate errate, decidiamo quindi di eliminarle
  * Data: Alcune date sono in formato *dd/mm/yyyy*, la maggior parte in formato *yyyy-mm-dd*. Decidiamo di convertire tutto nel formato più utilizzato nel documento, ovvero *yyyy-mm-dd*

* Input -> matera.csv / Output -> newMatera.csv
  * Data: Le date sono scritte nel formato *giorno dd mese yyyy*. Decidiamo di convertire tutto nel formato *yyyy-mm-dd*
  * Ora: Gli orari sono scritti nel formato *hh,mm*. Decidiamo di convertire tutto nel formato *hh:mm*
  * Illesi e Riservata: Nel file di origine non sono indicati il numero di persone illese e il numero di persone in prognosi riservata, non riuscendo a risalire a questi numeri nemmeno mediante l'utilizzo dei dati nelle altre colonne, decidiamo di assegnare a queste due colonne valore 0.

* Input -> bergamo.csv / Output -> newBergamo.csv
  * Data: le date sono scritte nel formato *dd-mm-yyyy*. Si converte il tutto nel formato *yyyy-mm-dd* 
  * Città:La riga contenente la località presenta sia la città che la via dove è avvenuto il sinistro, queste due informazioni sono state "separate" rimpiazzando la città con uno spazio vuoto e specificando la città all'inizio di ogni riga durante la scrittura
  *Il nome della città è specificato all'inizio della funzione "writerow" come stringa.
  
* Input->nomeMese2018.json / Output ->newRoma.csv
   * Data : la data è scritta nel formato corretto ma ad essa è affiancata anche l'ora, viene perciò eseguito lo splitting di queste due informazioni, prendendo come punto di split lo spazio vuoto tra loro.
   * Coordinate: latitudine e longitudine vengono concatenate in un unica variabile chiamata "coordinate".
   
   * Input->merger.py / Output -> sinistri2018.csv
   
   
  
