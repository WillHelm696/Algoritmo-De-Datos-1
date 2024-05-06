from linkedlist import *

def reverse(L):
	if L.head!=None:
		x=L.head
		y=L.head.nextNode
		while y!=None:
			tmp=y.nextNode
			y.nextNode=x
			if x==L.head:
				x.nextNode=None
			x=y
			y=tmp
		L.head=x