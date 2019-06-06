# Software utilizzato
* **Python** 3.7
* **Visual Studio Code**, per l'implementazione del codice Python
* **LibreOffice**, per la visione dei file .csv
* **GitHub**, per la sincronizzazione del codice

# Abstract 
*La nostra idea di progetto è quella di realizzare una mappa interattiva che mostra dove sono avvenuti i sinistri nella zona di palermo nel 2018 ed, eventualmente, avere la possibilità di filtrare i risultati ottenuti per via, tipologia, giorno della settimana, ecc.... Verranno utilizzati anche i dati relativi al meteo per dare una visione più chiara delle zone che sono più 'pericolose' durante il maltempo, in modo tale da assegnare alla zona a rischio incidente un "indice di pericolosità" maggiore.

*This project is based on the idea of creating an interactive map that shows where the incident occurred in all Palermo in 2018 and, eventually, having the chance of filtering those results in address, tipology, day of the week and so on. We'll also use data concerning the weather in which those accident occured so that the user can have a clearer view of which zone is 'more dangerous' during a bad weather, it has also the purpose of assigning to those zones an "index of danger" higher than it would usually be. 

# 1. Raccolta dati
* sinistri2018.csv (http://opendata.comune.palermo.it)
  * Licenza CC BY-SA 4.0
* Dati meteo mese per mese (http://ilmeteo.it)
  * Licenza ...
  
  
**Note**: impossibile da scaricare con rete università perché riconosciuta come rete professionale.

# 2. Processamento dei dati
* Input -> sinistri.csv / Output -> newSinistri.csv
  * Luogo: Ci interessa prendere solo la via e non altri dati come il numero civico. Alcune vie non sono indicate e da un primo confronto contengono coordinate errate, decidiamo quindi di eliminarle
  * Data: Alcune date sono in formato *dd/mm/yyyy*, la maggior parte in formato *yyyy-mm-dd*. Decidiamo di convertire tutto nel formato più utilizzato nel documento, ovvero *yyyy-mm-dd*


* Input -> Palermo-2018-*.csv / Output -> 2018-\*.csv
  * Data: Le date sono scritte nel formato *dd/mm/yyyy*. Decidiamo di convertire tutto nel formato utilizzato dal documento newSinistri.csv, *yyyy-mm-dd*
  * Fenomeno: La colonna è scritta con spazi superflui che eliminiamo. Sostituiamo i fenomeni del tipo "piogga temporale" con "temporale"

* Input -> 2018-*.csv / Output -> datiMeteo2018.csv
  * Vengono uniti tutti i file csv riguardanti le condizioni meteo mese per mese in un unico file
