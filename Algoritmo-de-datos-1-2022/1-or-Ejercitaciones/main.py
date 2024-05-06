from algo1 import *
from funcion import *
#Ingreso de valores enteros y reales...
print("Ingres valores enteros y reales")
a=input_int("Ingrese valor entero: ")
print("Valor Ingresado ",a)
b=input_real("Ingrese valor real: ")
print("Valor Ingresado ",b)
c=a+b
print("Sumatoria de ambos ",c)
#Escriba un programa que sea capaz de sumar los números impares del 1 al 99 inclusive
print()
print("Suma de numeros impares del 1 al 99")
Suma_imp=0
Suma_par=0
for n in range(1,100):
	if n%2==0 :
		Suma_par=Suma_par+n
	else:
		Suma_imp=Suma_imp+n
print("El total de la Suma Impares ",Suma_imp)
print("El total de la Suma Pares ",Suma_par)
print("Suma Total ",Suma_imp+Suma_par)
# Escriba un programa que permita ingresar los límites enteros 
# de un rango de valores y calcule el promedio de los mismos mediante una función
print()
valor_1=input_int("Ingrese valor desde: ")
valor_2=input_int("ingrese valor hasta: ")
print("El promedio es ",promedio_media(valor_1,valor_2))
#----------------------------------------------------------
print()
print("Ingrese dos valores enteros")
Entero_1=input_int(": ")
Entero_2=input_int(": ")
Suma=Entero_1+Entero_2
if Suma>50:
	resta_5(Suma)
elif Suma<=50:
	resta_2(Suma)
#----------------------------------------------------------
print()
print("Ingrese tres valores reales")
Entero_1=input_real(": ")
Entero_2=input_real(": ")
Entero_3=input_real(": ")
print("el orden es:")
promedio=orden(Entero_1,Entero_2,Entero_3)
print ("el promedioes")
print (promedio)
print("Fin")