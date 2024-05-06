from linkedlist import *
from exch import *
def HeapSort(L):
	return Heap(L,length(L))

def Heap(L,lng):
	if 1<lng:
		Heapify(L,lng)
		Exchange(L,0,lng-1)
	else:
		return L
	return Heap(L,lng-1)
	
def Heapify(L,End):
	Flag=True
	if 1<End:
		for n in range(0,End):
			if 2*n+1<End:
				#print('n:',n,'2n:',2*n+1)
				if access(L,n) < access(L,2*n+1):
					Flag==False
					Exchange(L,n,2*n+1)
			if 2*n+2<End:
				#print('n:',n,'2n+1:',2*n+2)
				if access(L,n) < access(L,2*n+2):
					Flag==False
					Exchange(L,n,2*n+2)
	if Flag!=True:
		return Heapify(L,End)
	return L