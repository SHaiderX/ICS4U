import random
from random import randint


class Abilities:
    def __init__(self, username):
        self.enemy=100
        self.hero=100
        self.name=username

    def Earth(self):
        damage=random.randint(18,25)
        self.enemy=self.enemy-damage
        print (self.name, 'did', damage, 'damage using earth!')
        return self.enemy

    def EarthQuake(self):
        damage=random.randint(23,35)
        userdamage=random.randint(5,12)
        self.enemy=self.enemy-damage
        self.hero=self.hero-userdamage

        print(self.name, 'did', damage, 'damage to the enemy, but took', userdamage, 'in return!')
        return [self.enemy, self.hero]
                
    def Barrage(self):
        x=random.randint(1,5)
        TotalDmg=0
        for y in range (x):
            damage=random.randint(3,7)
            print(self.name, 'did', damage, 'damage for barrage #', x)
            TotalDmg=TotalDmg+damage
            
        print ('A total of', TotalDmg, 'damage!')
        self.enemy=self.enemy-TotalDmg
        return self.enemy

    def Heal(self):
        heal=random.randint(6,20)
        self.hero=self.hero+heal
        print (self.name, 'healed', heal, 'health!')
        return self.hero

    def LifeDrain(self):
        drain = random.randint(3,15)
        self.hero=self.hero+drain
        self.enemy=self.enemy-drain
        print(username, 'drained', drain, 'health from the enemy!')
        return [self.enemy,self.hero]

#   def Fire(self):


EnemyHealth = 100
HeroHealth = 100
        


Enemy = Abilities('Enemy')

def Enemy_Choice():
    a=(randint(0, 6))
    d=(randint(0, 3))
    s=(randint(0, 3))
    Amoves = ChooseAbility('a', a)
    Dmoves = ChooseAbility('d', d)
    Smoves = ChooseAbility('s', s)
    return [Amoves,Dmoves,Smoves]
    
E = Enemy_Choice()
E_Attack = E[0]
E_Defense = E[1]
E_Support = E[2]



def EnemyMove():
     if EnemyHealth <= 25:
         choices = [E_Attack,E_Defense,E_Support,E_Support,E_Support,E_Support,E_Support,E_Support]
         choice = random.choice(choices)
     if EnemyHealth <=50 and EnemyHealth > 25:
         choices = [E_Attack,E_Defense,E_Defense,E_Defense,E_Defense,E_Support,]
         choice = random.choice(choices)
     if EnemyHealth <= 100 and EnemyHealth >= 90:
         choices = [E_Attack,E_Defense]
         choice = random.choice(choices)
     if EnemyHealth <90 and EnemyHealth >50:
         choices = [E_Attack,E_Attack,E_Attack,E_Attack,E_Defense,E_Support]
         choice = random.choice(choices)
    return choice
    
def ChooseAbility(x, y):
    ability=''
    Hero=Abilities('MainHero')
    if x == 'a':
        if y == 1:
            ability = Hero.Fire
        if y == 2:
            ability = Hero.Earth
        if y == 3:
            ability = Hero.Lightning
        if y == 4:
            ability = Hero.EarthQuake
        if y == 5:
            ability = Hero.ChargedAttack
        if y == 6:
            ability = Hero.Barrage
    if x=='d':
        if y == 1:
            ability = Hero.Confusion
        if y == 2:
            ability = Hero.Dodge
        if y == 3:
            ability = Hero.Shield
    if x=='s':
        if y == 1:
            ability = Hero.Healing
        if y == 2:
            ability = Hero.Freeze
        if y == 3:
            ability = Hero.LifeDrain

    return ability


print ('Attack \n 1.Fire\n 2.Earth\n 3.Lighting\n 4.Earthquake\n 5.Charged Attack\n 6.Barrage\nDefence\n 1.Confusion\n 2.Dodge\n 3.Shield\nSupport\n 1.Healing\n 2.Freeze\n 3.Life Drain')

def pick():
    x=input('Press \'a\' \'d\' or \'s\' to pick between \'attack\' \'defence\' or \'support\'')
    y=input('Choose the number of the ability you want')

    return ChooseAbility(x,y)

one=pick()
two=pick()
three=pick()





def Battle():
    while EnemyHealth > 0 and HeroHealth >0:
        H_choice = input('Which Move Do You Want To Use', ' 1)', one , ' 2)', two, ' 3)',three)
        if H_choice == 1:
            EnemyHealth - one
        elif H_choice == 2:
            EnemyHealth - two
        elif H_choice == 3:
            EnemyHealth - three
        Enemy_Choice()
        EnemyMove()
        
