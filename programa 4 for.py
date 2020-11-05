#Utilizînd ciclul FOR elaboraţi un program care 
# afişează toate numerele impare, pentru intervalul 
# de la a la b (a și b se citesc de la tastatură).
a=int(input('Dati a = '))
b=int(input('Dati b = '))
start=a
stop=b+1
for i in range(start,stop):
    if (i%2!=0):
        print (i,end=' ')

