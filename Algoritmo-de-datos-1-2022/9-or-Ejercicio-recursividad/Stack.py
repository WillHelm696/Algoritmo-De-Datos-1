from algo1 import *
from LinkedList import *


def push(S,element):
	add(S,element)
	
def pop(S):
	if None!=S.head:
		element=S.head.value
		S.head=S.head.nextNode
		return element
	return None
		
	