#Autor Ruddy Blehisner Choqueribe Huanca
a=int(input("Ingrese a "))
b=int(input("Ingrese b "))
c=int(input("Ingrese c "))
d=(b*b)-(4*a*c)
if d>0:
    print("la naturaleza de sus raices son reales y distintas")
else:
    if d < 0:
        print("la naturaleza de sus raices son complejas o conjugadas")
    else:
        print("la naturaleza de sus raices son reales e iguales")
