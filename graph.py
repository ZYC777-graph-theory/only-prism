from collections import deque,defaultdict
import copy
def tree(): return defaultdict(tree)
class Vertex:
    def __init__(self,name):
        self.name = name
        self.next = []

class Graph:
    def __init__(self):
        self.vertexList = {}
    def isempty(self):
        for i in self.vertexList:
            if self.vertexList[i].next !=None:
                return False
            else:
                return True

    def addVertex(self,vertex):
        if vertex in self.vertexList:
            return
        self.vertexList[vertex] = Vertex(vertex)

    def addEdge(self,fromVertex,toVertex):
        if fromVertex == toVertex:
            return
        if fromVertex not in self.vertexList:
            print("vertexList has no ",fromVertex)
            return
        if toVertex not in self.vertexList:
            print("vertexList has no ", toVertex)
            return
        if(toVertex not in self.vertexList[fromVertex].next):
            self.vertexList[fromVertex].next.append(toVertex)
        if (fromVertex not in self.vertexList[toVertex].next):
            self.vertexList[toVertex].next.append(fromVertex)
        # self.vertexList[fromVertex].next.append(toVertex)
        # self.vertexList[toVertex].next.append(fromVertex)
    def removeVertex(self,vertex):
        if vertex in self.vertexList:
            removed = self.vertexList.pop(vertex)
            removed = removed.name
            for key, vertex in self.vertexList.items():
                if removed in vertex.next:
                    vertex.next.remove(removed)

    def removeEdge(self,fromVertex,toVertex):
        if fromVertex not in self.vertexList:
            if fromVertex not in self.vertexList:
                print("vertexList has no ", fromVertex)
                return
            if toVertex not in self.vertexList:
                print("vertexList has no ", toVertex)
                return
        if fromVertex in self.vertexList[toVertex].next:
            self.vertexList[fromVertex].next.remove(toVertex)
            self.vertexList[toVertex].next.remove(fromVertex)
    def clique_check(self,nodelist):

        for n in range(len(nodelist)):
            temp_list=copy.deepcopy(nodelist)
            a=temp_list.pop(n)
            for m in temp_list:
                if m not in self.vertexList[a].next:
                    return False
        
        return True
        """
        a=nodelist.pop(0)
        for i in nodelist:
            if i not in self.vertexList[a].next:
                return False
            else:
                return True
        """
    def edge_list(self):
        edge_list=[]
        for i in self.vertexList.keys():
            for n in self.vertexList[i].next:
                #print([i,n])
                if i!=n and i<n:
                    edge_list.append([i,n])
        #edge_list=set(edge_list)
        return edge_list
    def findNonadjecentnode(self):
        non_adj={}

        for i in self.vertexList.keys():
            vertexList=[]
            a=self.vertexList[i].next
            a.append(i)
            vertexList= list(set(self.vertexList.keys()).difference(set(a)))
            non_adj[i]=vertexList
        return non_adj
    def BFS_search(self,start_point,end_point):
        search_queue=deque()
        search_queue+=self.vertexList[start_point].next
        searched=[]
        while search_queue:
            next_node=search_queue.popleft()
            if not next_node in searched:
                if next_node==end_point:
                    return True
                else:
                    searched.append(next_node)
                    Check_List=self.vertexList[next_node].next
                    if next_node in Check_List:
                       Check_List.remove(next_node)
                    search_queue+=Check_List
        return False

    def BFS_search_chordless(self,start_point,end_point,W_set):
        Flag=False
        W_set.append(end_point)
        past={}
        search_queue=deque()
        first=copy.deepcopy(self.vertexList[start_point].next)
        for i in first:
            if (i==start_point):
                first.remove(i)
        for i in first:
            if (i==start_point):
                first.remove(i)
        past[start_point]=first
        search_queue+=first
        searched=[start_point]
        while search_queue:
            next_node=search_queue.popleft()
            if  (next_node not in searched) and (next_node in W_set):
                if next_node==end_point:
                    Flag=True
                    break
                else:
                    searched.append(next_node)
                    Check_List=self.vertexList[next_node].next
                    if next_node in Check_List:
                       Check_List.remove(next_node)
                    second=copy.deepcopy(Check_List)
                    for i in second:
                        if i in searched:
                            second.remove(i)
                    past[next_node]=second
                    search_queue+=second

        path_SET=[]
        if(Flag==True):
            temp=[]
            for i in searched:
                for n in past[i]:
                    temp=[i,n]
                    path_SET.append(temp)
            record=[]
            num=0
            while (path_SET):
                num+=1
                a=path_SET.pop(0)
                for n in path_SET:
                    if n[0]==a[-1]:
                        temp=(a[0:len(a)-1]+n)
                        path_SET.insert(0,temp)
                        record.append(temp)
                        path_SET.remove(n)
                if num>50:
                    break
            for n in record:
                if(n[0]==start_point and n[-1]==end_point):
                    chordlesspath=n
                    return chordlesspath
                    break
        return False







#test
