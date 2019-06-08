# Software utilizzato
* **Python** 3.7
* **Visual Studio Code**, per l'implementazione del codice Python
* **LibreOffice**, per la visione dei file .csv
* **GitHub**, per la sincronizzazione del codice

# Abstract 
* La nostra idea di progetto è quello di creare un modello unico per i sinistri stradali, tale modello è pensato prendendo come riferimento quattro città, ciascuna delle quali situata in una zona divera di Italia, da Nord, al Centro, al Sud e alle isole, confrontando la struttura di ciascuno dataset e unendoli in un unico modello che li rappresenti tutti  seguendo la medesima struttura, si ha la possibilità di filtrare tutti i sinistri  per via, tipologia, giorno della settimana, ecc....
Un ulteriore passo è quello di una mappa interattiva che mostra dove sono avvenuti i sinistri studiati. Per problemi di disponibilità di dataset aggiornati, alcuni modelli si riferiscono all'anno 2017, altri all'anno 2018.

La nostra idea di progetto è quella di realizzare un modello unificato di dati che permetta di riunire in un unico posto i sinistri stradali che sono avvenuti in Italia in un determinato anno.
Ad una prima analisi molti portali comunali di open data in Italia pubblicano dati sugli incidenti stradali nei vari anni, ma le tabelle presentano ....
Il nostro modello conterrà le informazioni principali di dove e come è avvenuto il sinistro, ovvero: 
* città;
* data e ora;
* luogo;
* numero di persone coinvolte suddivise in: illesi, feriti, prognosi riservata e deceduti;
* latitudine e longitudine;
* dinamica dell’incidente.

Una volta implementato, questo modello potrà essere preso come riferimento dai comuni per la pubblicazione dei dati e per l’unificazione con i dati distribuiti da altri comuni, con la possibilità di creare un unico database nazionale, facilmente consultabile e accessibile.
Un possibile utilizzo del nostro modello può essere quello di rappresentare i dati su una mappa interattiva utilizzando le coordinate contenute nel modello, con la possibilità anche di filtrare i risultati secondo diversi criteri.

* The project proposed is based on the idea of creating a unique mode for accidents, this model is studied taking in account four cities, each of which located on different zone of Italy, North,South, Center,islands. We confront the structure for each dataset, mergin them into a single model that represents them all with the same structure , having the chance of filtering them by address, tipology, day of the week and so on. Another step would be an interactive map that shows where those accident occured. Regrettably, the availability of the dataset was not sufficient so we had to use different years, some referring to the 2017 and others 2018. 

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
  * Coordinate: le coordinate sono scritte insieme, separate da una virgola. Vengono separate tramite splitting e scritte separatamente al momento di scrittura del nuovo csv.
  * Città:La riga contenente la località presenta sia la città che la via dove è avvenuto il sinistro, queste due informazioni sono state "separate" rimpiazzando la città con uno spazio vuoto e specificando la città all'inizio di ogni riga durante la scrittura
