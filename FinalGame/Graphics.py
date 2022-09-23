import tkinter
from tkinter import *
import stack

#create all of the window properties
root = Tk()
root.title('BOSS GAME!')
root.geometry("640x480")
root.resizable(False, False)
frame = Frame(root)
frame.pack()

C = Canvas(frame, bg="blue", height=480, width=640)
filename = PhotoImage(file="main menu cs.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

stack = stack.Stack()

#decides where to place the images of abilities
#sends information to the main code about chosen abilities
class Choice:
    def choicePlace(self, filename, type, ability):
        self.img = PhotoImage(file=filename)
        self.imgLabel = Label(root, image=self.img, borderwidth=0, highlightthickness=0, bd=0)
        self.imgLabel.photo = self.img
        if len(stack.items) == 0 or len(stack.items) == 1 or len(stack.items) == 2:
            if len(stack.items) == 0:
                self.imgLabel.place(x=360, y= 391)
                self.abi_x = type
                self.abi_y = ability
                
            if len(stack.items) == 1:
                self.imgLabel.place(x=446, y=391)
                self.abi2_x = type
                self.abi2_y = ability
            
            if len(stack.items) == 2:
                self.imgLabel.place(x=537, y= 391)
                self.abi3_x = type
                self.abi3_y = ability
                
            stack.push("x")



    
    def backChoice(self):
        self.blank_img = PhotoImage(file='empty.png')
        self.blank_label = Label(root, image=self.blank_img, borderwidth=0, highlightthickness=0, bd=0)
        self.blank_label.photo = self.blank_img
        self.blank_label.place(x=349, y=353)
        while len(stack.items) > 0:
            stack.pop()

    def confirmedChoice(self):
        if len(stack.items) > 2:
            self.abilities = {
                'first': [self.abi_x, self.abi_y],
                'second': [self.abi2_x, self.abi2_y],
                'third': [self.abi3_x, self.abi3_y]}
            self.abils = self.abilities
            print(self.abils)
            try:
                root.destroy()
            except:
                pass
            return self.abils
        
choice = Choice()


# creates all of the buttons:
O1 = PhotoImage(file='fire.png')
buttonO1 = Button(image=O1, borderwidth=0, highlightthickness=0, bd=0)
buttonO1.place(x=30, y=135)
buttonO1['command'] = lambda filename='fire.png', type=1, ability=1: choice.choicePlace(filename, type, ability)

if len(stack.items) > 2:
    print('reached limit of abilities')

O2 = PhotoImage(file='lightning.png')
buttonO2 = Button(image=O2, borderwidth=0, highlightthickness=0, bd=0)
buttonO2.place(x=130, y=135)
buttonO2['command'] = lambda filename='lightning.png', type=1, ability=2: choice.choicePlace(filename, type, ability)

O3 = PhotoImage(file='charged.png')
buttonO3 = Button(image=O3, borderwidth=0, highlightthickness=0, bd=0)
buttonO3.place(x=230, y=135)
buttonO3['command'] = lambda filename='charged.png', type=1, ability=3: choice.choicePlace(filename, type, ability)

O4 = PhotoImage(file='earth.png')
buttonO4 = Button(image=O4, borderwidth=0, highlightthickness=0, bd=0)
buttonO4.place(x=328, y=135)
buttonO4['command'] = lambda filename='earth.png', type=1, ability=4: choice.choicePlace(filename, type, ability)

O5 = PhotoImage(file='earthquake.png')
buttonO5 = Button(image=O5, borderwidth=0, highlightthickness=0, bd=0)
buttonO5.place(x=424, y=135)
buttonO5['command'] = lambda filename='earthquake.png', type=1, ability=5: choice.choicePlace(filename, type, ability)


O6 = PhotoImage(file='barrage.png')
buttonO6 = Button(image=O6, borderwidth=0, highlightthickness=0, bd=0)
buttonO6.place(x=521, y=135)
buttonO6['command'] = lambda filename='barrage.png', type=1, ability=6: choice.choicePlace(filename, type, ability)

D1 = PhotoImage(file='confuse.png')
buttonD1 = Button(image=D1, borderwidth=0, highlightthickness=0, bd=0)
buttonD1.place(x=28, y=265)
buttonD1['command'] = lambda filename='confuse.png', type=2, ability=1: choice.choicePlace(filename, type, ability)

D2 = PhotoImage(file='shield.png')
buttonD2 = Button(image=D2, borderwidth=0, highlightthickness=0, bd=0)
buttonD2.place(x=130, y=266)
buttonD2['command'] = lambda filename='shield.png', type=2, ability=2: choice.choicePlace(filename, type, ability)


D3 = PhotoImage(file='wind.png')
buttonD3 = Button(image=D3, borderwidth=0, highlightthickness=0, bd=0)
buttonD3.place(x=230, y=267)
buttonD3['command'] = lambda filename='wind.png', type=2, ability=3: choice.choicePlace(filename, type, ability)


S1 = PhotoImage(file='heal.png')
buttonS1 = Button(image=S1, borderwidth=0, highlightthickness=0, bd=0)
buttonS1.place(x=24, y=396)
buttonS1['command'] = lambda filename='heal.png', type=3, ability=1: choice.choicePlace(filename, type, ability)


S2 = PhotoImage(file='ice.png')
buttonS2 = Button(image=S2, borderwidth=0, highlightthickness=0, bd=0)
buttonS2.place(x=126, y=396)
buttonS2['command'] = lambda filename='ice.png', type=3, ability=2: choice.choicePlace(filename, type, ability)


S3 = PhotoImage(file='drain.png')
buttonS3 = Button(image=S3, borderwidth=0, highlightthickness=0, bd=0)
buttonS3.place(x=230, y=397)
buttonS3['command'] = lambda filename='drain.png', type=3, ability=3: choice.choicePlace(filename, type, ability)


back = PhotoImage(file='back.png')
buttonB = Button(image=back, borderwidth=0, highlightthickness=0, bd=0, command=choice.backChoice)
buttonB.place(x=376, y=297)


confirm = PhotoImage(file='confirm.png')
buttonC = Button(image=confirm, borderwidth=0, highlightthickness=0, bd=0, command=choice.confirmedChoice)
buttonC.place(x=534, y=300)


root.mainloop()