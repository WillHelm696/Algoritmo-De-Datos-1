from linkedlist import *
from Queue import *
from Inversa import *

class BinaryTree:
	root=None
class BinaryTreeNode:
	key=None
	value=None
	leftnode=None
	rightnode=None
	parent=None
'------------------------------------------------------------'
def search(B,element):
	if B.root!=None:
		return Búsqueda(B.root,element)
	return None
def Búsqueda(Current,element):
	if Current!=None:
		if Current.value==element:
			return Current.key
		key=Búsqueda(Current.leftnode,element)
		if key==None:
			key=Búsqueda(Current.rightnode,element)
		return key
'------------------------------------------------------------'
def insert(B,element,key):
	Node=BinaryTreeNode()
	Node.key=key
	Node.value=element
	if B.root==None:
			B.root=Node
			return key
	return Add_Node(B.root,Node)
def Add_Node(Current,Node):
	if Current.leftnode!=None or Current.rightnode!=None:	
		if Current.key==Node.key:
			return 
		if Current.leftnode!=None:
			if Node.key<Current.key: #Si el nodo es menor entra por izq
				return Add_Node(Current.leftnode,Node)
		if Current.rightnode!=None:#Si el nodo es mayor entra por der
			if Current.key<Node.key:
				return Add_Node(Current.rightnode,Node)
	if Current.leftnode==None or Current.rightnode==None:
		if Node.key<Current.key and Current.leftnode==None:
			Current.leftnode=Node
		elif Current.key<Node.key and Current.rightnode==None:
			Current.rightnode=Node			
	Node.parent=Current
	return Node.key
'------------------------------------------------------------'
def delete(B,element):
	key=search(B,element)
	if key!=None:
		return deleteKey(B,key)
	return None 
def deleteKey(B,key):
	if access(B,key)!=None:
		Nodo=Node_Raiz(B,key)
		return Nodo.key
	return None
'------------------------------------------------------------'
def Node_Raiz(B,key):
	if B.root.key==key: # El Nodo a eliminar es la raiz
		Node=B.root
		if Node.leftnode!=None or Node.rightnode!=None: #si el arbol Tiene hijos
			B.root=Node_Interno(B.root,key) # Busca El nodo Hoja para insertal en la raiz
		else: #El arbol tiene solo un nodo raiz
			B.root=Node.leftnode 
		return Node #Elimina el unico no do y lo devuelve
	return Node_Interno(B.root,key) #Si el Nodo es una rama o una hoja Entra al arbol

def Node_Hoja(Node,key):#Desvincula la hoja del arbol
	Rama=Node.parent 
	if Rama.leftnode!=None:
		if Rama.leftnode.key==key:
			Rama.leftnode=Node.leftnode
	if Rama.rightnode!=None:
		if Rama.rightnode.key==key:
			Rama.rightnode=Node.rightnode
	return Node # devuelve el la hoja desvinculada
	
def Node_Interno(Current,key):#Fucion para eliminar una rama
	if Current!=None:
		if Current.key==key:#Si encontro el nodo a eliminar
			Rama=Current
			Node=Current
			if Rama.leftnode==None and Rama.rightnode==None:
				return Node_Hoja(Current,key)		#Si el nodo No tiene hijos es una hoja
			elif Rama.leftnode!=None:
				Current=Current.leftnode
				while Current.rightnode!=None:#Busca El menor de su rama Derecha 
					Current=Current.rightnode					
			elif Rama.rightnode!=None:
				Current=Current.rightnode
				while Current.leftnode!=None:#Busca el menor de su rama Izquierda
					Current=Current.leftnode
			elif Current.rightnode!=None or Current.leftnode!=None:
				return Node_Interno(Current,Current.key)
			Hoja=Node_Hoja(Current,Current.key)
			Hoja.rightnode=Rama.rightnode
			Hoja.leftnode=Rama.leftnode
			Hoja.parent=Rama.parent
			if Rama.parent==None:
				return Hoja #Retorna La hoja para Colocarlo como raiz
			#--------------------	
			else:#Problema sin solucion En Observacion
				Rama=Hoja#No efectua el cambio
			#--------------------					
		elif key<Current.key: # Recusion para buscar la llave
			return Node_Interno(Current.leftnode,key)
		elif Current.key<key:
			return Node_Interno(Current.rightnode,key)
	return Node
'------------------------------------------------------------'
def access(B,key):
	if B.root!=None:
		return Acceso(B.root,key)
	return None
def Acceso(Current,key):
	#print(Current.value)
	if Current!=None:
		if Current.key==key:
			return Current.value
		elif key<Current.key:
			return Acceso(Current.leftnode,key)
		elif Current.key<key:
			return Acceso(Current.rightnode,key)
	return None
'------------------------------------------------------------'
def update(B,element,key):
	if B.root!=None:
		return Actualizar(B.root,element,key)
	return None
def Actualizar(Current,element,key):
	if Current!=None:
		if Current.key==key:
			Current.value=element
			return Current.key
		elif key<Current.key:
			return Actualizar(Current.leftnode,element,key)
		elif Current.key<key:
			return Actualizar(Current.rightnode,element,key)
	return None
'------------------------------------------------------------'
def traverseInOrder(B):
	if B.root!=None:
		L=Order(LinkedList(),B.root)
		reverse(L)
		return L
	return None
def Order(L,Current):
	if Current!=None:
		Order(L,Current.leftnode)
		add(L,Current.value)
		Order(L,Current.rightnode)
	return L
'------------------------------------------------------------'
def traverseInPostOrder(B):
	if B.root!=None:
		L= PostOrder(LinkedList(),B.root)
		reverse(L)
		return L
	return None	
def PostOrder(L,Current):
	if Current!=None:
		PostOrder(L,Current.leftnode)
		PostOrder(L,Current.rightnode)
		add(L,Current.value)
	return L	
'------------------------------------------------------------'
def traverseInPreOrder(B):
	if B.root!=None:
		L=PreOrder(LinkedList(),B.root)
		reverse(L)
		return L
	return None
def PreOrder(L,Current):
	if Current!=None:
		add(L,Current.value)
		PreOrder(L,Current.leftnode)
		PreOrder(L,Current.rightnode)
	return L
'------------------------------------------------------------'
def traverseBreadFirst(B):
	if B.root!=None:
		Q=Queue()
		enqueue(Q,B.root)		
		L=BreadFirst(LinkedList(),Q)
		reverse(L)
		return 	L
	return None
def BreadFirst(L,Q):
	if Q.head!=None:
		Node=dequeue(Q)
		add(L,Node.value)
		if Node.leftnode!=None:
			enqueue(Q,Node.leftnode)
		if Node.rightnode!=None:
			enqueue(Q,Node.rightnode)
		return BreadFirst(L,Q)
	return L
'------------------------------------------------------------'
def print_B(B):
	print_L(traverseBreadFirst(B))