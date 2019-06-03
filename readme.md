# 0. Software utilizzato
* Python ver.3.7
* Visual Studio Code, per l'implementazione del codice Python
* LibreOffice, per la visione dei file .csv
* GitHub, per la sincronizzazione del codice

# 1. Raccolta dati
* sinistri2018.csv (http://opendata.comune.palermo.it)
  * Licenza CC BY-SA 4.0
* Dati meteo mese per mese (http://ilmeteo.it)
  * Licenza ...
  
  
**Note**: impossibile da scaricare con rete università perché riconosciuta come rete professionale.

# 2. Processamento dei dati
* Input -> sinistri.csv / Output -> newSinistri.csv
  * Luogo: Ci interessa prendere solo la via e non altri dati come il numero civico
  * Data: Alcune date sono in formato *dd/mm/yyyy*, la maggior parte in formato *yyyy-mm-dd*. Decidiamo di convertire tutto nel formato più utilizzato nel documento, ovvero *yyyy-mm-dd*
