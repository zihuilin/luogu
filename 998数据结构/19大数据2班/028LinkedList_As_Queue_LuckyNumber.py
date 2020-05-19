class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data #数据
            self.next = None #next链接指向None

    def __init__(self):
        self.head = None  #头部一开始指向None(为空）
        self.tail = None  #尾部一开始指向None(为空）

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def add_to_head(self, new_data):
        new_node = self.Node(new_data) #创建一个节点
        if self.head == None:
            self.tail = new_node
        new_node.next = self.head #让新节点的next引用原来的head
        self.head = new_node #变更head为这个新节点

    def delete_from_head(self):
        #1. 当LinkedList为空时
        if self.head == None:
            return None # None表示没有可以删除的节点
        if self.head == self.tail :
            d = self.head.data  #记录原来头部的数据
            #让head和tail都引用None
            self.head = None
            self.tail = None
        #3. 当多于1个节点的时候：
        else:
            d = self.head.data  #记录原来头部的数据
            #让head引用原来head的next节点
            self.head = self.head.next
        return d
        #还要返回被删除节点中的数据

    def delete_from_tail(self):
        d = None #用来返回被删除的数据
        if self.head == None: #1. 空链表
            d = None
        elif self.head == self.tail: #2. 只有1个节点：
            d = self.tail.data
            self.head = None
            self.tail = None
        else: #3. 使用while循环找tail前面的节点
            d = self.tail.data
            p = self.head
            while p.next != self.tail: #如果p后面不是tail
                p = p.next  #p向后移动
            self.tail = p #更改tail为tail前面的节点
            self.tail.next = None #末尾的next总是None
        return d

    def delete_node(self, data_to_be_deleted):
        d = data_to_be_deleted
        if self.head == None:  #空链表
            return None
        elif self.head == self.tail and self.head.data == d :
            #只有一个节点，这个节点是要删除的节点
            self.head = None
            self.tail = None
            return d
        else:
            if self.head.data == d:
                self.head = self.head.next
                return d
            else: #通过while循环，寻找d前面的节点
                p = self.head
                while p.next != None and p.next.data != d:
                    p = p.next # 向后移动
                if p.next != None:
                    p.next = p.next.next
                    return d
        #没找到。。。
        return None # None表示没有找到要删除的节点


    #创建一个节点，存放new_data，并把这个节点插入到末尾
    def add_to_tail(self, new_data):
        new_node = self.Node(new_data)
        if self.head == None: #空链表
            self.head = new_node
        else: #不是空链表
            self.tail.next = new_node
        self.tail = new_node


    def print_all(self):
        print("head->", end='')
        p = self.head
        while p != None:
            print("(" + str(p.data) + ")->", end='')
            p = p.next
        print("None")

class Queue:
    def __init__(self):
        self.llist = LinkedList()

    def put(self, data): #入队
        self.llist.add_to_tail(data)

    def get(self):    #出队
        return self.llist.delete_from_head()

    def peak(self):   #只看队首，但不出队
        if self.is_empty():
            return None   #空队列
        else:
            return self.llist.head.data

    def is_empty(self): #是否为空队列
        return self.llist.is_empty()

n = int(input())
input_nums = []
max_num = 0
for i in range(n):
    num = int(input())
    if num > max_num:
        max_num = num
    input_nums.append(num)
output_nums = []

#准备3个队列
q3 = Queue()
q5 = Queue()
q7 = Queue()
#最初的3个幸运数，入列
q3.put(3)
q5.put(5)
q7.put(7)

dq_num = 0  #出列的数字，一开始设置为0
count = 0
dq_count = 1
while dq_num != max_num:
    if q3.peak() <= q5.peak() and q3.peak() <= q7.peak():
        dq = q3.get() #q3出列
    elif q5.peak() <= q3.peak() and q5.peak() <= q7.peak():
        dq = q5.get() #q5出列
    else: #q7
        dq = q7.get() #q7出列
    if dq != dq_num: #跟之前不同
        dq_num = dq
        q3.put(dq*3)
        q5.put(dq*5)
        q7.put(dq*7)
        if dq == input_nums[count]:
            output_nums.append(dq_count)
            count = count + 1
        dq_count = dq_count + 1

for i in range(len(output_nums)):
    print(output_nums[i])
