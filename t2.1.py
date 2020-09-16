#Autor Ruddy Blehisner Choqueribe Huanca
a=int(input("Ingrese horas "))
b=int(input("Ingrese minutos "))
c=int(input("Ingrese segundos "))
c=c+1
if c >= 60:
    c=0
    b=b+1
    if b >=60:
        b=0
        a=a+1
print (a,":",b,":",c)
