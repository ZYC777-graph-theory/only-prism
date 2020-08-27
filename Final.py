# coding:utf8
import graph
import copy
global T,num
list_of_leaf=[]
from collections import deque,defaultdict
def check_triangle(G,edge_list):
	for i in edge_list:
		if list(set(G.vertexList[i[0]].next)&set(G.vertexList[i[1]].next))==[]:
			return True
	return False


class Tarjan(object):
    def criticalConnections(self, n, connections):
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
            
        dfn = [None for i in range(n)]
        low = [None for i in range(n)]
       	parent_list=[None for i in range(n)]
        cur = 0
        start = 0
        res = []
        self.cur = 0
       
        def dfs(node,parent):

            if dfn[node] is None:
                dfn[node] = self.cur
                low[node] = self.cur
                self.cur+=1
                for n in graph[node]:
                    if dfn[n] is None:
                        dfs(n,node)    
                if parent is not None:

                    l = min([low[i] for i in graph[node] if i!=parent]+[low[node]])
                    parent_list[parent]=node
                else:
                    l = min(low[i] for i in graph[node]+[low[node]])
                low[node] = l
            parent_list[node]=parent    
        dfs(0,None)
        print("low and dfn is ",low,dfn)
        for v in connections:
            if (low[v[1]]>=dfn[v[0]] and parent_list[v[1]]==v[0]):
                res.append(v[0])
            elif(low[v[0]]>=dfn[v[1]] and parent_list[v[0]]==v[1]):
            	res.append(v[1])
        print("Parent list",parent_list)
        res.pop(0)
        res=list(set(res))
        return res
class BinaryTree(object):
    def __init__(self, root_value):
        self.root = root_value
        self.leftchild = None
        self.rightchild = None
    def insert_left(self, left_value):
        if self.leftchild == None :
            self.leftchild = BinaryTree(left_value)
        else:
            left_subtree = BinaryTree(left_value)
            left_subtree.leftchild = self.leftchild
            self.leftchild = left_subtree
    def insert_right(self, right_value):
        if self.rightchild == None :
            self.rightchild = BinaryTree(right_value)
        else:
            right_subtree = BinaryTree(right_value)
            right_subtree.rightchild = self.rightchild
            self.rightchild = rightchild
  
    def set_root(self, root_value):
        self.root = root_value




#Initailization===================================
def Initialization(G):
	Nonadjecent_List=G.findNonadjecentnode()
	vw=[]
	Flag=False
	for node in Nonadjecent_List.keys():
		if(Nonadjecent_List[node]):
			vw.append(node)
			vw.append(Nonadjecent_List[node][0])
			break
	if(len(vw)==0):
		return Flag,0
	v=vw[0]
	w=vw[1]
	N=G.vertexList.get(v).next
	N.pop()
	V=[]
	for i in G.vertexList.keys():
		V.append(i)
	W=[]
	Sub_graph=copy.deepcopy(G)
	for i in N:
		Sub_graph.removeVertex(i)
	for i in Sub_graph.vertexList.keys():
		if Sub_graph.BFS_search(i,w):
			W.append(i)
	M=[]
	for i in N:
		A=G.vertexList.get(i).next
		A.pop()
		for n in A:
			if n in W:
				M.append(i)
				break
	xy=[]
	for i in M:
		for j in Nonadjecent_List[i]:
			if j in M:
				xy=[j,i]
				break
	if (len(xy)==0):
		part=[]
		Sub_graph2=copy.deepcopy(G)
		for i in M:
			Sub_graph2.removeVertex(i)
		for i in Sub_graph2.vertexList.Keys():
			if BFS_search(i,v):
				part.append(i)
		partition=[part,M]
		return Flag,partition
	Sub_graph1=copy.deepcopy(G)
	for i in G.vertexList.keys():
		if i not in M and  i not in W:
			Sub_graph1.removeVertex(i)
	Chordless_path=Sub_graph1.BFS_search_chordless(xy[0],xy[1],W)
	Chordless_cycle=Chordless_path
	Chordless_cycle.append(v)
	Flag=True
	return Flag,Chordless_cycle


#==================start_finding clique_cutset====================
def whitesides(G,S):
	clique_cutset=[]
	x=0
	y=0
	P=[]
	Nonadjecent_List=G.findNonadjecentnode()
	while S !=G.vertexList.keys():
		C=[]
		Sub_graph2=copy.deepcopy(G)
		for i in S:
			Sub_graph2.removeVertex(i)
		for i in Sub_graph2.vertexList.keys():
			if Sub_graph2.BFS_search(i,Sub_graph2.vertexList.keys()[0]):
				C.append(i)
		R=[]
		for n in S:
			for m in G.vertexList[n].next:
				if (m in C) and (n not in R):
					R.append(n)
		if G.clique_check(R):
			if R==[]:
				R=False
				return R,0
			clique_cutset=R
			print("Clique cutset is :",clique_cutset)
			return R,C
		else:
			for n in R:
				for m in Nonadjecent_List[n]:
					if m in R:
						x=n
						y=m 
						break
		P=G.BFS_search_chordless(x,y,C)

		for i in P[:]:
			if(i!=P[0] and i!=P[-1]):
				S.append(i)
	return False,0
#====================Decomposition Tree===========================

def pre_traversal(tree):
	flag=False

	if(tree!=None):
		flag,output=Initialization(tree.root)
     	if(flag!=True and tree!=None):
     		if(output!=0):
     			G1=copy.deepcopy(tree.root)
     			for i in output[0]:
     				G1.removeVertex(i)
     			tree.insert_left(G1)
     			G2=copy.deepcopy(tree.root)
     			for i in G2.vertexList.keys:
     				if i not in output[0] and i not in output[1]:
     					G2.removeVertex(i)
     			tree.insert_right(G2)
     			tree.set_root(output[1])
     			if(tree!=None):
     				pre_traversal(tree.leftchild)
     				pre_traversal(tree.rightchild)
        elif(flag==True and tree!=None):
        	clique,partition=whitesides(tree.root,output)
        	if (clique!=False):
        		G1=copy.deepcopy(tree.root)
        		for i in partition:
        			G1.removeVertex(i)
        		tree.insert_left(G1)
        		G2=copy.deepcopy(tree.root)
        		for i in G2.vertexList.keys():
        			if i not in clique and i not in partition:
        				G2.removeVertex(i)
        		tree.insert_left(G2)
        		tree.set_root(clique)
        		if (tree!=None):
        			pre_traversal(tree.leftchild)
        			pre_traversal(tree.rightchild)
def in_traversal(tree,list_of_leaf):
    if tree != None:
    	if not isinstance(tree.root,list):
    		print(tree.root.vertexList.keys())
    		list_of_leaf.append(tree.root)
        in_traversal(tree.leftchild,list_of_leaf)
        in_traversal(tree.rightchild,list_of_leaf)
    return list_of_leaf


'''
G = graph.Graph()
for i in range(1,12):
    G.addVertex(i)

G.addEdge(1,2)
G.addEdge(1,3)
G.addEdge(2,4)
G.addEdge(3,5)
G.addEdge(3,4)
G.addEdge(4,7)
G.addEdge(5,6)
G.addEdge(5,8)
G.addEdge(6,8)
G.addEdge(6,7)
G.addEdge(7,9)
G.addEdge(8,10)
G.addEdge(8,9)
G.addEdge(9,11)
G.addEdge(10,11)

G2=graph.Graph()
for i in range(1,9):
	G2.addVertex(i)
G2.addEdge(1,2)
G2.addEdge(1,5)
G2.addEdge(2,1)
G2.addEdge(2,6)
G2.addEdge(2,3)
G2.addEdge(3,7)
G2.addEdge(3,4)
G2.addEdge(4,8)
G2.addEdge(5,6)
G2.addEdge(6,7)
G2.addEdge(7,8)
Root=BinaryTree(G)
pre_traversal(Root)
print("============Leaf nodes=================")
in_traversal(Root,list_of_leaf)
list_of_leaf2=[]
a,b=Initialization(G2)
print(whitesides(G2,b))
Root2=BinaryTree(G2)
pre_traversal(Root2)
in_traversal(Root2,list_of_leaf2)

'''
