# HW 5
# Due Date: 12/07/2018, 11:59PM
########################################
#
# Name:Jess Walsh
# Collaboration Statement:
#
########################################

# ---Copy your code from labs 9 and 10 here (you can remove their comments)


# ----- HW5 Graph code
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top, out))

    __repr__ = __str__

    def isEmpty(self):
        # write your code here
        return self.top == None

    def __len__(self):
        # write your code here
        if self.isEmpty():
            return 'Stack is empty'
        current= self.top
        count = 1
        while currentnode.next != None:
            currentnode = currentnode.next
            count = count + 1
        return count

    def peek(self):
        # write your code here
        if self.isEmpty():
            return 0
        max = 0
        currentnode = self.top
        while currentnode != None:
            if currentnode.value > max:
                max = currentnode.value
            currentnode = currentnode.next
        return max

    def push(self, value):
        # write your code here
        newnode = Node(value)
        if not self.isEmpty():
            newnode.next = self.top
            self.top = newnode
        self.top = newnode

    def pop(self):
        # write your code here
        currentnode = self.top
        if self.isEmpty():
            return 'Stack is empty'
        else:
            self.top = currentnode.next
            currentnode.next = None
            return currentnode.value

class Queue:

    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        #write your code here
        return self.head == None

    def __len__(self):
        #write your code here
            currentNode = self.head
            count = 0
            while currentNode != None:
                currentNode = currentNode.next
                count += 1
            return count

    def enqueue(self, value):
        #write your code here
        currentNode = Node(value)
        if self.isEmpty():
            self.head = currentNode
            self.tail = currentNode
        else:
            self.tail.next = currentNode
            self.tail = currentNode

    def dequeue(self):
        #write your code here
        if self.isEmpty():
            return 'Queue is empty'
        elif self.__len__() == 1:
            val = self.head.value
            self.head = None
            self.tail = None
        else:
            val = self.head.value
            temp = self.head.next
            self.head.next = None
            self.head = temp
        return val



class Graph:
    def __init__(self, graph_repr=None):
        if graph_repr is None:
            self.vertList = {}
        else:
            self.vertList = graph_repr

    def addVertex(self, key):
        if key not in self.vertList:
            self.vertList[key] = []
            return self.vertList

    def addEdge(self, frm, to, cost=1):
        if frm not in self.vertList:
            self.addVertex(frm)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[frm].append((to, cost))
        return self.vertList

    def bfs(self, start):
# Your code starts here
        if not start in self.vertList or not isinstance(start, str):
            return 'error'
        path = [] 
        q = Queue()
        path.append(start)
        q.enqueue(start)

        while True:
            x =q.dequeue()
            for i in sorted(self.vertList[x]):
                if not isinstance(i, str):
                    i = i[0]
                if i not in path:
                    path.append(i)
                    q.enqueue(i)
            if q.isEmpty():
                return path

    def dfs(self, start):
    # Your code starts here
        if not start in self.vertList or not isinstance(start,str):
            return 'error'
        path=[]
        path.append(start)
        s = Stack()
        s.push(start)

        while True:
            x = s.top.value
            temp = True
            for i in sorted(self.vertList[x]):
                if not isinstance(i, str):
                    i = i[0]
                if i not in path:
                    path.append(i)
                    s.push(i)
                    temp = False
                    break
            if temp:
                s.pop()
            if s.isEmpty():
                return path



### EXTRA CREDIT, uncomment method definition if submitting extra credit

    def dijkstra(self,start):
        # Your code starts here
        if not start in self.vertList or not isinstance(start, str):
            return 'error'

        lst_final = {}
        queue_One = Queue()
        queue_Two = Queue()

        queue_One.enqueue(0)
        queue_Two.enqueue(start)

        for i in sorted(self.vertList):
            lst_final[i]=None
        while True:
            for i in sorted(self.vertList[queue_Two.head.value], key=lambda x:x[1]):
                if lst_final[i[0]]==None or queue_One.head.value + i[1] < lst_final[i[0]]:
                    lst_final[i[0]] = queue_One.head.value + i[1]
                    queue_One.enqueue(queue_One.head.value + i[1])
                    queue_Two.enqueue(i[0])
            if lst_final[queue_Two.head.value]==None or queue_One.head.value < lst_final[queue_Two.head.value]:
                lst_final[queue_Two.dequeue()] = queue_One.dequeue()
            else:
                queue_Two.dequeue()
                queue_One.dequeue()
            if queue_One.isEmpty():
                stack = Stack()
                list(map(lambda x: stack.push(x), filter(lambda x: lst_final[x]==None, [j for j in lst_final])))

                while not stack.isEmpty():
                    del lst_final[stack.pop()]
                return lst_final
