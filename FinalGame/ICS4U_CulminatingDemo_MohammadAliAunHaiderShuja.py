import random
from random import randint

class Abilities: #class of abilities 
    def __init__(self, username): #initialize 
        self.name=username

    def Earth(self): #function for attack move earth
        damage=random.randint(18,25) #generate damage value
        print (self.name, 'did', damage, 'damage using earth!')
        return [damage,0,0]

    def EarthQuake(self): #function for attack move earthquake
        damage=random.randint(23,35) #generate damage value dealt to enemy
        userdamage=random.randint(-12,-5) #generate damage value dealt to self
        print(self.name, 'did', damage, 'damage to the enemy, but took', userdamage, 'in return!')
        return [damage, userdamage,0]
                
    def Barrage(self): #function for attack move barrage
        x=random.randint(1,5) #generate number of attacks
        TotalDmg=0
        for y in range (x):
            damage=random.randint(3,7) #generate damage value of each attack
            print(self.name, 'did', damage, 'damage for barrage #', x)
            TotalDmg=TotalDmg+damage #sum of all turn's damage value to get total damage dealt 
        print ('A total of', TotalDmg, 'damage!')
        return [TotalDmg,0,0]

    def Lightning(self):
        Effect = 'shock'
        damage=random.randint(10,20)
        return [damage,0,Effect]

    def ChargedAttack(self):
        dmg = [0,0,0,0,50]
        dmg1 = random.choice(dmg)
        return [dmg1, 0, 0]

    def Fire(self):
        E = 'burn'
        dmg = random.randint(10,15)
        return [dmg,0,E]

    def Confusion(self):
        E = 'Confusion'
        return [0,0,E]

    def Dodge(self):
        E = 'dodge'
        print('The attack was dodged')
        return [0,0,E]

    def Shield(self):
        E = 'block'
        return [0,0,E]
         
    def Freeze(self):
        E = 'freeze'
        dmg = random.randint(5,15)
        return [dmg, 0, E]
        

    def Healing(self): #function for support move healing
        heal=random.randint(6,35) #generate healing value
        print (self.name, 'healed', heal, 'health!')
        return [0,heal,0]

    def LifeDrain(self): #function for support move life drain
        drain = random.randint(3,15) #generate drain value
        print(self.name, 'drained', drain, 'health from the enemy!')
        return [drain, drain,0]


Enemy = Abilities('Enemy')

    
def HeroChooseAbility(x, y): #function to choose hero abilities
    ability = ''
    Hero=Abilities('MainHero')
    names = [] #list of selected abilities
    if x == 'a': #if attack move is selected
        if y == 1: #select fire attack as ability
            ability = Hero.Fire
            
        elif y == 2: #select earth attack as ability
            ability = Hero.Earth
           
        elif y == 3: #select lightning attack as ability
            ability = Hero.Lightning
            
        elif y == 4: #select earthquake attack as ability
            ability = Hero.EarthQuake
            
        elif y == 5: #select charged attack as ability
            ability = Hero.ChargedAttack
            
        elif y == 6: #select barrage attack as ability
            ability = Hero.Barrage
            
    elif x=='d': #if defence move is selected
        if y == 1: #select confusion defence as ability
            ability = Hero.Confusion
            
        elif y == 2: #select dodge defence as ability
            ability = Hero.Dodge
            
        elif y == 3: #select shield defence as ability
            ability = Hero.Shield
            
    elif x=='s': #if support move is selected
        if y == 1: #select healing support ability
            ability = Hero.Healing
            
        elif y == 2: #select freeze support ability
            ability = Hero.Freeze
            
        elif y == 3: #select life drain support ability
            ability = Hero.LifeDrain
            
    
    return ability


def EnemyChooseAbility(x, y): #enemy boss chooses abilities
    names = []
    ability = ''
    Villain =Abilities('Boss')
    if x == 'a': #if attack move is selected
        
        if y == 1: #select fire attack as ability
            ability = Villain.Fire
            
        elif y == 2: #select earth attack as ability
            ability = Villain.Earth
            
        elif y == 3: #select lightning attack as ability
            ability = Villain.Lightning
            
        elif y == 4: #select earthquake attack as ability
            ability = Villain.EarthQuake
            
        elif y == 5: #select charged attack as ability
            ability = Villain.ChargedAttack
            
        elif y == 6: #select barrage attack as ability
            ability = Villain.Barrage
            
    elif x=='d': #if defence move is selected
        
        if y == 1: #select confusion defence as ability
            ability = Villain.Confusion

        elif y == 2: #select dodge defence as ability
            ability = Villain.Earth
            
        elif y == 3: #select shield defence as ability
            ability = Villain.Shield
            
    elif x=='s': #if support move is selected
        if y == 1: #select healing support ability
            ability = Villain.Healing
           
        elif y == 2: #select freeze support ability
            ability = Villain.Freeze
          
        elif y == 3: #select life drain support ability
            ability = Villain.LifeDrain
     
    
    return ability



print('Please choose your three abilities from the window')
import tkinter
from tkinter import *
import stack

# create all of the window properties
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


# decides where to place the images of abilities
# sends information to the main code about chosen abilities
class Choice:
    def choicePlace(self, filename, type, ability):
        self.img = PhotoImage(file=filename)
        self.imgLabel = Label(root, image=self.img, borderwidth=0, highlightthickness=0, bd=0)
        self.imgLabel.photo = self.img
        if len(stack.items) == 0 or len(stack.items) == 1 or len(stack.items) == 2:
            if len(stack.items) == 0:
                self.imgLabel.place(x=360, y=391)
                self.abi_x = type
                self.abi_y = ability
            
            if len(stack.items) == 1:
                self.imgLabel.place(x=446, y=391)
                self.abi2_x = type
                self.abi2_y = ability
            
            if len(stack.items) == 2:
                self.imgLabel.place(x=537, y=391)
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
buttonO1['command'] = lambda filename='fire.png', type='a', ability=1: choice.choicePlace(filename, type, ability)

if len(stack.items) > 2:
    print('reached limit of abilities')

O2 = PhotoImage(file='lightning.png')
buttonO2 = Button(image=O2, borderwidth=0, highlightthickness=0, bd=0)
buttonO2.place(x=130, y=135)
buttonO2['command'] = lambda filename='lightning.png', type='a', ability=2: choice.choicePlace(filename, type, ability)

O3 = PhotoImage(file='charged.png')
buttonO3 = Button(image=O3, borderwidth=0, highlightthickness=0, bd=0)
buttonO3.place(x=230, y=135)
buttonO3['command'] = lambda filename='charged.png', type='a', ability=3: choice.choicePlace(filename, type, ability)

O4 = PhotoImage(file='earth.png')
buttonO4 = Button(image=O4, borderwidth=0, highlightthickness=0, bd=0)
buttonO4.place(x=328, y=135)
buttonO4['command'] = lambda filename='earth.png', type='a', ability=4: choice.choicePlace(filename, type, ability)

O5 = PhotoImage(file='earthquake.png')
buttonO5 = Button(image=O5, borderwidth=0, highlightthickness=0, bd=0)
buttonO5.place(x=424, y=135)
buttonO5['command'] = lambda filename='earthquake.png', type='a', ability=5: choice.choicePlace(filename, type, ability)

O6 = PhotoImage(file='barrage.png')
buttonO6 = Button(image=O6, borderwidth=0, highlightthickness=0, bd=0)
buttonO6.place(x=521, y=135)
buttonO6['command'] = lambda filename='barrage.png', type='a', ability=6: choice.choicePlace(filename, type, ability)

D1 = PhotoImage(file='confuse.png')
buttonD1 = Button(image=D1, borderwidth=0, highlightthickness=0, bd=0)
buttonD1.place(x=28, y=265)
buttonD1['command'] = lambda filename='confuse.png', type='d', ability=1: choice.choicePlace(filename, type, ability)

D2 = PhotoImage(file='shield.png')
buttonD2 = Button(image=D2, borderwidth=0, highlightthickness=0, bd=0)
buttonD2.place(x=130, y=266)
buttonD2['command'] = lambda filename='shield.png', type='d', ability=2: choice.choicePlace(filename, type, ability)

D3 = PhotoImage(file='wind.png')
buttonD3 = Button(image=D3, borderwidth=0, highlightthickness=0, bd=0)
buttonD3.place(x=230, y=267)
buttonD3['command'] = lambda filename='wind.png', type='d', ability=3: choice.choicePlace(filename, type, ability)

S1 = PhotoImage(file='heal.png')
buttonS1 = Button(image=S1, borderwidth=0, highlightthickness=0, bd=0)
buttonS1.place(x=24, y=396)
buttonS1['command'] = lambda filename='heal.png', type='s', ability=1: choice.choicePlace(filename, type, ability)

S2 = PhotoImage(file='ice.png')
buttonS2 = Button(image=S2, borderwidth=0, highlightthickness=0, bd=0)
buttonS2.place(x=126, y=396)
buttonS2['command'] = lambda filename='ice.png', type='s', ability=2: choice.choicePlace(filename, type, ability)

S3 = PhotoImage(file='drain.png')
buttonS3 = Button(image=S3, borderwidth=0, highlightthickness=0, bd=0)
buttonS3.place(x=230, y=397)
buttonS3['command'] = lambda filename='drain.png', type='s', ability=3: choice.choicePlace(filename, type, ability)

back = PhotoImage(file='back.png')
buttonB = Button(image=back, borderwidth=0, highlightthickness=0, bd=0, command=choice.backChoice)
buttonB.place(x=376, y=297)

confirm = PhotoImage(file='confirm.png')
buttonC = Button(image=confirm, borderwidth=0, highlightthickness=0, bd=0, command=choice.confirmedChoice)
buttonC.place(x=534, y=300)

root.mainloop()

print ('Attack \n 1.Fire\n 2.Earth\n 3.Lighting\n 4.Earthquake\n 5.Charged Attack\n 6.Barrage\nDefence\n 1.Confusion\n 2.Dodge\n 3.Shield\nSupport\n 1.Healing\n 2.Freeze\n 3.Life Drain') #display abilities list

chosen = choice.confirmedChoice()
x=str(chosen['first'][0])
y=int(chosen['first'][1])
one = HeroChooseAbility(x, y)
print(type(one))
print(one)
x1=str(chosen['second'][0])
y1=int(chosen['second'][1])
two = HeroChooseAbility(x1, y1)
x2=str(chosen['third'][0])
y2=int(chosen['third'][1])
three = HeroChooseAbility(x2, y2)


a=(randint(1, 6)) #generate attack ability number
d=(randint(1, 3)) #generate defence ability number
s=(randint(1, 3)) #generate support ability number
E_Attack = EnemyChooseAbility('a', 2) #attack move selection
E_Defense = EnemyChooseAbility('d', 2) #defence move selection
E_Support = EnemyChooseAbility('s', 2) #support move selection

EnemyHealth = 100 #enemy starting health
HeroHealth = 100 #hero starting health


def EnemyMove(): #enemy move 
    if EnemyHealth <= 25: #if enemy has low health, high chance of support/defence ability selection
        choices = [E_Attack,E_Defense,E_Support,E_Support,E_Support,E_Support,E_Support,E_Support]
        choice = random.choice(choices)
        print (choice)
    if EnemyHealth <=50 and EnemyHealth > 25: #if enemy has medium to low health, high chance of defence ability selection
        choices = [E_Attack,E_Defense,E_Defense,E_Defense,E_Defense,E_Support,]
        choice = random.choice(choices)
        print (choice)
    if EnemyHealth <= 100 and EnemyHealth >= 90: #if enemy health is high, enemy will attack or defend, but wont use support ability
        choices = [E_Attack,E_Defense]
        choice = random.choice(choices)
        print (choice)
    if EnemyHealth <90 and EnemyHealth >50: #if enemy health is medium to high, enemy has high chance of using offensive ability
        choices = [E_Attack,E_Attack,E_Attack,E_Attack,E_Defense,E_Support]
        choice = random.choice(choices)
        print (choice)
    return choice

def Effects(E):
    
    if E=="shock":
        x= 1
        if x==1:
            print ('Paralyzed, next turn will be skipped')
            return 'S'
        else:
            return ''
    elif E=='freeze':
        x = 1
        if x==1:
            return 'F'
        else:
            return ''        
    elif E=='burn':
        b=random.randint(0,4)
        print ('Burn has done', b, 'damage.')
        return b
    elif E=='Confusion':
        x=random.randint(1,3)
        if x==1:        
            print('Did damage to themselves in confusion')
        else:
            print('Confusion did not work')
    elif E == 0:
        return " "
    elif E == 'dodge':
        x = random.randint(1,2)
        if x == 1: 
            return 0
        else:
            return ""
    return ' '


def Battle(EnemyHealth,HeroHealth): #battle function to run the game with turns
    EFF = ''
    
    if (EnemyHealth>0):

            if EnemyHealth <= 25: #if enemy has low health, high chance of support/defence ability selection
                choices = [E_Attack,E_Defense,E_Support,E_Support,E_Support,E_Support,E_Support,E_Support]
                choice = random.choice(choices)
                
            if EnemyHealth <=50 and EnemyHealth > 25: #if enemy has medium to low health, high chance of defence ability selection
                choices = [E_Attack,E_Defense,E_Defense,E_Defense,E_Defense,E_Support,]
                choice = random.choice(choices)
    
            if EnemyHealth <= 100 and EnemyHealth >= 90: #if enemy health is high, enemy will attack or defend, but wont use support ability
                choices = [E_Attack,E_Defense]
                choice = random.choice(choices)
                
            if EnemyHealth <90 and EnemyHealth >50: #if enemy health is medium to high, enemy has high chance of using offensive ability
                choices = [E_Attack,E_Attack,E_Attack,E_Attack,E_Defense,E_Support]
                choice = random.choice(choices)
            Dout = choice()
    while EnemyHealth > 0 and HeroHealth >0:
        
        H_choice = int(input('Which Move Do You Want To Use'+ ' 1)' + '' + ' 2)' + '' + ' 3)' + ''))
        EFF
        if EFF == 'S' or EFF == 'F':
            H_choice = 0
            
            
        if H_choice == 1:  
            Hout=one()
            Effects(Hout[2])  
            damage=Hout[0]
            heal=Hout[1]
            if Dout[2] == 'dodge':
                damage = 0
                heal = 0
            if Effects(Dout[2]) == 'F' or Effects(Dout[2]) == 'S':
               print('Your Turn is skipped')
               damage = 0
               heal = 0
            EnemyHealth -= damage
            HeroHealth += heal
        elif H_choice == 2:
            Hout=two()
            Effects(Hout[2])  
            damage=Hout[0]
            heal=Hout[1]
            if Dout[2] == 'dodge':
                damage = 0
                heal = 0
            if Effects(Dout[2]) == 'F' or Effects(Dout[2]) == 'S':
                print('Your Turn is skipped')
                damage = 0
                heal = 0
            EnemyHealth -= damage
            HeroHealth += heal
        elif H_choice == 3:
            Hout=three()
            Effects(Hout[2])  
            damage=Hout[0]
            heal=Hout[1]
            if Dout[2] == 'dodge':
                damage = 0
                heal = 0
            if Effects(Dout[2]) == 'F' or Effects(Dout[2]) == 'S':
                print('Your Turn is skipped')
                damage = 0
                heal = 0
            EnemyHealth -= damage
            HeroHealth += heal
        elif H_choice == 0:
            print('Turn is Skipped')


        if (EnemyHealth>0):

            if EnemyHealth <= 25: #if enemy has low health, high chance of support/defence ability selection
                choices = [E_Attack,E_Defense,E_Support,E_Support,E_Support,E_Support,E_Support,E_Support]
                choice = random.choice(choices)
                
            if EnemyHealth <=50 and EnemyHealth > 25: #if enemy has medium to low health, high chance of defence ability selection
                choices = [E_Attack,E_Defense,E_Defense,E_Defense,E_Defense,E_Support,]
                choice = random.choice(choices)
    
            if EnemyHealth <= 100 and EnemyHealth >= 90: #if enemy health is high, enemy will attack or defend, but wont use support ability
                choices = [E_Attack,E_Defense]
                choice = random.choice(choices)
                
            if EnemyHealth <90 and EnemyHealth >50: #if enemy health is medium to high, enemy has high chance of using offensive ability
                choices = [E_Attack,E_Attack,E_Attack,E_Attack,E_Defense,E_Support]
                choice = random.choice(choices)            

            Dout = choice()
            EFF = Effects(Dout[2])
            dmg=Dout[0]
            heal=Dout[1]
            if Hout[2] == 'dodge':
                dmg = 0
                heal = 0
            if Effects(Hout[2]) == 'F' or Effects(Hout[2]) == 'S':
                print('Enemy Turn is skipped')
                damage = 0
                heal = 0
            HeroHealth -= dmg
            EnemyHealth += heal
            
        print(HeroHealth,'hero') #display hero health
        print(EnemyHealth,'enemy') #display enemy health
        
    print('GAME OVER!!!!')
  
Battle(EnemyHealth,HeroHealth) #run the game
