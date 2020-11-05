# Să se calculeze sumele:
#         	s1=1+2+3+…+n
			#s2=1*2+2*3+3*4+…+(n-1)*n
			#s3=1+1*2+1*2*3+…+1*2*3*…*n
			#s4=12+22+32+…+n2
			#s5=1/2+2/3+3/4+…+n/(n+1)
			#s6=1+2+22+23+24+…+2n
			#Notă: Pentru fiecare sumă n – se va citi de la tastatură.

n=int(input('Dati n = '))
stop=n+1
stop2=(n*2)+1
s1=0
s2=0
s3=0
p1=1
s4=0
s5=0
s6=0
for i in range(1,stop):
    s1=s1+i
print ('S1= ',s1)
for j in range(1,stop):
	s2=s2+((j-1)*j)
print ('S2= ',s2)
for m in range(1,stop):
	p1=p1*m
	s3=s3+p1
print ('S3= ',s3)
for a in range(1,stop):
	s4=s4+((a*10)+2)
print ('S4= ',s4)
for t in range(1,stop):
	s5=s5+(t/(t+1))
print ('S5= ',s5)
for u in range(1,stop2):
	s6=s6+((u*10)+u)
print ('S6= ',s6)





