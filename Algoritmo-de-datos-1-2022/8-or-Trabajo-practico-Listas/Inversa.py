from LinkedList import *

def reverse(L):#Invierte una listas de elementos
	if L.head!=None:
		pre=L.head
		sig=L.head.nextNode
		while sig!=None:
			tmp=sig.nextNode
			sig.nextNode=pre
			if pre==L.head:
				pre.nextNode=None
			pre=sig
			sig=tmp
		L.head=pre