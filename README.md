# Linked List Implementation in Python

This Python code provides a comprehensive implementation of a singly linked list data structure with various operations. Below is a detailed explanation of the code and its functionality.

## Code Structure

### Node Class
```python
class Node:
    def __init__(self, value):
        self.data = value  # Stores the node's value
        self.next = None   # Pointer to the next node
```

### Linked List Class
```python
class Linked_list:
    def __init__(self):
        self.head = None  # Points to the first node
        self.n = 0       # Tracks the number of nodes
```

## Key Methods

### 1. Insertion Operations

**Insert at Head**
```python
def insert_head(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
    self.n += 1
```
- Adds a new node at the beginning
- Time Complexity: O(1)

**Append (Insert at Tail)**
```python
def append(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
    else:
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    self.n += 1
```
- Adds a new node at the end
- Time Complexity: O(n)

**Insert Between Nodes**
```python
def insert_bw(self, after_value, value):
    new_node = Node(value)
    current = self.head
    
    while current and current.data != after_value:
        current = current.next
        
    if not current:
        print("Value not found")
        return
        
    new_node.next = current.next
    current.next = new_node
    self.n += 1
```
- Inserts after a specified value
- Time Complexity: O(n)

### 2. Deletion Operations

**Delete Head**
```python
def delete_head(self):
    if not self.head:
        print("Empty list")
        return
    self.head = self.head.next
    self.n -= 1
```
- Removes the first node
- Time Complexity: O(1)

**Pop (Delete Tail)**
```python
def pop(self):
    if not self.head:
        print("Empty list")
        return
        
    if not self.head.next:
        self.head = None
    else:
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    self.n -= 1
```
- Removes the last node
- Time Complexity: O(n)

**Delete by Value**
```python
def delete_by_value(self, value):
    if not self.head:
        print("Empty list")
        return
        
    if self.head.data == value:
        self.head = self.head.next
    else:
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
            
        if not current.next:
            print("Value not found")
            return
            
        current.next = current.next.next
    self.n -= 1
```
- Removes the first occurrence of a value
- Time Complexity: O(n)

### 3. Utility Operations

**Search**
```python
def search(self, value):
    current = self.head
    index = 0
    while current:
        if current.data == value:
            print(f"Value {value} found at index {index}")
            return
        current = current.next
        index += 1
    print("Value not found")
```
- Searches for a value
- Time Complexity: O(n)

**Get Item by Index**
```python
def __getitem__(self, index):
    current = self.head
    count = 0
    while current:
        if count == index:
            return current.data
        current = current.next
        count += 1
    raise IndexError("Index out of range")
```
- Accesses node by index
- Time Complexity: O(n)

**Reverse List**
```python
def reverse_linked_list(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev
```
- Reverses the linked list in-place
- Time Complexity: O(n)

### 4. Special Operations

**Replace Maximum Value**
```python
def replace_max(self, value):
    if not self.head:
        print("Empty list")
        return
        
    max_node = self.head
    current = self.head.next
    
    while current:
        if current.data > max_node.data:
            max_node = current
        current = current.next
        
    max_node.data = value
```
- Finds and replaces the maximum value
- Time Complexity: O(n)

**Sum Odd Indexed Nodes**
```python
def sum_odd_nodes(self):
    sum = 0
    index = 1  # Starting from first odd index (1)
    current = self.head
    
    while current:
        if index % 2 == 1:
            sum += current.data
        current = current.next
        index += 1
        
    return sum
```
- Sums values at odd indices (1, 3, 5...)
- Time Complexity: O(n)

### 5. String Representation

```python
def __str__(self):
    elements = []
    current = self.head
    while current:
        elements.append(str(current.data))
        current = current.next
    return "->".join(elements)
```
- Creates a string representation of the list
- Example: "1->2->3"

## Example Usage

```python
l = Linked_list()
l.append('T')
l.append('h')
l.append('e')
l.append('/')
l.append('*')
l.append('S')
l.append('k')
l.append('y')
print(l)  # Output: T->h->e->/->*->S->k->y

l.reverse_linked_list()
print(l)  # Output: y->k->S->*->/->e->h->T

l.delete_by_value('*')
print(l)  # Output: y->k->S->/->e->h->T
```

## Special Text Processing Method

```python
def change_linked_list(self):
    current = self.head
    while current:
        if current.data in ['*', '/']:
            current.data = ' '
            if current.next and current.next.data in ['*', '/']:
                if current.next.next:
                    current.next.next.data = current.next.next.data.upper()
                    current.next = current.next.next
        current = current.next
```

This method:
1. Replaces '*' or '/' with a space
2. If two special characters appear consecutively:
   - Replaces them with a single space
   - Capitalizes the next character
3. Example: "The/*Sky" becomes "The Sky"

## Time Complexity Summary

| Operation          | Time Complexity |
|--------------------|-----------------|
| insert_head        | O(1)            |
| append             | O(n)            |
| insert_bw          | O(n)            |
| delete_head        | O(1)            |
| pop                | O(n)            |
| delete_by_value    | O(n)            |
| search             | O(n)            |
| __getitem__        | O(n)            |
| reverse_linked_list| O(n)            |
| replace_max        | O(n)            |
| sum_odd_nodes      | O(n)            |

This implementation provides a solid foundation for working with linked lists in Python, with operations for insertion, deletion, searching, and various utility functions.
