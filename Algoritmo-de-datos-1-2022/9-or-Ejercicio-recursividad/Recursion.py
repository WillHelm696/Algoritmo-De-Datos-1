from LinkedList import *
from Stack import *
#-----------------------------------------------------------------
def Fibonacci(n):
	if n==0 or n==1:
		return n
	return Fibonacci(n-1)+Fibonacci(n-2)

def Summation(n):
	if n==0 or n ==1:
		return n
	return n+Summation(n-1)
#-----------------------------------------------------------------
def Sum_Even(n):
	if n%2!=0:
		return None
	elif n<=2:
		return n
	return n+Sum_Even(n-2)
#-----------------------------------------------------------------
def Fibonacci_Stack(n):
	S=LinkedList()
	S1=0
	S2=1
	if n==0:
		return S1
	for n in range (0,n-1):
		push(S,S2+S1)
		S1=S2
		S2=pop(S)
	return S2
#-----------------------------------------------------------------
def Organize(L):
	lng=length(L)
	Move(L,0,lng)
	
def Move(L,orig,dest):		
	if orig<dest:
		pos=orig
		for n in range(orig,dest):
			if access(L,n)<access(L,pos):
				pos=n
		if pos!=orig:
			pre=L.head
			sig=pre
			for n in range(1,orig):
				pre=pre.nextNode
			for n in range(0,pos-1):
				sig=sig.nextNode
			tmp=sig.nextNode
			sig.nextNode = sig.nextNode.nextNode
			if orig==0:
				tmp.nextNode = L.head
				L.head=tmp
			else:
				tmp.nextNode = pre.nextNode
				pre.nextNode=tmp
	else:
		return L
	return Move(L,orig+1,dest)
	
