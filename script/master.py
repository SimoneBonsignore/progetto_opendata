import os

print("#################################################")
print("##            Aggiorno i dataset               ##")
print("#################################################")

#Esegue sequenzialmente i seguenti script
os.system("python3 matera.py; python3 palermo.py; python3 bergamo.py; python3 roma.py; python3 merger.py")

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