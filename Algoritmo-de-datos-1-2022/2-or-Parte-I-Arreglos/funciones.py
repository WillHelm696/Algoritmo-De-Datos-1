from algo1 import *
import random
import math

def vector(long,Aleatorio): #Ingreso de elementos en Vector
	vector=Array(long,0)
	if Aleatorio=='R':
		for n in range (0,long):
			vector[n]=random.randint(-9,9)
	else:
		print("Ingreso Manual")
		for n in range (0,long):
			vector[n]=input_int("> ")
	return vector
#-------------------------------------------------------------------
def Matrix(m,n,Aleatorio): #Ingreso de elementos en matriz
	Matriz=Array(m,Array(n,0))
	if Aleatorio=='R':
		for j in range (0,m):
			for k in range (0,n):
				Matriz[j][k]=random.randint(-9,9)
	else:
		print("Ingreso Manual")
		for j in range (0,m):
			for k in range (0,n):
				Matriz[j][k]=input_int("> ")
	return Matriz
#-------------------------------------------------------------------
def greatest_element(vector): #Mayor Elemento
	j=len(vector)
	mayor=vector[0]
	for n in range(0,j):
		if mayor < abs(vector[n]):
			mayor=abs(vector[n])
	return mayor
#-------------------------------------------------------------------
def add_vectors(vector_A,vector_B): #  Suma Vector
	if len(vector_A)==len(vector_B):
		m=len(vector_A)
		vector_C=Array(m,0)
		for i in range (0,m):
			vector_C[i]=vector_A[i]+vector_B[i]
		return vector_C
	return"No son de la Misma dimension"
#-------------------------------------------------------------------	
def quadratic_norm(vector):  #Norma cuadratica de un Vector
	if vector=="No son de la Misma dimension":
		return None
	modulo=0
	for n in range (0,len(vector)):
		modulo=modulo+math.pow(vector[n],2)
	modulo=math.sqrt(modulo)
	return modulo
#-------------------------------------------------------------------
def multiply(vector,Matriz): #Multiplicacion de Vector Por Una Matriz
	i=len(vector)
	j=len(Matriz[0])
	if j==i:
		vector_A=Array(len(Matriz),0)
		for n in range (0,len(Matriz)):
			vector_A[n]=0	
			for k in range (0,j):
				vector_A[n]+=vector[k]*Matriz[n][k]
		return vector_A
	return "dimensiones incorrectas"
#-------------------------------------------------------------------	
def Difference(Matriz_A,Matriz_B): #Diferencia de matrizes
	i=len(Matriz_A)
	j=len(Matriz_A[0])
	if i==len(Matriz_B):
		if j==len(Matriz_B[0]):
			Matriz_C=Array(i,Array(j,0))
			for m in range (0,i):
				for n in range (0,j):
					Matriz_C[m][n]=Matriz_A[m][n]-Matriz_B[m][n]
			return Matriz_C
	print("dimensiones incorrectas")
	return None
#-------------------------------------------------------------------
def Triangle_Lower(Matriz): #Matriz Inferior
	i=len(Matriz)
	j=len(Matriz[0])
	Flag=True
	cnt=1
	if i==j:
		for m in range (0,i):
			for n in range(0,j):
				if m<n and Matriz [m][n]!=0:
					Flag=False
				elif m==n:
					cnt=cnt*Matriz [m][n]
		if Flag!=False:
			return cnt
	elif i!=j:
		print("No es Cuadrada")
	else:
		print("No es Triangular inferior")
	return None
#------------------------------------------------------------------
#-------------------------------------------------------------------
def Scalar_product(vector_A,vector_B): #Producto escalar de Vectors
	if len(vector_A)==len(vector_B):
		cnt=0
		for n in range(0,len(vector_A)):
			cnt=cnt+vector_A[n]*vector_B[n]
		return cnt
	else:
		print("dimensiones incorrectas")
	return None
#-------------------------------------------------------------------
def Product_Matrix(Matriz_A,Matriz_B): #Producto de Matrizes
	i=len(Matriz_A[0])
	j=len(Matriz_A)
	h=len(Matriz_B[0])
	k=len(Matriz_B)
	if i==k:
		Matriz_C=Array(j,Array(h,0))
		for z in range(0,h):
			for y in range(0,j):
				Matriz_C[z][y]=0
				for x in range (0,i):
					Matriz_C[z][y]+=Matriz_A[y][x]*Matriz_B[x][z]
		return Transposed(Matriz_C)
	elif i!=k:
		print("No es Posible La Multiplicacion")
	return None

def Dominant_Matrix(Matriz): #Matriz Dominate
	i=len(Matriz)
	j=len(Matriz[0])
	if i==j:
		Flag=True			
		for i in range (0,i):
			cnt=0
			for j in range (0,j):
				if (i != j):
					cnt=cnt+abs(Matriz[i][j])
			if abs(Matriz[i][i])<=cnt:
				Flag=False
	elif i!=j:
		print("No es Cuadrada")
		return None
	elif Flag==True:
		print ("Es una matriz dominante por filas")
	else:
		print("No es una matris dominante por filas")
#-------------------------------------------------------------------
def Transposed(Matriz): # Transpuesta
	i=len(Matriz)
	j=len(Matriz[0])
	Tranpuesta=Array(j,Array(i,0))
	for m in range (0,i):
		for n in range(0,j):
			Tranpuesta[n][m]=Matriz[m][n]
	return Tranpuesta
	
def Top_Triangle(Matriz): #Triangular Superior
	i=len(Matriz)
	j=len(Matriz[0])
	Flag=True
	cnt=1
	if i==j:
		for m in range (0,i):
			for n in range(0,j):
				if m>n and Matriz [m][n]!=0:
					Flag=False
				elif m==n:
					cnt=cnt*Matriz [m][n]
		if Flag!=False:
			print("Es triangular Inferior")
			return Transposed(Matriz)
	elif i!=j:
		print("No es Cuadrada")
	else:
		print("No es Triangular inferior")
	return None