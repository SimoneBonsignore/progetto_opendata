import os

print("#################################################")
print("##            Aggiorno i dataset               ##")
print("#################################################")

#Esegue sequenzialmente i seguenti script
os.system("python3 newMatera.py; python3 newPalermo.py; python3 newBergamo.py; python3 newRoma.py; python3 merger.py")

print("#################################################")
print("##            Dataset aggiornati               ##")
print("#################################################")

print("\n\n")

print("#################################################")
print("##            Creo ontologia                   ##")
print("#################################################")

os.system("python data_processer.py")

print("#################################################")
print("##                   FINE                      ##")
print("#################################################")
print("\n\n\n")