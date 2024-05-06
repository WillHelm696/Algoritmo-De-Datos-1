from linkedlist import *
from exch import *

def BubbleSort(L):
	lng=length (L)-1
	if lng>1 or lng!=None:
		Burbuja(L,lng)
		return L
def Burbuja(L,pos):
	if pos>1:
		pre=L.head
		sig=pre.nextNode
		for n in range (0,pos):
			#print()
			#print('n:',n)
			#print('pre',pre.value,'sig',sig.value)
			if pre.value > sig.value:
				pre.nextNode = sig.nextNode
				if n==0:
					sig.nextNode = L.head
					L.head=sig
				else:
					#print('CAMBIAR',pre.value,'POR',sig.value)
					#print('tmp',tmp.value)
					sig.nextNode=pre
					tmp.nextNode=sig
				pre=sig
				sig=pre.nextNode
			
			tmp=pre
			pre=sig
			sig=pre.nextNode
	else:
		return L
	#print_L(L)
	return Burbuja(L,pos-1)
#-----------------------------------------------------------------
def SelectionSort(L):
	if L.head!=None:
		Seleccion(L,0)
	return L

def Seleccion(L,pos):
	lng=length(L)
	if 1 < lng and pos < lng :
		Myr=pos
		for n in range(pos+1,lng):
			if access(L,Myr)>=access(L,n):
				Myr=n
		Exchange(L,Myr,pos)
		#print_L(L)
		return Seleccion(L,pos+1)
	return L
#-----------------------------------------------------------------
def InsertionSort(L):
	Lng=length (L)
	if 1<Lng:
		Inserción(L,0,Lng)
	return L

def Inserción(L,Pos,Lng):
	if Pos<Lng :
		#print('desde 0 a Pos:',Pos)
		if 0<Pos:
			
			Curr=L.head
			Pre=Curr
			for n in range(0,Pos):
				Aux=Curr
				Curr=Curr.nextNode
			for n in range(0,Pos):
				if Pre.value<Curr.value:
					Ant=Pre
					Pre=Pre.nextNode
			#print('Nodo Curr:',Curr.value)
			#print('posisionar en Pre:',Pre.value)
			
			Aux.nextNode=Aux.nextNode.nextNode
			if Pre == L.head:
				Curr.nextNode=L.head	
				L.head = Curr
			else:
				#print('SI-------------')
				Curr.nextNode=Ant.nextNode
				Ant.nextNode=Curr
	else:
		return L
	print_L(L)
	#print('')
	return Inserción(L,Pos+1,Lng)