from algo1 import *
from short import *
S = LinkedList()
add(S,10),add(S,82),add(S,9),add(S,3),add(S,43),add(S,27),add(S,38)
L = LinkedList()
add(L,2),add(L,9),add(L, 4),add(L, 7),add(L, 3),add(L,8),add(L,6),add(L,10),add(L,1),add(L,11),add(L,12),add(L,5)
T = LinkedList()
add(T,66),add(T,47),add(T,20),add(T,12),add(T,47)
print('Lista Ordenada')
print()
print('BubbleSort')
print_L(S)
print_L(BubbleSort(S))
print()
print('SelectionSort')
print_L(L)
print_L(SelectionSort(L))
print()
print('InsertionSort')
print_L(T)
print_L(InsertionSort(T))