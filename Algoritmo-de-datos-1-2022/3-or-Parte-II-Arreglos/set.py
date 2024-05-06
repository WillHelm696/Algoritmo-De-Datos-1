from algo1 import *
def Create_Set(Arreglo):
	cnt=0
	i=len(Arreglo)
	for m in range (0,i):
		for n in range (m,i):
			if Arreglo[m]==Arreglo[n] and m<n and Arreglo[n]!=None:
				Arreglo[n]=None
		if Arreglo[m]==None:
			cnt=cnt+1
	if 0<cnt:	
		Vector=Array(i-cnt,0)
		cnt=0
		for j in range (0,i):
			if Arreglo[j] != None:
				Vector[cnt]=Arreglo[j]
				cnt+=1
		return Vector
	return Arreglo
	
def Union(Arreglo_S,Arreglo_T):
	i=len(Arreglo_S)
	j=len(Arreglo_T)
	Arreglo_W=Array(i+j,0)
	for n in range (0,i):
		Arreglo_W[n]=Arreglo_S[n]
	for k in range (0,j):
		Arreglo_W[i+k]=Arreglo_T[k]
	return Create_Set(Arreglo_W)
		
def Intersection(Arreglo_S,Arreglo_T):
	i=len(Arreglo_S)
	j=len(Arreglo_T)
	Arreglo_W=Array(i,0)
	for m in range (0,i):
		for n in range (0,j):
			if Arreglo_S[m]==Arreglo_T[n] :
				Arreglo_W[m]=Arreglo_S[m]
	Arreglo_W=Create_Set(Arreglo_W)
	return Arreglo_W
	
def Difference(Arreglo_S,Arreglo_T):
	i=len(Arreglo_S)
	Arreglo_W=Intersection(Arreglo_S,Arreglo_T)
	j=len(Arreglo_W)
	for m in range (0,i):
		for n in range (0,j):
			if Arreglo_S[m]==Arreglo_W[n] :
				Arreglo_S[m]=None
	Arreglo_A=Create_Set(Arreglo_S)
	return Arreglo_A

def check_duplicates(Array):
	i=len(Array)
	for m in range (0,i):
		for n in range (m,i):
			if Arreglo[m]==Arreglo[n] and m<n and Arreglo[n]!=None:
				return Print ('Duplicate')
				
#def Create_Set(Array):
#	cnt=len(Array)
#	i=len(Array)
#	for m in range (0,i):
#		for n in range (m,i):
#			if Array[m]==Array[n] and m<n:
#				cnt=cnt-1
#				n=i
#	if cnt<i:	
#		vector=Array(cnt,0)
#		cnt=cnt-1
#		for m in range (i-1,-1,-1):
#			for n in range (m,-1,-1):
#				if vector[m]!=Array[n] and m<n:
#					vector[cnt]=Array[n]
#					cnt=cnt-1
#					n=0
#	return Array
