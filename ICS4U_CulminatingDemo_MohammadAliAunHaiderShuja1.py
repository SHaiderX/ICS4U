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
    

#   def Fire(self):


Enemy = Abilities('Enemy')

    
def HeroChooseAbility(x, y): #function to choose hero abilities
    ability = ''
    Hero=Abilities('MainHero')
    names = [] #list of selected abilities
    if x == 'a': #if attack move is selected
        if y == 1: #select fire attack as ability
            ability = Hero.Fire
            Aname = 'Fire'
        elif y == 2: #select earth attack as ability
            ability = Hero.Earth
            Aname = 'Earth'
        elif y == 3: #select lightning attack as ability
            ability = Hero.Lightning
            Aname = 'Lightning'
        elif y == 4: #select earthquake attack as ability
            ability = Hero.EarthQuake
            Aname = 'EarthQuake'
        elif y == 5: #select charged attack as ability
            ability = Hero.ChargedAttack
            Aname = 'ChargedAttack'
        elif y == 6: #select barrage attack as ability
            ability = Hero.Barrage
            Aname = 'Barrage'
        names.append(Aname) #append abilities list to add the selected abilities to the list
    elif x=='d': #if defence move is selected
        if y == 1: #select confusion defence as ability
            ability = Hero.Confusion
            Dname = 'Confusion'
        elif y == 2: #select dodge defence as ability
            ability = Hero.Earth
            Dname = 'Dodge'
        elif y == 3: #select shield defence as ability
            ability = Hero.Shield
            Dname = 'Sheild'
        names.append(Dname) #append abilities list to add the selected abilities
    elif x=='s': #if support move is selected
        if y == 1: #select healing support ability
            ability = Hero.Healing
            Sname = 'Healing'
        elif y == 2: #select freeze support ability
            ability = Hero.Freeze
            Sname = 'Freeze'
        elif y == 3: #select life drain support ability
            ability = Hero.LifeDrain
            Sname = 'LifeDrain'
        names.append(Sname) #append abilities list to add selected abilities
    
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



print ('Attack \n 1.Fire\n 2.Earth\n 3.Lighting\n 4.Earthquake\n 5.Charged Attack\n 6.Barrage\nDefence\n 1.Confusion\n 2.Dodge\n 3.Shield\nSupport\n 1.Healing\n 2.Freeze\n 3.Life Drain') #display abilities list

one = HeroChooseAbility('a',2) 
two = HeroChooseAbility('d',2)
three = HeroChooseAbility('s',1)


a=(randint(1, 6)) #generate attack ability number
d=(randint(1, 3)) #generate defence ability number
s=(randint(1, 3)) #generate support ability number
E_Attack = EnemyChooseAbility('a', a) #attack move selection
E_Defense = EnemyChooseAbility('d', d) #defence move selection
E_Support = EnemyChooseAbility('s', s) #support move selection

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
    effect=0
    if E=="shock":
        x=random.randint(1,5)
        if x==1:
            print ('Paralyzed, next turn will be skipped')
            return 'S'
        else:
            return ''
    elif E=='Freeze':
        x=random.randint(1,3)
        if x==1:
            print ('Frozen, next turn will be skipped')
            return 'S'
        else:
            return ''        
    elif E=='burn':
        b=random.randint(0,4)
        print ('Burn has done', b, 'damage.')
        return b
    elif E=='Confusion':
        x=random.randint(1,3)
        if x==1:        
            print('Did', dmg, 'damage to themselves in confusion')
        else:
            print('Confusion did not work')
    elif E == 0:
        return " "
    elif E == 'dodge':
        x = random.randint(1,2)
        if x == 1: 
            return dmg

def Battle(EnemyHealth,HeroHealth): #battle function to run the game with turns
    while EnemyHealth > 0 and HeroHealth >0:
        
        H_choice = int(input('Which Move Do You Want To Use'+ ' 1)' + '' + ' 2)' + '' + ' 3)' + ''))

        if H_choice == 1:  
            out=one()
            Effects(out[2])  
            damage=out[0]
            heal=out[1]
            if out[2] == 'dodge':
                damage = 0
                heal = 0
            EnemyHealth -= damage
            HeroHealth += heal
        elif H_choice == 2:
            out=two()
            Effects(out[2])  
            damage=out[0]
            heal=out[1]
            if out[2] == 'dodge':
                damage = 0
                heal = 0
            EnemyHealth -= damage
            HeroHealth += heal
        elif H_choice == 3:
            out=three()
            Effects(out[2])  
            damage=out[0]
            heal=out[1]
            if out[2] == 'dodge':
                damage = 0
                heal = 0
            EnemyHealth -= damage
            HeroHealth += heal
                
        if (EnemyHealth>0):

            if EnemyHealth <= 25: #if enemy has low health, high chance of support/defence ability selection
                choices = ['A', 'D', 'S', 'S', 'S', 'S', 'S', 'S']
                choice = random.choice(choices)

            if EnemyHealth <=50 and EnemyHealth > 25: #if enemy has medium to low health, high chance of defence ability selection
                choices = ['A', 'D', 'D', 'D', 'D', 'S']
                choice = random.choice(choices)
            if EnemyHealth <= 100 and EnemyHealth >= 90: #if enemy health is high, enemy will attack or defend, but wont use support ability
                choices = ['A', 'A', 'A', 'D']
                choice = random.choice(choices)
     
            if EnemyHealth <90 and EnemyHealth >50: #if enemy health is medium to high, enemy has high chance of using offensive ability
                choices = ['A', 'A', 'A', 'D', 'D', 'D', 'S']
                choice = random.choice(choices)
            
            if choice=='A':
                out=E_Attack()
            elif choice=='D':
                out=E_Defense()
            elif choice=='S':
                out=E_Support()                    
                
            print ('qwdqw', choice)   
            out=choice()
            dmg=out[0]
            heal=out[1]
            if out[2] == 'dodge':
                damage = 0
                heal = 0
            HeroHealth -= dmg
            EnemyHealth += heal
            
        print(HeroHealth,'hero') #display hero health
        print(EnemyHealth,'enemy') #display enemy health
    print('GAME OVER!!!!!!!!!!!!!!!!')      
        
Battle(EnemyHealth,HeroHealth) #run the game
