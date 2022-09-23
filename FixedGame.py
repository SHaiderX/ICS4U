import random
from random import randint

class Abilities: #class of abilities 
    def __init__(self, username): #initialize 
        self.name=username

    def Earth(self): #function for attack move earth
        damage=random.randint(18,25) #generate damage value
        print (self.name, 'did', damage, 'damage using earth!')
        return damage

    def EarthQuake(self): #function for attack move earthquake
        damage=random.randint(23,35) #generate damage value dealt to enemy
        userdamage=random.randint(5,12) #generate damage value dealt to self
        print(self.name, 'did', damage, 'damage to the enemy, but took', userdamage, 'in return!')
        return damage

    
                
    def Barrage(self): #function for attack move barrage
        x=random.randint(1,5) #generate number of attacks
        TotalDmg=0
        for y in range (x):
            damage=random.randint(3,7) #generate damage value of each attack
            print(self.name, 'did', damage, 'damage for barrage #', x)
            TotalDmg=TotalDmg+damage #sum of all turn's damage value to get total damage dealt 
        print ('A total of', TotalDmg, 'damage!')
        return TotalDmg

    def Healing(self): #function for support move healing
        heal=random.randint(12,21) #generate healing value
        print(self.name, 'healed', heal, 'health!')
        return heal

    def LifeDrain(self): #function for support move life drain
        drain = random.randint(3,15) #generate drain value
        print(self.name, 'drained', drain, 'health from the enemy!')
        return drain

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
    ability = ''
    Villian =Abilities('Boss')
    if x == 'a': #attack abilities selected
        if y == 1: 
            ability = Villian.Earth
        if y == 2: 
            ability = Villian.Earth
        if y == 3:
            ability = Villian.Earth
        if y == 4:
            ability = Villian.EarthQuake
        if y == 5:
            ability = Villian.Earth
        if y == 6:
            ability = Villian.Barrage
    if x=='d': #defence abilities selected
        if y == 1:
            ability = Villian.Earth
        if y == 2:
            ability = Villian.Earth
        if y == 3:
            ability = Villian.Earth
    if x=='s': #support abilities selected
        if y == 1:
            ability = Villian.Healing
        if y == 2:
            ability = Villian.Earth
        if y == 3:
            ability = Villian.LifeDrain
    return ability



print ('Attack \n 1.Fire\n 2.Earth\n 3.Lighting\n 4.Earthquake\n 5.Charged Attack\n 6.Barrage\nDefence\n 1.Confusion\n 2.Dodge\n 3.Shield\nSupport\n 1.Healing\n 2.Freeze\n 3.Life Drain') #display abilities list

one = HeroChooseAbility('a',2) 
two = HeroChooseAbility('d',2)
three = HeroChooseAbility('s',1)


def Enemy_Choice(): 
    a=(randint(1, 6)) #generate attack ability number
    d=(randint(1, 3)) #generate defence ability number
    s=(randint(1, 3)) #generate support ability number
    Amoves = EnemyChooseAbility('a', a) #attack move selection
    Dmoves = EnemyChooseAbility('d', d) #defence move selection
    Smoves = EnemyChooseAbility('s', s) #support move selection
    return [Amoves,Dmoves,Smoves]

EnemyHealth = 100 #enemy starting health
HeroHealth = 100 #hero starting health
E = Enemy_Choice()
E_Attack = E[0]
E_Defense = E[1]
E_Support = E[2]


def EnemyMove(): #enemy move 
     if EnemyHealth <= 25: #if enemy has low health, high chance of support/defence ability selection
         choices = [E_Attack, E_Defense, E_Support,E_Support,E_Support,E_Support,E_Support,E_Support]
         pos = random.randint(-1,7)
         choice = choices[pos]
     if EnemyHealth <=50 and EnemyHealth > 25: #if enemy has medium to low health, high chance of defence ability selection
         choices = [E_Attack,E_Defense,E_Defense,E_Defense,E_Defense,E_Support]
         pos = random.randint(-1,5)
         choice = choices[pos]
     if EnemyHealth <= 100 and EnemyHealth >= 90: #if enemy health is high, enemy will attack or defend, but wont use support ability
         choices = [E_Attack,E_Defense]
         pos = random.randint(-1,1)
         choice = choices[pos]
     if EnemyHealth <90 and EnemyHealth >50: #if enemy health is medium to high, enemy has high chance of using offensive ability
         choices = [E_Attack,E_Attack,E_Attack,E_Attack,E_Defense,E_Support]
         pos = random.randint(-1,5)
         choice = choices[pos]
     return choice

def Battle(EnemyHealth, HeroHealth): #battle function to run the game with turns

    while EnemyHealth > 0 and HeroHealth >0: #Game is played while both players have more than 0 health
        H_choice = int(input('Which Move Do You Want To Use'+ ' 1) 2) 3)')) #ask user for desired ability 
        if H_choice == 1: #if user chooses their first ability, use the first selected ability
            x = one()
            EnemyHealth = EnemyHealth - x #reduce enemy health by ability damage value
        elif H_choice == 2: #if user chooses their second ability, use the second selected ability
            z = two()
            EnemyHealth = EnemyHealth - z #reduce enemy health by ability damage value
        elif H_choice == 3: #if user chooses their third ability, use the third selected ability
            f = three()
            if HeroHealth + f <= 100: #Make sure health does not go over 100 due to healing
                HeroHealth = HeroHealth + f #Increase hero health by heal value
            else:
                HeroHealth = 100
        Enemy_Choice() #enemy turn, call on enemy move function
        y = EnemyMove()
        print(y)
        if y == ([E_Support]): 
            if EnemyHealth + y() <= 100: #make sure health does not go over 100 due to healing 
                EnemyHealth = EnemyHealth + y()  #heal boss by healing value
            else:
                EnemyHealth = 100
        else:
            HeroHealth = HeroHealth - y() #reduce hero health by enemy move damage value
        
        print(HeroHealth,'hero') #display hero health
        print(EnemyHealth,'enemy') #display enemy health
    print('GAME OVER!!!!!!!!!!!!!!!!')
Battle(EnemyHealth,HeroHealth) #run the game

