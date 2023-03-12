# Programa que permite obtener las coordenadas de una circuferencia 

print("---------------------------------------------")
print("-------------Coordenadas (x,y)---------------")
print("---------------------------------------------")

# Input

import math
radio=int(input("Dígite el valor del radio: "))
n=int(input("Dígite en cuantas partes quieres dividir el semicirculo: "))
print("("+str(radio)+",0)")
angulo=math.pi/2/n
a=1

# Processing y output

while n!=a:
    contador=angulo*a
    a=a+1
    y=round(math.sin(contador)*radio,3)
    x=round(math.cos(contador)*radio,3)
    print("("+str(x)+","+str(y)+")")

print("(0,"+str(radio)+")")   