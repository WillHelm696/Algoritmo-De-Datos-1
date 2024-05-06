from algo1 import*
from array import *
Array_1=Array(5,0)
Array_1[0]=1
Array_1[1]=2
Array_1[2]=5
Array_1[3]=None
Array_1[4]=3
print("Arreglo:",Array_1)
print("Buscar elemento : 5")
x=search(Array_1,5)
print("> Posisicion :",x)
print("Insertar : 3 , Posicion : 2")
x=insert(Array_1,3,2)
print("> Insertado en posicion :",x)
print("Arreglo:",Array_1)
print("Eliminar elemento : 5")
x=delete(Array_1,5)
print("> Eliminado de la posicion :",x)
print("Arreglo:",Array_1)
print("Elementos Activos del Array")
x=length(Array_1)
print("> Cantidad Activos :",x)