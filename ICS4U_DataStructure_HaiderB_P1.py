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

#stacks to hold actions for undo and redo
action=Stack()
redone=Stack()

class WordProc:
    def __init__(self):
        '''a new empty stack'''
        self.word=[]

    def app(self,add):
        '''append to the list'''
        self.word.append(add)
        #also add to the action list, for when need to undo. Letter a represents that item has been appended
        action.push([add, 'a'])
        print (self.word)

    def delete(self):
        '''Remove word from list'''
        x=int(input('Which line do you wish to delete?'))
        ind=(x-1)
        delt=self.word.pop(ind)
        #Add to actions list, d represents 'delete', and the index is also given for when undo is needed
        action.push([delt,'d', ind])
        print (self.word)

    def undo(self):
        '''undo an action'''
        #Only start is list isnt empty
        if action.isEmpty()==False:
            #Pop the latest action done
            un=action.pop()
            #Also send it to redone list, for when need to redo
            redone.push(un)
            if un[1] == 'd':
                #If 'd', it means item was deleted, so add it back at specific index
                self.word.insert(un[2], un[0])
                print (self.word)
                
            elif un[1] == 'a':
                #if 'a', means item was appended, so delete it
                self.word.remove(un[0])
                print (self.word)
        else:
            #if list empty, let user know
            print ('No more actions to undo')
            
    def redo(self):
        '''redo undone action'''
        #start if not empty
        if redone.isEmpty()==False:
            #pop from redo list
            re=redone.pop()
            #send it to undo list if need to undo later
            action.push(re)
            
            if re[1] == 'd':
                #if undone action was deleted, delete it again.
                x=self.word.pop(re[2])
                print (self.word)
                
            elif re[1] == 'a':
                #if undone action was appended, append it again.
                self.word.append(re[0])
                print (self.word)
        else:
            #Let user know if nothing to undo
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

