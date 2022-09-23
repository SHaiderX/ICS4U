import random
from random import randint

class Abilities:
    def __init__(self, username):
        self.name=username

    def Earth(self):
        damage=random.randint(18,25)
        print (self.name, 'did', damage, 'damage using earth!')
        return [damage,0]

    def EarthQuake(self):
        damage=random.randint(23,35)
        userdamage=random.randint(-5,-12)
        print(self.name, 'did', damage, 'damage to the enemy, but took', userdamage, 'in return!')
        return [damage, userdamage]
                
    def Barrage(self):
        x=random.randint(1,5)
        TotalDmg=0
        for y in range (x):
            damage=random.randint(3,7)
            print(self.name, 'did', damage, 'damage for barrage #', x)
            TotalDmg=TotalDmg+damage 
        print ('A total of', TotalDmg, 'damage!')
        return [TotalDmg,0]

    def Healing(self):
        heal=random.randint(6,20)
        print (self.name, 'healed', heal, 'health!')
        return [0,heal]

    def LifeDrain(self):
        drain = random.randint(3,15)
        print(self.name, 'drained', drain, 'health from the enemy!')
        return [drain, drain]

#   def Fire(self):


Enemy = Abilities('Enemy')

    
def HeroChooseAbility(x, y):
    ability = ''
    Hero=Abilities('MainHero')
    names = []
    if x == 'a':
        if y == 1:
            ability = Hero.Fire
            Aname = 'Fire'
        elif y == 2:
            ability = Hero.Earth
            Aname = 'Earth'
        elif y == 3:
            ability = Hero.Lightning
            Aname = 'Lightning'
        elif y == 4:
            ability = Hero.EarthQuake
            Aname = 'EarthQuake'
        elif y == 5:
            ability = Hero.ChargedAttack
            Aname = 'ChargedAttack'
        elif y == 6:
            ability = Hero.Barrage
            Aname = 'Barrage'
        names.append(Aname)
    elif x=='d':
        if y == 1:
            ability = Hero.Confusion
            Dname = 'Confusion'
        elif y == 2:
            ability = Hero.Earth
            Dname = 'Dodge'
        elif y == 3:
            ability = Hero.Shield
            Dname = 'Sheild'
        names.append(Dname)
    elif x=='s':
        if y == 1:
            ability = Hero.Healing
            Sname = 'Healing'
        elif y == 2:
            ability = Hero.Freeze
            Sname = 'Freeze'
        elif y == 3:
            ability = Hero.LifeDrain
            Sname = 'LifeDrain'
        names.append(Sname)
    
    return ability


def EnemyChooseAbility(x, y):
    ability = ''
    Villian =Abilities('Boss')
    if x == 'a':
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
    if x=='d':
        if y == 1:
            ability = Villian.Earth
        if y == 2:
            ability = Villian.Earth
        if y == 3:
            ability = Villian.Earth
    if x=='s':
        if y == 1:
            ability = Villian.Healing
        if y == 2:
            ability = Villian.Earth
        if y == 3:
            ability = Villian.LifeDrain
    return ability



print ('Attack \n 1.Fire\n 2.Earth\n 3.Lighting\n 4.Earthquake\n 5.Charged Attack\n 6.Barrage\nDefence\n 1.Confusion\n 2.Dodge\n 3.Shield\nSupport\n 1.Healing\n 2.Freeze\n 3.Life Drain')


one = HeroChooseAbility('a',2)
two = HeroChooseAbility('d',2)
three = HeroChooseAbility('s',1)
print ('')

def Enemy_Choice():
    a=(randint(0, 6))
    d=(randint(0, 3))
    s=(randint(0, 3))
    Amoves = EnemyChooseAbility('a', a)
    Dmoves = EnemyChooseAbility('d', d)
    Smoves = EnemyChooseAbility('s', s)
    return [Amoves,Dmoves,Smoves]

EnemyHealth = 100
HeroHealth = 100
E = Enemy_Choice()
E_Attack = E[0]
E_Defense = E[1]
E_Support = E[2]

print('attack',E_Attack())
print (one())

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

def Effects(E, dmg):
    effect=0
    if E=="shock":
        x=random.randint(1,5)
        if x==1:
            print ('Paralyzed, next turn will be skipped')
            return 'S'
        else:
            return ''
    if E=='burn':
        b=random.randint(0,4)
        print ('Burn has done', b, 'damage.')
        return b
    if E=='Confusion':
        x=random.randint(1,3)
        if x==1:        
            print('Did', dmg, 'damage to themselved in confusion')
            return dmg

    
def Battle(EnemyHealth, HeroHealth):
    while EnemyHealth > 0 and HeroHealth >0:
        HeroEffect=Effects(HeroHealth, Eff)
        if HeroEffect!='S':
            H_choice = input('Which Move Do You Want To Use'+ ' 1)' + '' + ' 2)' + '' + ' 3)' + '')
            if H_choice == 1:
                EnemyHealth -= one()[0]
                HeroHealth += one()[1]
            elif H_choice == 2:
                EnemyHealth -= two()[0]
                HeroHealth += two()[1] 
            elif H_choice == 3:
                EnemyHealth -= three()[0]
                HeroHealth += three()[1]   
        EnemyEffect=Effects(EnemyHealth, Eff)
        if (EnemyEffect!='S'):
            Enemy_Choice()
            EM=EnemyMove()
            HeroHealth -= EM()[0]
            EnemyHealth += EM()[1]
        
        print(HeroHealth,'hero') #display hero health
        print(EnemyHealth,'enemy') #display enemy health
        print('GAME OVER!!!!!!!!!!!!!!!!')        
        
Battle(EnemyHealth, HeroHealth)

