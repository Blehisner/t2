#Autor Ruddy Blehisner Choqueribe Huanca
a=int(input("Ingrese tiempo disponible: "))
b=int(input("Ingrese tiempo necesario: "))
h=b-int((b/100))*100
b=int(b/100)
h=h*3600
m=b-int((b/100))*100
b=int(b/100)
m=m*60
sum=b+m+h
print(sum)
if sum>=a:
    print("El trabajo no puede realizarse")
else:
    print("El trabajo puede realizarse")
