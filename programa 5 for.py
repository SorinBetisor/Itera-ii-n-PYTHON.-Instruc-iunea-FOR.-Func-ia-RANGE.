#Utilizînd ciclul FOR elaboraţi un program care
#  să calculeze suma numerelor de la 1 la n, 
# care se împart la 3 şi 5 pentru oricare n întrodus de la tastatură.
n=int(input('Dati n = '))
stop=n+1
for i in range(1,stop):
    if ((i%3==0) and (i%5==0)):
        print (i,end= ' ')