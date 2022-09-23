#------------------------------1--------------------------------------------
def sum_math_average(x):
    for ind in range(0,len(x)):
        first=x[ind]['V']
        second=x[ind]['VI']
        avrg=(second+first)/2
        x[ind]["V+VI"]=avrg
        x[ind].pop('V')
        x[ind].pop('VI')
        print (x[ind])
    
student_details = [{'id': 1, 'subject': 'math', 'V': 70, 'VI' : 82},
{'id': 2, 'subject': 'math', 'V': 73, 'VI' : 74},
 {'id': 3, 'subject': 'math', 'V': 75, 'VI' : 86}]
sum_math_average(student_details)

#------------------------------2--------------------------------------------
class Stack:
    def __init__(self):
        self.items = []
 
    def isEmpty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
Palin = Stack()

def check(text):
    for x in text:
        Palin.push(x)
        
    Palindrome=''
    while Palin.isEmpty()==False:
        Palindrome = Palindrome + Palin.pop()
     
    if text == Palindrome:
        print('The string is a palindrome.')
    elif text != Palindrome:
        print('The string is not a palindrome.')

check('madam')

#------------------------------3--------------------------------------------

class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
            return len(self.items)