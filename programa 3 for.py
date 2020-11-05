#Utilizînd ciclul FOR elaboraţi 
# un program care afişează toate numerele pare, 
# pentru intervalul de la 1 la n
#  (n-este citit de la tastatură).
n=int(input('Dati n = '))
stop=n+1
for i in range(2,stop,2):
    print (i,end=' ')
