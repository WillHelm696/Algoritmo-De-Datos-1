from LinkedList import *
from Exch import *
import random
import math

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
			if pre.value > sig.value:
				pre.nextNode = sig.nextNode
				if n==0:
					sig.nextNode = L.head
					L.head=sig
				else:
					sig.nextNode=pre
					tmp.nextNode=sig
				pre=sig
				sig=pre.nextNode	
			tmp=pre
			pre=sig
			sig=pre.nextNode
	else:
		return L
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
			Aux.nextNode=Aux.nextNode.nextNode
			if Pre == L.head:
				Curr.nextNode=L.head	
				L.head = Curr
			else:
				Curr.nextNode=Ant.nextNode
				Ant.nextNode=Curr
	else:
		return L
	print_L(L)
	return Inserción(L,Pos+1,Lng)
#-----------------------------------------------------------------

def MergeShort(L):
	lng=length(L)
	if lng>1 :
		k=math.trunc(lng/2)-1
		S=LinkedList()
		Pre=L.head
		for n in range (0,k):
			Pre=Pre.nextNode
		S.head=Pre.nextNode
		Pre.nextNode=None
		L=MergeShort(L)
		S=MergeShort(S)
		return Merge(L,S)
	return L		

def Merge(A,B): 
	L=LinkedList()
	if A.head!=None and B.head!=None:
		if A.head.value<=B.head.value:
			L.head=A.head
			A.head=A.head.nextNode
		else:
			L.head=B.head
			B.head=B.head.nextNode
	Curr=L.head
	while A.head!=None and B.head!=None: 
		if A.head.value<=B.head.value:
			Curr.nextNode=A.head
			A.head=A.head.nextNode
		else:
			Curr.nextNode=B.head
			B.head=B.head.nextNode
		Curr=Curr.nextNode
	if A.head!=None and B.head==None:
		Curr.nextNode=A.head
		A.head=A.head.nextNode
	if A.head==None and B.head!=None:
		Curr.nextNode=B.head
		B.head=B.head.nextNode
	return L
"----------------------------------------------------------------------"
def QuickSort(L):
	lng=length(L)-1                      #Complejodad O(n)
	if 1<lng :
		return Quick(L,0,lng)          
	return L

def Quick(L,Dsd,Hst):
	if 1<(Hst-Dsd):
		Piv=access(L,Hst)                  #Complejidad O(n)
		Cnt=Dsd
		for n in range(Dsd,Hst+1):	       #Complejidad O(n°2)
			if access(L,n) <= Piv :
				Exchange(L,Cnt,n)
				Cnt+=1
		Pos=search(L,Piv)									 #Complejidad O(n)
		Quick(L,Dsd,Pos-1)						 #F(n/2)
		Quick(L,Pos,Hst)							 #F(n/2)
	return L
