from LinkedList import *
from mystack import *

class PriorityQueue:
	head=None
class PriorityNode:
	value=None
	nextNode=None
	priority=None

def enqueue_priority(Q,element,priority):
	Nodo=PriorityNode()
	Nodo.value=element
	Nodo.priority=priority
	if Q.head==None or Q.head.priority<priority:
		Nodo.nextNode=Q.head
		Q.head=Nodo
	else:		
		current=Q.head
		previous=Q.head
		while current.nextNode!=None:
			current=current.nextNode
			if current.priority<priority:
				Nodo.nextNode=previous.nextNode
				previous.nextNode=Nodo
				return search(Q,element)
			previous=previous.nextNode
		Nodo.nextNode=previous.nextNode
		previous.nextNode=Nodo
	return search(Q,element)
	

def dequeue_priority(Q):
  if Q.head==None:
    return None
  elmt=Q.head.value
  Q.head=Q.head.nextNode
  return elmt
