from linkedlist import *
from exch import *
import random
import math
def MergeShort(L):
	lng=length(L)
	if lng>1 :
		k=math.trunc(lng/2)-1
		S=LinkedList()
		Pre=L.head
		#print_L(L)
		#print('K:',k,'Lgn:',lng)
		for n in range (0,k):
			Pre=Pre.nextNode
		S.head=Pre.nextNode
		Pre.nextNode=None
		#print_L(L)
		#print_L(S)
		L=MergeShort(L)
		S=MergeShort(S)
		return Merge(L,S)
	return L		

def Merge(A,B): 
	#print_L(A)
	#print_L(B)
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
	#print_L(L)
	return L
"----------------------------------------------------------------------"
def QuickSort(L):
	lng=length(L)-1                      #Complejodad O(n)
	if 1<lng :
		return Quick(L,0,lng)          
	return L

def Quick(L,Dsd,Hst):
	if 1<(Hst-Dsd):
		#Pos=random.randint(Dsd,Hst)
		Piv=access(L,Hst)                  #Complejidad O(n)
		
		#print('Dsd:',Dsd,' Hst:',Hst)		
		#print('Pivote:',Piv)
		Cnt=Dsd
		for n in range(Dsd,Hst+1):	       #Complejidad O(n°2)
			if access(L,n) <= Piv :
				#print('Cnt',Cnt,'n',n)
				Exchange(L,Cnt,n)
				Cnt+=1
		#print_L(L)
		Pos=search(L,Piv)									 #Complejidad O(n)
		#print(Pos)
		Quick(L,Dsd,Pos-1)						 #F(n/2)
		Quick(L,Pos,Hst)							 #F(n/2)
	#print()
	return L