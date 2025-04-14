class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return print ('total nodes in linked list are' ,self.n)

    def insert_head(self,value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

        self.n = self.n +1 
    


    def append (self,value):
        new_node = Node(value)

        if self.head == None:
              self.head = new_node
              self.n = self.n+1
              return
            
        else: 
            current = self.head
            while current.next != None:
               current = current.next 

        current.next = new_node
        self.n = self.n+1



    def insert_bw (self,after_value, value):
        self.after_value = after_value
        new_node = Node(value)
        current = self.head

        if self.head == None:
            self.head = new_node
            self.n = self.n+1
            return    
        
        while current.data != after_value  :
             if current.data == after_value:
                  break
             current = current.next
             
        if current == None:
            print("not found")        

        new_node.next = current.next
        current.next = new_node
        self.n +=1
        
        
            

    def clear(self):
        self.head = None
        self.n = 0



    def delete_head(self):
        if self.head == None:
          return  print("Empty list")
        
        self.head = self.head.next 
        self.n -= 1



    def pop(self):

        if self.head == None:
           return self.delete_head()
         
        current = self.head
        print("after poping")
        if current.next == None:
           return self.delete_head()

        
        if self.head == None:
            return print('empty list ')

        while current.next.next != None:
             current = current.next 
        current.next = None
        self.n -= 1    
     

    def delete_by_value(self,value):
        if self.head == None:
            return print("Empty linked list ")
        print('Ater delete the {} from linked list '.format(value))
        
        current = self.head 
        if current.data == value:
           
            return self.delete_head()
        
        while current.next != None:
           if current.next.data == value:
               break
           current = current.next  

        #found the value:::
        if current.next == None:
            return print('Not found')
        else:
            current.next = current.next.next 
        self.n -= 1


    def search (self,value):
        if self.head == None:
            return print("Nothing to search in empty linked list ")
         
        current = self.head 
        number = 0

        while current != None:
            if current.data == value:
               return print('the value {} is found at index {}'.format(value, number))
             
            current = current.next
            number += 1
       
        return print("Item not in list ")
        

    def __getitem__(self,index):
        if self.head == None:
            return print("Nothing to search in empty linked list ")
         
        current = self.head 
        number = 0
        while current != None:
            if number == index:
                return print('after searcing_by_index {} found at {} index number'.format(index,current.data))
            current = current.next 
            number +=1

        return print('after searcing_by_index nothing found at {}'.format(index))    
        

    def replace_max(self,value):
        if self.head == None:
            return print("Nothing to replace in empty linked list ")
        
        temp= self.head
        max= temp

        while temp != None:
            if temp.data > max.data:
                max = temp
            temp = temp.next

        max.data = value

    def sum_odd_nodes(self):
        sum = 0
        index = 0
        temp = self.head
        while temp != None:
            if index%2 == 1:
                sum = sum + temp.data
            temp = temp.next 
            index+= 1
        return print('The sum of odd_indices in linked list is {}'.format(sum)  )       

    
    def reverse_linked_list(self):
        prev_node = None
        current = self.head
        

        while current != None:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

        self.head = prev_node
        return print("After reversing the linked list :\n{}".format(l))

    def change_linked_list(self):
        temp = self.head
        while temp!= None:
            if temp.data == '*' or temp.data == '/':
                temp.data = ' '
                if temp.next.data =='*' or temp.next.data == '/':
                    temp.next.next.data =temp.next.next.data.upper()
                    temp.next = temp.next.next 

            temp = temp.next 




    def traverse(self):
        current = self.head
        while current!= None:
            print(current.data, end = '')
            current = current.next 


    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result = result + str(current.data)+ '->'

            current = current.next   
        return result [:-2]      



l = Linked_list()
'''#l.insert_head(4)
#l.insert_head(3)
#l.insert_head(2)
#l.insert_head(1)
#l.pop()
#l.__len__()


#l.delete_by_value(1)
l.replace_max(5)
l.search(0)
l.sum_odd_nodes()
l.__getitem__(2)
l.__len__()
print(l)
l.reverse_linked_list()
l.traverse()'''

l.append('T')
l.append('h')
l.append('e')
l.append('/')
l.append('*')
l.append('S')
l.append('k')
l.append('y')
l.append('*')
l.append('i')
l.append('s')
l.append('/')
l.append('/')
l.append('b')
l.append("l")
l.append("u")
l.append("e")
print(l)
l.change_linked_list()
l.traverse()