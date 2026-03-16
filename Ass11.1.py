Task 01 :
  # Generate a Python class implementation for a Stack data structure.
# Include the following methods: push(), pop(), peek(), and is_empty().
# Use a Python list internally to store stack elements.
# Add proper docstrings and comments explaining each method.
# Also include a simple example demonstrating stack operations.
class Stack:
    """
    A Stack data structure implementation using a Python list.
    The Stack follows the Last In First Out (LIFO) principle.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Parameters:
        item: The item to be added to the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Remove and return the item at the top of the stack.

        Returns:
        The item at the top of the stack.

        Raises:
        IndexError: If the stack is empty when trying to pop an item.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """
        Return the item at the top of the stack without removing it.

        Returns:
        The item at the top of the stack.

        Raises:
        IndexError: If the stack is empty when trying to peek an item.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
        True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0
# Example usage of the Stack class
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Top item (peek):", stack.peek())  # Output: 3
    print("Stack is empty:", stack.is_empty())  # Output: False

    print("Popped item:", stack.pop())  # Output: 3
    print("Top item after pop (peek):", stack.peek())  # Output: 2

    stack.pop()
    stack.pop()
    print("Stack is empty after popping all items:", stack.is_empty())  # Output: True
    # Uncommenting the following line will raise an error because the stack is empty
    # stack.pop()  # This will raise an IndexError
    # Uncommenting the following line will raise an error because the stack is empty
    # stack.peek()  # This will raise an IndexError
Task 02 :
  # Create a Python class for a Queue using a Python list.
# The queue should follow the FIFO principle.
# Implement the methods enqueue(), dequeue(), peek(), and size().
# Include proper comments and docstrings.
# Also provide a small example showing how the queue works.
class Queue:
    """
    A Queue data structure implementation using a Python list.
    The Queue follows the First In First Out (FIFO) principle.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []

    def enqueue(self, item):
        """
        Add an item to the end of the queue.

        Parameters:
        item: The item to be added to the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.

        Returns:
        The item at the front of the queue.

        Raises:
        IndexError: If the queue is empty when trying to dequeue an item.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        """
        Return the item at the front of the queue without removing it.

        Returns:
        The item at the front of the queue.

        Raises:
        IndexError: If the queue is empty when trying to peek an item.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]

    def size(self):
        """
        Return the number of items in the queue.

        Returns:
        The size of the queue.
        """
        return len(self.queue)

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
        True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

# Example usage of the Queue class
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Front item (peek):", queue.peek())  # Output: 1
    print("Queue size:", queue.size())  # Output: 3
    print("Queue is empty:", queue.is_empty())  # Output: False

    print("Dequeued item:", queue.dequeue())  # Output: 1
    print("Front item after dequeue (peek):", queue.peek())  # Output: 2

    queue.dequeue()
    queue.dequeue()
    print("Queue is empty after dequeuing all items:", queue.is_empty())  # Output: True
Task 03 :
  # Write Python code to implement a Singly Linked List.
# Create a Node class and a LinkedList class.
# Include methods to insert elements and display the list.
# Add clear docstrings and comments explaining each method.
# Provide an example showing insertion and display operations.
class Node:
    """
    A Node class for a singly linked list.
    Each node contains data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Initialize a new node with the given data.

        Parameters:
        data: The value to be stored in the node.
        """
        self.data = data
        self.next = None
class LinkedList:
    """
    A LinkedList class to manage a singly linked list.
    It provides methods to insert elements and display the list.
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert(self, data):
        """
        Insert a new node with the given data at the end of the list.

        Parameters:
        data: The value to be stored in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        """
        Display the elements of the linked list.

        Returns:
        A string representation of the linked list.
        """
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(elements)
# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    print("Linked List:", linked_list.display())
    # Output: Linked List: 10 -> 20 -> 30
Task 04 :
  # Write Python code to implement a Singly Linked List.
# Create a Node class and a LinkedList class.
# Include methods to insert elements and display the list.
# Add clear docstrings and comments explaining each method.
# Provide an example showing insertion and display operations.
class Node:
    """
    A Node class for a singly linked list.
    Each node contains data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Initialize a new node with the given data.

        Parameters:
        data: The value to be stored in the node.
        """
        self.data = data
        self.next = None
class LinkedList:
    """
    A LinkedList class to manage a singly linked list.
    It provides methods to insert elements and display the list.
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert(self, data):
        """
        Insert a new node with the given data at the end of the list.

        Parameters:
        data: The value to be stored in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        """
        Display the elements of the linked list.

        Returns:
        A string representation of the linked list.
        """
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(elements)
# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    print("Linked List:", linked_list.display())
    # Output: Linked List: 10 -> 20 -> 30
Task 05 :
  # Implement a Hash Table in Python.
# Include methods insert(), search(), and delete().
# Use chaining (linked list or list of lists) for collision handling.
# Add proper comments and docstrings to explain the implementation.
# Also include an example demonstrating insertion, searching, and deletion.
class HashTable:
    """
    A Hash Table implementation using chaining for collision handling.
    The hash table supports insertion, searching, and deletion of key-value pairs.
    """

    def __init__(self, size=10):
        """
        Initialize the hash table with a specified size.

        Parameters:
        size: The number of buckets in the hash table (default is 10).
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Compute the hash value for a given key.

        Parameters:
        key: The key to be hashed.

        Returns:
        The hash value corresponding to the key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.

        Parameters:
        key: The key to be inserted.
        value: The value associated with the key.
        """
        index = self._hash(key)
        # Check if the key already exists and update its value
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # If the key does not exist, add a new key-value pair
        self.table[index].append((key, value))

    def search(self, key):
        """
        Search for a value associated with a given key.

        Parameters:
        key: The key to be searched.

        Returns:
        The value associated with the key if found, otherwise None.
        """
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.

        Parameters:
        key: The key to be deleted.
        """
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
# Example usage of the HashTable class
if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.insert("name", "Alice")
    hash_table.insert("age", 30)
    hash_table.insert("city", "New York")

    print("Search for 'name':", hash_table.search("name"))  # Output: Alice
    print("Search for 'age':", hash_table.search("age"))    # Output: 30
    print("Search for 'city':", hash_table.search("city"))  # Output: New York

    hash_table.delete("age")
    print("Search for 'age' after deletion:", hash_table.search("age"))  # Output: None 
Task 06 :
  # Write Python code to implement a Graph using an adjacency list representation.
# Include methods add_vertex(), add_edge(), and display_graph().
# Add comments and docstrings explaining each method.
# Also include an example showing how vertices and edges are added.
class Graph:
    """
    A Graph class implemented using an adjacency list representation.
    The graph supports adding vertices, adding edges, and displaying the graph.
    """
    
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.

        Parameters:
        vertex: The vertex to be added to the graph.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Add an edge between two vertices in the graph.

        Parameters:
        vertex1: The first vertex of the edge.
        vertex2: The second vertex of the edge.
        """
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def display_graph(self):
        """
        Display the adjacency list representation of the graph.

        Returns:
        A string representation of the graph.
        """
        result = []
        for vertex, edges in self.graph.items():
            result.append(f"{vertex}: {', '.join(edges)}")
        return "\n".join(result)
# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    print(graph.display_graph())
Task 07 :
  # Create a Python class implementing a Priority Queue using the heapq module.
# Include methods enqueue(item, priority), dequeue(), and display().
# Ensure that elements with higher priority are removed first.
# Add clear docstrings and comments explaining the implementation.
# Include an example demonstrating priority queue operations.
import heapq
class PriorityQueue:
    """
    A Priority Queue implementation using the heapq module.
    Elements with higher priority are removed first.
    """

    def __init__(self):
        """Initialize an empty priority queue."""
        self.elements = []

    def enqueue(self, item, priority):
        """
        Add an item to the priority queue with a given priority.

        Parameters:
        item: The item to be added to the queue.
        priority: The priority of the item (lower values indicate higher priority).
        """
        heapq.heappush(self.elements, (priority, item))

    def dequeue(self):
        """
        Remove and return the item with the highest priority from the queue.

        Returns:
        The item with the highest priority.

        Raises:
        IndexError: If the priority queue is empty when trying to dequeue an item.
        """
        if not self.elements:
            raise IndexError("Dequeue from an empty priority queue")
        return heapq.heappop(self.elements)[1]

    def display(self):
        """
        Display the elements in the priority queue in order of their priorities.

        Returns:
        A string representation of the priority queue.
        """
        return ", ".join(f"{item} (priority {priority})" for priority, item in sorted(self.elements))
# Example usage:
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Task A", priority=2)
    pq.enqueue("Task B", priority=1)
    pq.enqueue("Task C", priority=3)
    print("Priority Queue:", pq.display())
    print("Dequeue:", pq.dequeue())
    print("Priority Queue after dequeue:", pq.display())
Task 08 :
  # Implement a double-ended queue (Deque) in Python using collections.deque.
# Include methods insert_front(), insert_rear(), remove_front(), and remove_rear().
# Add proper comments and docstrings explaining each operation.
# Provide a small example demonstrating deque usage.
from collections import deque
class Deque:
    """
    A Deque (double-ended queue) implementation using collections.deque.
    The Deque allows insertion and removal of elements from both ends.
    """

    def __init__(self):
        """Initialize an empty deque."""
        self.deque = deque()

    def insert_front(self, item):
        """
        Insert an item at the front of the deque.

        Parameters:
        item: The item to be inserted at the front of the deque.
        """
        self.deque.appendleft(item)

    def insert_rear(self, item):
        """
        Insert an item at the rear of the deque.

        Parameters:
        item: The item to be inserted at the rear of the deque.
        """
        self.deque.append(item)

    def remove_front(self):
        """
        Remove and return the item at the front of the deque.

        Returns:
        The item at the front of the deque.

        Raises:
        IndexError: If the deque is empty when trying to remove an item from the front.
        """
        if self.is_empty():
            raise IndexError("Remove from an empty deque")
        return self.deque.popleft()

    def remove_rear(self):
        """
        Remove and return the item at the rear of the deque.

        Returns:
        The item at the rear of the deque.

        Raises:
        IndexError: If the deque is empty when trying to remove an item from the rear.
        """
        if self.is_empty():
            raise IndexError("Remove from an empty deque")
        return self.deque.pop()

    def is_empty(self):
        """
        Check if the deque is empty.

        Returns:
        True if the deque is empty, False otherwise.
        """
        return len(self.deque) == 0
# Example usage of the Deque class
if __name__ == "__main__":
    my_deque = Deque()
    my_deque.insert_rear(10)
    my_deque.insert_rear(20)
    my_deque.insert_front(5)

    print("Deque after insertions:", list(my_deque.deque))  # Output: [5, 10, 20]

    print("Removed from front:", my_deque.remove_front())  # Output: 5
    print("Removed from rear:", my_deque.remove_rear())    # Output: 20

    print("Deque after removals:", list(my_deque.deque))   # Output: [10]
task 09 :
# Analyze the following campus management features and suggest the most suitable data structure for each:
# 1. Student Attendance Tracking
# 2. Event Registration System
# 3. Library Book Borrowing
# 4. Bus Scheduling System
# 5. Cafeteria Order Queue

# Choose from: Stack, Queue, Priority Queue, Linked List, Binary Search Tree, Graph, Hash Table, Deque.

# Provide a table mapping:
# Feature → Data Structure → Justification (2–3 sentences).

# Then implement one selected feature as a Python program with comments and docstrings.
# Feature → Data Structure → Justification
# 1. Student Attendance Tracking → Hash Table → A hash table allows for efficient storage and
# retrieval of student attendance records using student IDs as keys, providing O(1) average time complexity for lookups.
# 2. Event Registration System → Queue → A queue is suitable for managing event registrations as it follows the First In First Out (FIFO) principle, ensuring that registrations are processed in the order
# they were received.
# 3. Library Book Borrowing → Linked List → A linked list can efficiently manage the borrowing and returning of books, allowing for dynamic memory allocation and easy insertion and deletion of book records.      
# 4. Bus Scheduling System → Graph → A graph is ideal for representing bus routes and stops, allowing for efficient pathfinding algorithms to determine the best routes and schedules.
# 5. Cafeteria Order Queue → Queue → A queue is perfect for managing cafeteria orders as it ensures that orders are processed in the order they were placed, providing a fair and organized system for both customers and staff.
# Implementing the Cafeteria Order Queue using a Queue data structure.
class CafeteriaOrderQueue:  
    """
    A class to manage cafeteria orders using a Queue data structure.
    This class allows for adding orders to the queue and processing them in a First In First Out (FIFO) manner.
    """

    def __init__(self):
        """Initialize an empty order queue."""
        self.orders = []

    def place_order(self, order):
        """
        Place a new order in the queue.

        Parameters:
        order: A string representing the customer's order.
        """
        self.orders.append(order)
        print(f"Order placed: {order}")

    def process_order(self):
        """
        Process the next order in the queue.

        Returns:
        The order that was processed.

        Raises:
        IndexError: If there are no orders to process.
        """
        if self.is_empty():
            raise IndexError("No orders to process")
        order = self.orders.pop(0)
        print(f"Order processed: {order}")
        return order

    def peek_next_order(self):
        """
        Peek at the next order in the queue without processing it.

        Returns:
        The next order in the queue.

        Raises:
        IndexError: If there are no orders to peek at.
        """
        if self.is_empty():
            raise IndexError("No orders to peek at")
        return self.orders[0]

    def is_empty(self):
        """
        Check if the order queue is empty.

        Returns:
        True if the queue is empty, False otherwise.
        """
        return len(self.orders) == 0
# Example usage of the CafeteriaOrderQueue class
if __name__ == "__main__":
    cafeteria_queue = CafeteriaOrderQueue()
    cafeteria_queue.place_order("Burger and Fries")
    cafeteria_queue.place_order("Salad")
    cafeteria_queue.place_order("Pizza")
    
    print(f"Next order to process: {cafeteria_queue.peek_next_order()}")
    
    cafeteria_queue.process_order()
    print(f"Next order to process: {cafeteria_queue.peek_next_order()}")
    
    cafeteria_queue.process_order()
    cafeteria_queue.process_order()
    
    print(f"Is the order queue empty? {cafeteria_queue.is_empty()}")
    
