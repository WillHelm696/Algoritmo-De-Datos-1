def Exchange(L,orig,dest):		
	if orig<dest:               
		Nod1=L.head                
		Nod2=Nod1                 
		for n in range(0,orig):
			Pre1=Nod1
			Nod1=Nod1.nextNode
		for n in range(0,dest):
			Pre2=Nod2
			Nod2=Nod2.nextNode
		tmp1=Nod1
		tmp2=Nod2
		Pre2.nextNode = Pre2.nextNode.nextNode
		if Nod1==L.head:
			tmp2.nextNode = L.head
			L.head=tmp2
		else:
			tmp2.nextNode = Nod1
			Pre1.nextNode=tmp2
		if (orig+1)!=dest:
			Nod2.nextNode=Nod2.nextNode.nextNode		
			tmp1.nextNode=Pre2.nextNode
			Pre2.nextNode=tmp1
	elif dest<orig:
		return Exchange(L,dest,orig)
	return L