class Contact:

    def __init__(self, name, number, next=None):
        self.name = name
        self.number = number
        self.next = next
    

class Node:
     def __init__(self, key, value, next=None):
         self.key = key
         self.value = value
         self.next = next

     def __str__(self):
         return f" {self.key}: {self.value}"
        

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size 
    
    def insert(self, key, value):
        index = self.hash_function(key)

        if self.data[index] is None:
            self.data[index] = Node(key, value)
            return

        current = self.data[index]
        while True:

            if current.key == key:
                current.value = value
                return

            if current.next is None:
                break
            current = current.next

        current.next = Node(key, value)
    

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    

    def print_table(self):
        for i in range(self.size):
            if self.data[i] is None:
                print(f"Index {i}: Empty")
            else:
                current = self.data[i]
                chain = ""
                while current:
                    chain += str(current) + " "
                    current = current.next
                print(f"Index {i}: -{chain}")

    
    

# Test your hash table implementation here.  
'''
contact_1 = Contact("Riley", "123-456-7890", None)
node_1 = Node(contact_1.name, contact_1.number, None)
print(node_1.key) # Riley 
print(node_1.value) # Riley: 123-456-7890 
print(node_1.next) # None 
'''
table = HashTable(10)
table.print_table()

table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
table.print_table()

contact = table.search("John") 
print("\nSearch result:", contact) 

table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")  # May collide with Amy depending on hash function 
table.print_table()

table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number 
table.print_table()

print(table.search("Chris"))