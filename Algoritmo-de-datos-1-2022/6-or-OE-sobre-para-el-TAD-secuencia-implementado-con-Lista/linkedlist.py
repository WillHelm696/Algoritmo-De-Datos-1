from algo1 import *
class LinkedList:
	head=None
class Node:
	value=None
	nextNode=None

def add(L,element):
	Nodo=Node()
	Nodo.value=element
	Nodo.nextNode=L.head
	L.head=Nodo	
	
def search(L,element):
	current=L.head
	pos=0
	while current!=None:
		if current.value==element:
			return pos
		pos+=1
		current=current.nextNode
	return None
	
def insert(L,element,pos):
	if pos==0:
		add(L,element)
		return 0
	if L.head!=None:
		if 0<pos or pos<length(L):
			current=L.head
			for n in range(0,pos-1):
				current=current.nextNode
			Nodo=Node()
			Nodo.value=element
			Nodo.nextNode=current.nextNode
			current.nextNode=Nodo
	return search(L,element)

def delete(L,element):
	current=L.head
	pos=search(L,element)
	if pos==0 and pos!=None:
		L.head=current.nextNode
	elif pos!=None and 0<pos:
		while current.nextNode.value!=element:
			current=current.nextNode
		current.nextNode=current.nextNode.nextNode

	return pos

def length(L):
	cnt=0
	current=L.head
	while current!=None:
		cnt+=1
		current=current.nextNode
	return cnt
	
def access(L,pos):
	current=L.head
	if 0<=pos<length(L):
		for n in range(1,pos+1):
			current=current.nextNode
		return current.value
	return None

def update(L,element,pos):
	if 0<=pos<length(L):
		insert(L,element,pos)
		element=access(L,pos+1)
		delete(L,element)
		return pos
	return None

def print_L(L):
	current=L.head
	while current!=None:
		print("[",current.value,"|]->",end='')
		current=current.nextNode
	print(None)