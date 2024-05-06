from set import *
Arreglo_A=Array (5,0)
Arreglo_A[0]=1
Arreglo_A[1]=None
Arreglo_A[2]=7
Arreglo_A[3]=None
Arreglo_A[4]=9
print("A: ",Arreglo_A)
print("Create Set")
Arreglo_A=Create_Set(Arreglo_A)
print(Arreglo_A)
Arreglo_B=Array (5,0)
Arreglo_B[0]=1
Arreglo_B[1]=3
Arreglo_B[2]=4
Arreglo_B[3]=5
Arreglo_B[4]=1
print("B: ",Arreglo_B)
print("Union A U B")
Arreglo_C= Union(Arreglo_A,Arreglo_B)
print(Arreglo_C)
print("Interseccion A Int B")
Arreglo_D= Intersection(Arreglo_A,Arreglo_B)
print(Arreglo_D)
print("Diferencia A/B")
Arreglo_E=Difference(Arreglo_A,Arreglo_B)
print(Arreglo_E)

