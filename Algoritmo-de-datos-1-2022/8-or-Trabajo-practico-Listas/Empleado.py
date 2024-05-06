from LinkedList import *

class Empleado:
	nombre=None
	edad=None
	nroLegajo=None
	
def Add(L,Name,Age,File): #Agrega ala lista los Nodo de tipo empleado
  Employee=Empleado()
  Employee.nombre=Name
  Employee.edad=Age
  Employee.nroLegajo=File
  NodeA=Node()
  NodeA.value=Employee
  NodeA.nextNode=L.head
  L.head=NodeA


def print_E(L): #Imprime La lista de empleados
	current=L.head
	while current!=None:
		print(current.value.nombre, current.value.edad,current.value.nroLegajo)
		current=current.nextNode

def Set_LG(E):# Elimina Legajos duplicados de la lista
	#print("Entro al SET...")
	previous=E.head
	current=E.head
	lng=length(E)
	for n in range (0,lng):
		#print("entro al N:")
		if (previous.nextNode==None):
			#print("el siguiente es None, salgo")
			return
		
		#print(" tomo el N:", previous.value.nroLegajo)
		antCurrent=previous
		current=previous.nextNode
		for m in range (n,lng):
			if(current!=None):
				#print(" comparo con el M:", current.value.nroLegajo)
				if previous.value.nroLegajo==current.value.nroLegajo:
					#print("encuentro iguales, borro:",previous.value.nroLegajo)
					#print("antCurrent:",antCurrent.value.nroLegajo)
					#if(current.nextNode!=None):
					#	print("Current:",current.nextNode.value.nroLegajo)
					antCurrent.nextNode=current.nextNode
					lng=lng-1
				antCurrent=current
				current=current.nextNode	
				
		previous=previous.nextNode
		#print("avanzo previous al: ",previous.value.nroLegajo)

			

def insert_File(L,Name,Age,File): #Inserta Un empleado en una pocicion de legajo
  Employee=Empleado()
  Employee.nombre=Name
  Employee.edad=Age
  Employee.nroLegajo=File
  current=L.head
  pos=0
  while current!=None:
  	if File<current.value.nroLegajo:
  		return insert(L,Employee,pos)
  	pos+=1
  	current=current.nextNode
  	
def Move( L ,Leg1,Leg2): #Mueve elementos de Una pocicion a otra
	if length( L ) > 1:	
		cur=L.head #Primer nodo
		pre=L.head
		while pre.nextNode.value.nroLegajo!=Leg1 :
			pre = pre.nextNode
		while cur.nextNode.value.nroLegajo!=Leg2:
			cur=cur.nextNode		
		next = cur.nextNode.nextNode  # (1)
		pre.nextNode = cur.nextNode  # (2)
		cur.nextNode.nextNode = cur  # (3)
		cur.nextNode = next  # (4)
