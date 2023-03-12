# Programa que permite obtener las coordenadas de una circuferencia 

print("---------------------------------------------")
print("-------------Coordenadas (x,y)---------------")
print("---------------------------------------------")

# Input

import math
radio=int(input("Dígite el valor del radio: "))
n=int(input("Dígite en cuantas partes quieres dividir el sector circular: "))
decimas=int(input("Ingrese el número de decimales máximo que quieres ver: "))
print("---------------------------------------------")
print("("+str(radio)+",0)")
angulo=math.pi/2/n
a=1
b=1
c=1
e=1

# Processing y output

while n!=a:
    contador=angulo*a
    a=a+1
    y=round(math.sin(contador)*radio,decimas)
    x=round(math.cos(contador)*radio,decimas)
    print("("+str(x)+","+str(y)+")")

print("(0,"+str(radio)+")")  

while n!=b:
    contador=angulo*b
    b=b+1
    y=round(math.sin(contador)*radio,decimas)
    x=round(math.cos(contador)*radio,decimas)
    x=x*-1
    print("("+str(x)+","+str(y)+")")

print("("+str(radio*-1)+",0)")

while n!=c:
    contador=angulo*c
    c=c+1
    y=round(math.sin(contador)*radio,decimas)
    x=round(math.cos(contador)*radio,decimas)
    x=x*-1
    y=y*-1
    print("("+str(x)+","+str(y)+")")

print("(0,"+str(radio*-1)+")")

while n!=e:
    contador=angulo*e
    e=e+1
    y=round(math.sin(contador)*radio,decimas)
    x=round(math.cos(contador)*radio,decimas)
    y=y*-1
    print("("+str(x)+","+str(y)+")")