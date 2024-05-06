from binarytree import *

def balanced(B):
	if B.root!=None:
		X=Altura(B.root.leftnode,0)
		Y=Altura(B.root.rightnode,0)
		if X==Y:
			return True
		if X+1==Y or X==Y+1:
			return True
	return False
	
def Altura(Current,Cnt):
	if Current!=None:
		Cnt+=1
		if Current.leftnode!=None:
			return Altura(Current.leftnode,Cnt)
		elif Current.rightnode!=None:
			return Altura(Current.rightnode,Cnt)
	return Cnt	
'-----------------------------------------------'
def subTree(BT1,BT2):
	if BT1.root!=None and BT2!=None:
		S=InOrder(BT1.root,LinkedList())
		T=InOrder(BT2.root,LinkedList())
		return SubList(S.head,T.head)
	return False
	
def SubList(Curr_S,Curr_T):
	if Curr_S!=None and Curr_T!=None:
		if Curr_S.value.value==Curr_T.value.value:
			return SubTree(Curr_S.value,Curr_T.value,True)
		return SubList(Curr_S.nextNode,Curr_T)	
	return False
	
def SubTree(Curr_S,Curr_T,Flag):
	if Curr_T!=None:
		if Curr_S!=None:		
			if Curr_S.value==Curr_T.value:
				Flag=SubTree(Curr_S.leftnode,Curr_T.leftnode,Flag)
				Flag=SubTree(Curr_S.rightnode,Curr_T.rightnode,Flag)
			else:	
				Flag=False
		else:	
			Flag=False
	return Flag
'-----------------------------------------------'
def checkBST(B):
	if B.root!=None:
		L=InOrder(B.root,LinkedList())
		Pre=L.head
		Curr=Pre.nextNode
		while Curr!=None:
			if Pre.value.key<Curr.value.key:
				return False
			Pre=Curr
			Curr=Curr.nextNode
	return True
	
def InOrder(Current,L):
	if Current!=None:
		InOrder(Current.leftnode,L)
		add(L,Current)
		InOrder(Current.rightnode,L)
	return L
	