from funciones import *
print("Las Longitudes de un Vector seran de 0*m")
print("Las Longotudes de una Matriz seran de m*n")
print("--------------------------------------")
print("Elemento mayor:")
print ("Vector A: Longitud")
m=input_int("m: ")
print("R:Aleatorio / M:Manual ")
Aleatorio=input_str(">: ")
vector_A=vector(m,Aleatorio)
print(vector_A)
print("Mayor ",greatest_element(vector_A))
print()
print("Operacion Suma: A+B ")
print ("Vector B: Longitud")
m=input_int("m: ")
vector_B=vector(m,'R')
print(vector_B)
vector_C=add_vectors(vector_A,vector_B)
print("A+B = C : ",vector_C)
print("Operacion Norma cuadratica C")
print(quadratic_norm(vector_C))
print()
print("Operacion Producto: D*A")
print("Matriz D: Dimencion")
m=input_int("m:")
n=input_int("n:")
print("R:Aleatorio / M:Manual ")
Aleatorio=input_str("> ")
Matriz_D=Matrix(m,n,Aleatorio)
for i in range (0,m):
	print(Matriz_D[i])
vector_C=multiply(vector_A,Matriz_D)
print("D*A = C :",vector_C)
print()
print("Operacion Diferencia: D-E")
print("Matriz E: Dimencion")
m=input_int("m: ")
n=input_int("n: ")
Matriz_E=Matrix(m,n,'R')
print()
for i in range (0,m):
	print(Matriz_E[i])
Matriz_F=Difference(Matriz_D,Matriz_E)
if Matriz_F!=None:
	print("D-E:")
	for n in range(0,m):
		print(Matriz_F[n])
print()
print("D : Triangular inferio")
x=Triangle_Lower(Matriz_D)
print("Su deternimante es: ",x)
print("--------------------------------------")
print ("Adicionales ")
print("producto escalar de Dos Vecotes A*B")
print(Scalar_product(vector_A,vector_B))

print("Producto de dos matrices D*E=G")
Matriz_G =Product_Matrix(Matriz_D,Matriz_E)
if Matriz_G!=None:
	for n in range(0,len(Matriz_G)):
		print(Matriz_G[n])
print("Es diagonal dominante por Filas")
Matriz_H=Dominant_Matrix(Matriz_G)
print("Es matriz G triangular inferior ")
Matriz_H=Top_Triangle(Matriz_G)
print("Su transpuesta es")
for n in range(0,len(Matriz_H)):
	print(Matriz_H[n])
