class Stack:
    
    def __init__(self):
        '''A new empty stack'''
        self.s = []
    
    def push(self, o):
        '''Make o the new top item in this Stack.'''
        self.s.append(o)
        
    def pop(self):
        '''Remove and return the top item.'''
        return self.s.pop()
    
    def peek(self):
        '''Return the top item.'''
        return self.s[-1]
    
    def isEmpty(self):
        '''Return whether this stack is empty.'''   # This is like a Javadoc comment.
        return self.s == []
    
    def size(self):
        '''Return the number of items in this stack.'''
        return len(self.s)

    def swap(self):
        '''swap top two items of stack s'''
        #pop item at top
        first = self.s.pop()
        #pop item second from top
        second = self.s.pop()
        #add back first item
        self.push(first)
        #add second item above first item
        self.push(second)
    
    def roll(self, x):
        '''perform the roll operation on a stack s.
        A roll with integer n causes the nth item from the top to be removed
        and placed on top of the stack.'''
        #pop item from given index, counting from top
        item = self.s.pop(-x)
        #push popped item back to the top.
        self.push(item)
    
Test = Stack()
Test.s.append('a')
Test.s.append('b')
Test.s.append('c')

Test.swap()
#prints a, c, b
print(Test.s)


Test.roll(2)
#prints a, b, c
print(Test.s)
Test.roll(3)
#prints b, c, a
print(Test.s)