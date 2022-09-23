class Stack:
    
    def __init__(self):
        '''A new empty stack'''
        self.items = []
    
    def push(self, o):
        '''Make o the new top item in this Stack.'''
        self.items.append(o)
        
    def pop(self):
        '''Remove and return the top item.'''
        return self.items.pop()
    
    def peek(self):
        '''Return the top item.'''
        return self.items[-1]
    
    def isEmpty(self):
        '''Return whether this stack is empty.'''   # This is like a Javadoc comment.
        return self.items == []
    
    def size(self):
        '''Return the number of items in this stack.'''
        return len(self.items)

action=Stack()
redone=Stack()

class WordProc:
    def __init__(self):
        self.word=[]

    def app(self,add):
        self.word.append(add)
        action.push([add, 'a'])
        print (self.word)

    def delete(self):
        x=int(input('Which line do you wish to delete?'))
        ind=(x-1)
        delt=self.word.pop(ind)
        action.push([delt,'d', ind])
        print (self.word)

    def undo(self):
        if action.isEmpty()==False:
            un=action.pop()
            redone.push(un)
            if un[1] == 'd':
                self.word.insert(un[2], un[0])
                print (self.word)
                
            elif un[1] == 'a':
                self.word.remove(un[0])
                print (self.word)
        else:
            print ('No more actions to undo')
            
    def redo(self):
        if redone.isEmpty()==False:
            re=redone.pop()
            action.push(re)
            
            if re[1] == 'd':
                x=self.word.pop(re[2])
                print (self.word)
                
            elif re[1] == 'a':
                self.word.append(re[0])
                print (self.word)
        else:
            print ('No more actions to redo')


Test=WordProc()

x='0'

while x != '':
    
    x=(raw_input('command?\n'))
    
    if x == 'd':
        Test.delete()
        
    elif x == 'undo':
        Test.undo()
        
    elif x=='redo':
        Test.redo()
        
    else:
        Test.app(x)

