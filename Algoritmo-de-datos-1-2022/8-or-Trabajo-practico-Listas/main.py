from LinkedList import *
from Conjuntos import *
from Empleado import *
from Inversa import *

#A) 24, 45, 3, 67, 89, 345, 54, 22, 3, 678
#B) 46, 34, 64, 59, 12, 15, 234, 567, 12, 33
A=LinkedList()
add(A,678)
add(A,3)
add(A,22)
add(A,54)
add(A,345)
add(A,89)
add(A,67)
add(A,3)
add(A,45)
add(A,24)
B=LinkedList()
add(B,33)
add(B,12)
add(B,567)
add(B,234)
add(B,15)
add(B,12)
add(B,59)
add(B,64)
add(B,34)
add(B,46)
print("A:")
print_L(A)
print("B:")
print_L(B)
C=LinkedList()
Intercalar(C,A,B)
print("C: A y B intercalando")
print_L(C)
print("C: C - pares de A")
Diferencia_Pares(C,A)
print_L(C)
print("D: Lista impares de C  ")
D=LinkedList()
Lista_impares(D,C)
print_L(D)
print("A: Set(A) U  50<B<100  ")
union_conjuntos(A,B)
print_L(A)
#-----------------------------------------------
print()
print("	A:Lista invertida")
reverse(A)
print_L(A)
#-----------------------------------------------
print()
E=LinkedList()
Add(E,'Luis Esteban  ', 32, 7)
Add(E,'Eduardo Ángel ', 34, 2)
Add(E,'Pedro César   ', 45, 8)
Add(E,'Luis Esteban  ', 32, 7)
Add(E,'Pedro Augusto ', 40, 9)
Add(E,'Juan Carlos   ', 23, 5)
Add(E,'Luis Esteban  ', 32, 7)
Add(E,'Juan Carlos   ', 23, 5)
Add(E,'Eduardo Ángel ', 34, 2)
print_E(E)
print()
print("	Set(E).........")
Set_LG(E)
print_E(E)
print()
print("	Insertar_Legajo(L,Ernesto Andrés, 55, 6)")
print()
insert_File(E,'Ernesto Andrés', 55, 6)
print_E(E)
print()

print("	Permutar legajo 9 <=> 8 ")
Move(E,9,8)
print_E(E)