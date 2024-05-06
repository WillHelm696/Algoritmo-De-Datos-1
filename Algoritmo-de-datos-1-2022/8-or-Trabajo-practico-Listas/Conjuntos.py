from algo1 import *
from LinkedList import *

def Intercalar(C,A,B): # Intercala elementos de ambos conjuntos  
	lng=length(A)+length(B)
	current_A=A.head
	current_B=B.head
	for n in range (0,lng):
		if n%2==0 and current_A!=None:
			insert(C,current_A.value,n)
			current_A=current_A.nextNode
		elif n%2!=0 and current_B!=None :
			insert(C,current_B.value,n)
			current_B=current_B.nextNode
	
def Diferencia_Pares(C,A): #Elimina del conjunto C los pares de A
	current=A.head
	while current!=None:
		if current.value%2==0:
			delete (C,current.value)
		current=current.nextNode

def Lista_impares(D,C): #Saca de la lista C los valores Impares
	current=C.head
	pos=0
	while current!=None:
		if current.value%2!=0:
			insert (D,current.value,pos)
			pos+=1
		current=current.nextNode

def union_conjuntos(A,B): #Une dos conjuntos Sin A repeticiones y B (50,100) 
	Set(A)
	pos=length(A)
	current=B.head
	while current!=None:
		if 50<current.value and current.value<100:
			insert(A,current.value,pos)
			pos+=1
		current=current.nextNode

def Set(E): #Elimina elementos duplicados de la Lista
	previous=E.head
	current=E.head
	lng=length(E)
	for n in range (0,lng):
		if (previous.nextNode==None):
			return
		antCurrent=previous
		current=previous.nextNode
		for m in range (n,lng):
			if(current!=None):
				if previous.value==current.value:
					antCurrent.nextNode=current.nextNode
					lng=lng-1
				antCurrent=current
				current=current.nextNode	
		previous=previous.nextNode
