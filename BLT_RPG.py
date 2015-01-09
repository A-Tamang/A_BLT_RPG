# --------------------------------------------------------------------------------------------------
#
# Title: A BLT RPG
# Creator: Ashish Tamang
# Student of the University of Waterloo
# Created: Spring 2013
#
# Synopsis:
#          A text-based Dungeon Crawling RPG made in Python. It employs the use of
#          Object Oriented Programming to handle stats of the characters and monsters.
#          Careful attention has been paid to balancing the game to make the playing
#          experience as pleasurable as possible.
#
# Description:
#
#          In BLT_RPG, you are an adventure raiding a floating castle inhabited by 
#          the notorious bandit guild, 'Neko Hooligans'. In the character creation section, 
#          you must pick one of five classes: 
#          
#               i) Berserker ii) Hemomancer iii) Weaponmaster iv) Archmage v) Lone Wolf
#          
#          With a weapon in hand, your objective is cleave through the Hooligans, ascend
#          the three floors of the floating castle and confront the ever-elusive 
#          phantom leader of the guild.
#
#
# Instructions:
#
#          The game is very easy to play. It is text-based and therefore every interaction,
#          --whether it is traversing through the dungeon, fighting monsters 
#          or checking one's stats-- is done through the use of I/O with Python. 
#
#
# Possible Future Updates:
#
#          i) Cleaner Battles; easier to distinguish damage
#         ii) The integration of a map to make traversing a bit easier
#        iii) The introduction of a GUI
#
#----------------------------------------------------------------------------------------------------


import random
from time import time
#Format for the Monsters/Classes
class Characters():
    name = ""
    job = ""
    STR = ""
    MAGIC = ""
    AGI = ""
    HP = ""
    LIMIT = ""
    LS = ""
    Explain = {}
    Upgrades = []
    UpgradesREAL = []
    TierOne = {}
    TierOneLIST = []
    TierTwo = {}
    TierTwoLIST = []
    TierOneLevel = 0
    TierTwoLevel = 0
    CurrentHP = ""
    MoveSet = []
    ExecuteMove = {}
#Player Lifesteal
def Lifesteal(Damage, Classes, Hero):
    Classes[Hero].CurrentHP = Classes[Hero].CurrentHP + round((Damage*Classes[Hero].LS))
    if Classes[Hero].CurrentHP > Classes[Hero].HP:
        Classes[Hero].CurrentHP = Classes[Hero].HP
#Monster Lifesteal
def LifestealMonster(Damage, LS, BadGuy):
    BadGuy.HP = BadGuy.HP + round((Damage*LS))
    if BadGuy.HP > BadGuy.MaxHP:
        BadGuy.HP = BadGuy.MaxHP
#Player Critical Chance
def CriticalChance(Classes, Hero):
    if random.randrange(100)+1 <= Classes[Hero].AGI:
        Crit = 2.5
    else:
        Crit = 1
    return Crit
#Monster Critical Chance
def MonsterFatality(BadGuy):
    if random.randrange(100)+1 <= BadGuy.AGI:
        Crit = 2
    else:
        Crit = 1
    return Crit
#Player Special Move Check
def LimitBreak(Ultimate):
    if Ultimate == 100:
        Ultimate = 0
        return 1, Ultimate
    else:
        print ("\nYou cannot break your 'Limit' yet.\nYour current SP is", str(Ultimate)+"!\n")
        return 0, Ultimate
#Critical Hit Announcement
def CriticalHit(Crit):
    if Crit >= 2:
        print ("CRITICAL HIT!")
            
def BerAttack(Berserker, BadGuy):
    SaveAGI = Berserker.AGI
    if Berserker.CurrentHP/Berserker.HP <= 0.75:
        Berserker.AGI = Berserker.AGI + 5
    elif Berserker.CurrentHP/Berserker.HP <= 0.50:
        Berserker.AGI = Berserker.AGI + 10
    elif Berserker.CurrentHP/Berserker.HP <= 0.25:
        Berserker.AGI = Berserker.AGI + 15
    elif Berserker.CurrentHP/Berserker.HP <= 0.10:
        Berserker.AGI = Berserker.AGI + 20
    Crit = CriticalChance(Classes, Hero)
    Damage = Berserker.STR * (random.randrange(10, 20, 5)+1)/10 * Crit
    print (Classes[Hero].name, "used Vicious Strike!\n"+ BadGuy.name, "received", round(Damage), "damage!")
    CriticalHit(Crit)
    Berserker.AGI = SaveAGI
    return round(Damage)

def BerSkill(Berserker, BadGuy):
    Rage = 0
    Crit = CriticalChance(Classes, Hero)
    if Berserker.CurrentHP/Berserker.HP <= 0.10:
        Rage = 2.5
    elif Berserker.CurrentHP/Berserker.HP <= 0.25:
        Rage = 1.25
    elif Berserker.CurrentHP/Berserker.HP <= 0.50:
        Rage = 0.75
    elif Berserker.CurrentHP/Berserker.HP <= 0.75:
        Rage = 0.5
    Damage = Berserker.STR*(random.randrange(13, 18, 1)+1)/10*Crit + (Berserker.STR*(random.randrange(10, 30, 2)+1)/10*Crit)*Rage
    print (Classes[Hero].name, "used Limit Break: Raging Slash!\n"+ BadGuy.name, "received", round(Damage), "damage!")
    CriticalHit(Crit)
    return round(Damage)

Berserker = Characters()
Berserker.job = "Berserker"
Berserker.STR = 5
Berserker.MAGIC = 0
Berserker.AGI = 5
Berserker.HP = 410
Berserker.CurrentHP = 240
Berserker.LIMIT = 7
Berserker.MoveSet = ["Vicious Strike", "Raging Slash"]
Berserker.Explain = {"Vicious Strike":"A regular attack that delivers with increased agility the lower the user's health is.", "Raging Slash":"A Limit Break with damage that scales higher the lower the user's health."}
Berserker.ExecuteMove = [BerAttack,BerSkill]
Berserker.TierOneLevel, Berserker.TierTwoLevel = 0, 0
Berserker.TierOne = {"Longsword":15, "Warrior's Greatsword":20, "Berserker's Blade":25, "Titan's Tooth":35, "Sanjeeve's Special Sword":50}
Berserker.TierOneLIST = ["Longsword", "Warrior's Greatsword", "Berserker's Blade", "Titan's Tooth", "Sanjeeve's Special Sword"]
Berserker.TierTwo = {"Leather Armour":25, "Stone Armour":50, "Iron Armour":75, "Knight's Armour":100, "Berserker's Armour":200}
Berserker.TierTwoLIST = ["Leather Armour", "Stone Armour", "Iron Armour", "Knight's Armour", "Berserker's Armour"]
Berserker.Upgrades = ["Strength", "Health"]
Berserker.UpgradesREAL = [Berserker.STR, Berserker.HP]

def HemAttack(Hemomancer, BadGuy):
    Crit = CriticalChance(Classes, Hero)
    Damage = Hemomancer.MAGIC*(random.randrange(12,20,4)+1)/10*Crit
    Lifesteal(Damage, Classes, Hero)
    print (Classes[Hero].name, "used Blood Drain!\n"+ BadGuy.name, "received", round(Damage), "damage!", Classes[Hero].name, "healed", round(Hemomancer.LS*Damage), "HP!")
    CriticalHit(Crit)
    return round(Damage)

def HemSkill(Hemomancer, BadGuy):
    Damage = 0
    neko = 0
    sacrifice = Hemomancer.CurrentHP * 0.2
    Hemomancer.CurrentHP = Hemomancer.CurrentHP - sacrifice
    for i in range(random.randrange(3,6)+1):
        Crit = CriticalChance(Classes, Hero)
        neko = neko + 1
        Damage = Damage + (Hemomancer.MAGIC*(random.randrange(10,18,2)+1)/10 + sacrifice*(random.randrange(2,8)+1)/10)*Crit
        CriticalHit(Crit)
    print (Classes[Hero].name, "sacrified", round(sacrifice), "health to unleash Limit Break: Savagery!\n"+ str(neko), "hits were executed.\n"+ BadGuy.name, "received", round(Damage), "damage!")
    return round(Damage)

Hemomancer = Characters()
Hemomancer.job = "Hemomancer"
Hemomancer.STR = 0
Hemomancer.MAGIC = 12
Hemomancer.AGI = 5
Hemomancer.LS = 0.1
Hemomancer.HP = 395
Hemomancer.CurrentHP = 255
Hemomancer.LIMIT = 5
Hemomancer.MoveSet = ["Blood Drain", "Savagery"]
Hemomancer.Explain = {"Blood Drain":"A vampiric attack that heals the user for a portion of the damage dealt.", "Savagery":"A Limit Break that requires a small health sacrifice. Deals damage that scales upwards depending on the the cost."}
Hemomancer.ExecuteMove = [HemAttack,HemSkill]
Hemomancer.TierOneLevel, Hemomancer.TierTwoLevel = 0, 0
Hemomancer.TierOne = {"Emblem of Fire":0, "Emblem of Blood":6, "Emblem of Wrath":15, "Emblem of Gods":23, "Emblem of the Abyss":30}
Hemomancer.TierOneLIST = ["Emblem of Fire", "Emblem of Blood", "Emblem of Wrath", "Emblem of Gods", "Emblem of the Abyss"]
Hemomancer.TierTwo = {"Transfer Seal":0, "Enhanced Seal":0.05, "Frenzy Seal":0.1, "Seal of Savagery":0.175, "Vampirical Seal":0.25}
Hemomancer.TierTwoLIST = ["Transfer Seal", "Enhanced Seal", "Frenzy Seal", "Seal of Savagery", "Vampirical Seal"]
Hemomancer.Upgrades = ["Magic", "Lifesteal"]
Hemomancer.UpgradesREAL = [Hemomancer.MAGIC, Hemomancer.LS]

def WepAttack(Weaponmaster, BadGuy):
    Slice = random.randrange(10)+1
    Crit = CriticalChance(Classes, Hero)
    Damage = (Weaponmaster.STR*(random.randrange(6,15,3)+1)/10+Weaponmaster.AGI*(random.randrange(2,8)+1)/10)*Crit
    print (Classes[Hero].name, "used Slice and Dice!\n"+ BadGuy.name, "received", round(Damage), "damage!")
    #Bleed 5%
    CriticalHit(Crit)
    if Slice == 1 or Slice == 2:
        Crit = CriticalChance(Classes, Hero)
        DamageBonus = (Weaponmaster.STR*(random.randrange(3,9,3)+1)/10+Weaponmaster.AGI*(random.randrange(2,5)+1)/10)*Crit
        Damage = Damage + DamageBonus
        print ("An opening! The second slash of Slice and Dice does a bonus", str(round(DamageBonus))+"!")
        CriticalHit(Crit)
    return round(Damage)

def WepSkill(Weaponmaster, BadGuy):
    Damage = 0
    neko = 0
    for i in range(random.randrange(5,10,1)+1):
        Crit = CriticalChance(Classes, Hero)
        neko = neko + 1
        Damage = Damage + (Weaponmaster.STR*(random.randrange(2,5)+1)/10+Weaponmaster.AGI*(random.randrange(8,15)+1)/10)*Crit
        CriticalHit(Crit)
    print (Classes[Hero].name, "used Limit Break: Hurricane SPD!\n"+ str(neko), "hits were executed.\n"+ BadGuy.name, "received", round(Damage), "damage!")
    return round(Damage)
        
Weaponmaster = Characters()
Weaponmaster.job = "Weaponmaster"
Weaponmaster.STR = 17
Weaponmaster.MAGIC = 0
Weaponmaster.AGI = 15
Weaponmaster.HP = 360
Weaponmaster.CurrentHP = 210
Weaponmaster.LIMIT = 2
Weaponmaster.MoveSet = ["Slice and Dice", "Hurricane SPD"]
Weaponmaster.Explain = {"Slice and Dice":"A regular attack that has 20% chance of dealing bonus damage.", "Hurricane SPD":"A fast-hitting Limit Break that deals 5 to 10 successive strikes. Very dependant on Agility."}
Weaponmaster.ExecuteMove = [WepAttack,WepSkill]
Weaponmaster.TierOneLevel, Weaponmaster.TierTwoLevel = 0, 0
Weaponmaster.TierOne = {"Unnamed Weapon":0, "Twin Blades":5, "Stormy Skies":12, "Twin Shadows":17, "Empty Skies":21}
Weaponmaster.TierOneLIST = ["Unnamed Weapon", "Twin Blades", "Stormy Skies", "Twin Shadows", "Empty Skies"]
Weaponmaster.TierTwo = {"Hidden Blade":0, "Concealed Shiv":2, "Chain and Sickle":4, "Long Scythe":7, "Katana":10}
Weaponmaster.TierTwoLIST = ["Hidden Blade", "Concealed Shiv", "Chain and Sickle", "Long Scythe", "Katana"]
Weaponmaster.Upgrades = ["Strength", "Agility"]
Weaponmaster.UpgradesREAL = [Weaponmaster.STR, Weaponmaster.AGI]

def ArcAttack(Archmage, BadGuy):
    Crit = CriticalChance(Classes, Hero)
    Damage = Archmage.MAGIC*(random.randrange(7,12)+1)/10*Crit
    print (Classes[Hero].name, "used Magic Channel!\n"+ BadGuy.name, "received", round(Damage), "damage!")
    CriticalHit(Crit)
    if random.randrange(10) == (1 or 2 or 3):
        print ("Remnants of magic have been absorbed!\n\n"+ Classes[Hero].name, "has gained +1 MAGIC!")
        Classes[Hero].MAGIC = Classes[Hero].MAGIC + 1
    return round(Damage)
        
def ArcSkill(Archmage, BadGuy):
    Crit = CriticalChance(Classes, Hero)
    Damage = Archmage.MAGIC*(random.randrange(17,22)+1)/10*Crit
    CriticalHit(Crit)
    print (Classes[Hero].name, "unleased Limit Break: Lightning Storm!\n"+ BadGuy.name, "received", round(Damage), "damage!")
    return round(Damage)
        
Archmage = Characters()
Archmage.job = "Archmage"
Archmage.STR = 0
Archmage.MAGIC = 25
Archmage.AGI = 5
Archmage.HP = 315
Archmage.CurrentHP = 165
Archmage.LIMIT = 7
Archmage.Explain = {"Magic Channel":"A magic attack that has 30% chance of increasing the user's MAGIC stat by 1.", "Lightning Storm":"A powerful Limit Break that recharges quickly and inflicts high damage."}
Archmage.MoveSet = ["Magic Channel", "Lightning Storm"]
                     
Archmage.ExecuteMove = [ArcAttack,ArcSkill]
Archmage.TierOneLevel, Archmage.TierTwoLevel = 0, 0
Archmage.TierOne = {"Wooden Staff":5, "Gem-Embedded Staff":10, "Alchemist's Staff":15, "Staff of Arcane Might":20, "Deity's Scepter":25}
Archmage.TierOneLIST = ["Wooden Staff", "Gem-Embedded Staff", "Alchemist's Staff", "Staff of Arcane Might", "Deity's Scepter"]
Archmage.TierTwo = {"Conduit":10, "Lightning Aura":20, "Natural Aura":40, "Elemental Aura":65, "Sacred Aura":125}
Archmage.TierTwoLIST = ["Conduit", "Lightning Aura", "Natural Aura", "Elemental Aura", "Sacred Aura"]
Archmage.Upgrades = ["Magic", "Health"]
Archmage.UpgradesREAL = [Archmage.MAGIC, Archmage.HP]

def LoneAttack(LoneWolf, BadGuy):
    LoneWolf.AGI = LoneWolf.AGI + 15
    Crit = CriticalChance(Classes, Hero)
    Damage = (LoneWolf.AGI*(random.randrange(8,10)+1)/10+LoneWolf.STR*(random.randrange(6,8)+1)/10)*Crit
    print (Classes[Hero].name,"struck a Headshot!\n"+ BadGuy.name, "received", round(Damage), "damage!")
    LoneWolf.AGI = LoneWolf.AGI - 15
    CriticalHit(Crit)
    return round(Damage)

def LoneSkill(LoneWolf, BadGuy):
    Damage = 0
    Crit = CriticalChance(Classes, Hero)
    print (Classes[Hero].name, "unleashed Limit Break: Bullet Rain!")
    for i in range(5):
        LuckyShot = random.randrange(5)+1
        if LuckyShot == 1 or LuckyShot == 2 or LuckyShot == 3:
            SideDMG = (LoneWolf.AGI*(random.randrange(5,15)+1)/10+LoneWolf.STR*(random.randrange(5,15)+1)/10)*Crit
            Damage = Damage + SideDMG
            print ("The bullet struck!", round(SideDMG), "damage dealt!")
            CriticalHit(Crit)
        else:
            print ("The bullet missed.")
    print ("A total of", round(Damage), "damage was dealt to", BadGuy.name+"!")
    return round(Damage)
    
LoneWolf = Characters()
LoneWolf.job = "Lone Wolf"
LoneWolf.STR = 10
LoneWolf.MAGIC = 0
LoneWolf.AGI = 15
LoneWolf.HP = 345
LoneWolf.CurrentHP = 195
LoneWolf.LIMIT = 4
LoneWolf.MoveSet = ["Headshot", "Bullet Rain"]
LoneWolf.Explain = {"Headshot":"An attack with a high chance of landing a critical hit.", "Bullet Rain":"A Limit Break highly dependant on luck. Five powerful bullets are shot, each with 60% chance of success."}
LoneWolf.ExecuteMove = [LoneAttack,LoneSkill]
LoneWolf.TierOneLevel, LoneWolf.TierTwoLevel = 0, 0
LoneWolf.TierOne = {"Revolver":5, "Modified Revolver":10, "Ancient Blaster":15, "Hellfire Blaster":20, "Sanjeeve's Glock":25}
LoneWolf.TierOneLIST = ["Revolver", "Modified Revolver", "Ancient Blaster", "Hellfire Blaster", "Sanjeeve's Glock"]
LoneWolf.TierTwo = {"Cloth Uniform":1, "Army Uniform":2, "Gunslinger's Uniform":4, "Desperado's Uniform":8, "Assasin's Attire":15}
LoneWolf.TierTwoLIST = ["Cloth Uniform", "Army Uniform", "Gunslinger's Uniform", "Desperado's Uniform", "Assasin's Attire"]
LoneWolf.Upgrades = ["Strength", "Agility"]
LoneWolf.UpgradesREAL = [LoneWolf.STR, LoneWolf.AGI]
    
Classes = [Berserker, Hemomancer, Weaponmaster, Archmage, LoneWolf]

def MonsterPhys(BadGuy, Classes, Hero, Crit):
    Damage = BadGuy.STR * (random.randrange(2, 20, 2)+1)/10 * Crit
    print (BadGuy.name, "used", BadGuy.MoveSet[0]+"!\n"+ Classes[Hero].name, "received", round(Damage), "damage!")
    return round(Damage)

def MonsterMagic(BadGuy, Classes, Hero, Crit):
    Damage = BadGuy.MAGIC * (random.randrange(6, 16, 2)+1)/10 * Crit
    print (BadGuy.name, "used", BadGuy.MoveSet[0]+"!\n"+ Classes[Hero].name, "received", round(Damage), "damage!")
    return round(Damage)

def SamuraiSkill(BadGuy, Classes, Hero):
    Crit = MonsterFatality(BadGuy)
    Meow = random.randrange(10)+1
    if Meow == 1 or Meow == 2 or Meow == 3:
        Rage = 0
        if BadGuy.HP/Samurai.HP <= 0.10:
            Rage = 1
        elif BadGuy.HP/Samurai.HP <= 0.25:
            Rage = 0.75
        elif BadGuy.HP/Samurai.HP <= 0.50:
            Rage = 0.5
        elif BadGuy.HP/Samurai.HP <= 0.75:
            Rage = 0.25
        Damage = BadGuy.STR*(random.randrange(2, 20, 2)+1)/10*Crit + (BadGuy.STR*(random.randrange(3, 15, 3)+1)/10*Crit)*Rage
        print (BadGuy.name, "used", BadGuy.MoveSet[1]+"!\n"+ Classes[Hero].name, "received", round(Damage), "damage!")
    else:
        Damage = MonsterPhys(BadGuy, Classes, Hero, Crit)
    CriticalHit(Crit)
    return round(Damage)

def AssasinSkill(BadGuy, Classes, Hero):
    Crit = MonsterFatality(BadGuy)
    Meow = random.randrange(10)+1
    if Meow == 1 or Meow == 2 or Meow == 3:
        BadGuy.AGI = BadGuy.AGI + 15
        Damage = (BadGuy.AGI*(random.randrange(2,5,1)+1)/10+BadGuy.STR*(random.randrange(5,8)+1)/10)*Crit
        print (BadGuy.name, "used", BadGuy.MoveSet[1]+"!\n"+ Classes[Hero].name, "received", round(Damage), "damage!")
        BadGuy.AGI = BadGuy.AGI - 15
    else:
        Damage = MonsterPhys(BadGuy, Classes, Hero, Crit)
    CriticalHit(Crit)
    return round(Damage)

def DMageSkill(BadGuy, Classes, Hero):
    Crit = MonsterFatality(BadGuy)
    Meow = random.randrange(10)+1
    if Meow == 1 or Meow == 2 or Meow == 3 or Meow == 4 or Meow == 5:
        Damage = BadGuy.MAGIC*(random.randrange(5,10)+1)/10*Crit
        print (BadGuy.name, "used", BadGuy.MoveSet[1]+"!\n"+ Classes[Hero].name, "received", round(Damage), "damage!")
    else:
        Damage = MonsterMagic(BadGuy, Classes, Hero, Crit)
    CriticalHit(Crit)
    return round(Damage)

def ZombieSkill(BadGuy, Classes, Hero):
    Crit = MonsterFatality(BadGuy)
    LS = 0.5
    Meow = random.randrange(10)+1
    if Meow == 1 or Meow == 2:
        Damage = BadGuy.STR*(random.randrange(5,10,1)+1)/10*Crit
        LifestealMonster(Damage, LS, BadGuy)
        print (BadGuy.name, "used", BadGuy.MoveSet[1]+"!\n"+ Classes[Hero].name, "received", round(Damage), "damage!\n"+ BadGuy.name, "healed", round(LS*Damage), "HP!")
    else:
        Damage = MonsterPhys(BadGuy, Classes, Hero, Crit)
    CriticalHit(Crit)
    return round(Damage)

def BansheeSkill(BadGuy, Classes, Hero):
    Crit = MonsterFatality(BadGuy)
    Meow = random.randrange(10)+1
    if Meow == 1 or Meow == 2 or Meow == 3:
        Damage = BadGuy.MAGIC*(random.randrange(8,15)+1)/10*Crit
        print (BadGuy.name, "used", BadGuy.MoveSet[1]+"!\n"+ Classes[Hero].name, "received", round(Damage), "damage!")
    else:
        Damage = MonsterMagic(BadGuy, Classes, Hero, Crit)
    CriticalHit(Crit)
    return round(Damage)

def StatueRegular(BadGuy, Classes, Hero, mUltimate):
    Crit = MonsterFatality(BadGuy)
    Meow = random.randrange(10)+1
    if mUltimate >= 100:
        Damage = BadGuy.MAGIC*(random.randrange(20,30)+1)/10*Crit
        print (BadGuy.name, "unleased Limit Break: Thousand Broken Shards!\n"+ Classes[Hero].name, "received", round(Damage), "damage!")
        mUltimate = 0
    elif Meow == 1 or Meow == 2:
        LS = 1
        Damage = BadGuy.MAGIC*(random.randrange(5,8)+1)/10*Crit
        LifestealMonster(Damage, LS, BadGuy)
        print (BadGuy.name, "used", "Breathe!\n"+ Classes[Hero].name, "received", round(Damage), "damage!\n"+ BadGuy.name, "healed", round(LS*Damage), "HP!")
    elif Meow == 3 or Meow == 4 or Meow == 5:
        Damage = BadGuy.MAGIC*(random.randrange(9,15,3)+1)/10*Crit
        print (BadGuy.name, "used", "Punish!\n"+Classes[Hero].name, "received", round(Damage), "damage!")
    elif Meow == 6 or Meow == 7 or Meow == 8 or Meow == 9 or Meow == 10:
        Damage = BadGuy.MAGIC*(random.randrange(12,24,3)+1)/10*Crit
        print (BadGuy.name, "used", "Chaotic Slam!\n"+Classes[Hero].name, "received", round(Damage), "damage!")
    CriticalHit(Crit)
    return round(Damage), mUltimate

def GhoulRegular(BadGuy, Classes, Hero, mUltimate):
    Crit = MonsterFatality(BadGuy)
    Meow = random.randrange(10)+1
    if mUltimate >= 100:
        Damage = BadGuy.MAGIC*(random.randrange(10,25,5)+1)/10*Crit
        print (BadGuy.name, "unleased Limit Break: Wailing Scythe!\n"+Classes[Hero].name, "received", round(Damage), "damage!")
        mUltimate = 0
    elif Meow == 1 or Meow == 2 or Meow == 3 or Meow == 4:
        LS = 0.1
        Damage = BadGuy.MAGIC*(random.randrange(9,15,3)+1)/10*Crit
        LifestealMonster(Damage, LS, BadGuy)
        print (BadGuy.name, "used", "Reap!\n"+Classes[Hero].name, "received", round(Damage), "damage!\n"+BadGuy.name, "healed", round(LS*Damage), "HP!")
    elif Meow == 5 or Meow == 6 or Meow == 7:
        Damage = BadGuy.MAGIC*(random.randrange(6,12,2)+1)/10*Crit
        print (BadGuy.name, "used", "Fear!\n"+Classes[Hero].name, "received", round(Damage), "damage!")
    elif Meow == 8 or Meow == 9 or Meow == 10:
        Damage = BadGuy.MAGIC*(random.randrange(5,8)+1)/10*Crit
        print (BadGuy.name, "used Chains of Destiny!\n"+Classes[Hero].name, "received", round(Damage), "damage!")
    CriticalHit(Crit)
    return round(Damage), mUltimate

def BlindRegular(BadGuy, Classes, Hero, mUltimate):
    Damage = 0
    Meow = random.randrange(10)+1
    if mUltimate >= 100:
        neko = 0
        for i in range(random.randrange(5,10,1)+1):
            Crit = MonsterFatality(BadGuy)
            neko = neko + 1
            Damage = Damage + (BadGuy.STR*(random.randrange(6,10,2)+1)/10*Crit)
            CriticalHit(Crit)
        print (BadGuy.name, "used Limit Break: Awakening!\n"+str(neko), "hits were executed.\n"+Classes[Hero].name, "received", round(Damage), "damage!")
    elif Meow == 1 or Meow == 2 or Meow == 3:
        for i in range(3):
            Crit = MonsterFatality(BadGuy)
            Damage = Damage + (BadGuy.STR*(random.randrange(7,10,2)+1)/10*Crit)
            CriticalHit(Crit)
        print (BadGuy.name, "used", "Tri-Slash!\n", Classes[Hero].name+"received", round(Damage), "damage!")
    elif Meow == 4 or Meow == 5:
        BadGuy.HP = BadGuy.HP + round(BadGuy.MaxHP*0.02)
        BadGuy.STR = BadGuy.STR + (BadGuy.STR * 0.05)
        print (BadGuy.name, "used", "Battle Condition!\nHealth and Strength replenished!")
    elif Meow == 6 or Meow == 7 or Meow == 8 or Meow == 9 or Meow == 10:
        Crit = MonsterFatality(BadGuy)
        Damage = Damage + (BadGuy.STR+BadGuy.AGI)*(random.randrange(4,14,2)+1)/10
        print (BadGuy.name, "unleashed", "Assasination!\n"+Classes[Hero].name, "received", round(Damage), "damage!")
    return round(Damage), mUltimate

Samurai = Characters() #Monster Stats
Samurai.name = "Tainted Samurai"
Samurai.STR = 8
Samurai.HP = 170
Samurai.MaxHP = 170
Samurai.AGI = 8
Samurai.MoveSet = ["Slice", "Cursed Bushido"]
Samurai.ATTACK = [SamuraiSkill]

Banshee = Characters()
Banshee.name = "Banshee"
Banshee.MAGIC = 10
Banshee.HP = 150
Banshee.MaxHP = 150
Banshee.AGI = 5
Banshee.MoveSet = ["Scream", "Soul Touch"]
Banshee.ATTACK = [BansheeSkill]

Assasin = Characters()
Assasin.name = "Masked Assasin"
Assasin.STR = 7
Assasin.MaxHP = 125
Assasin.HP = 125
Assasin.AGI = 10
Assasin.MoveSet = ["Attack", "Backstab"]
Assasin.ATTACK = [AssasinSkill]

Zombie = Characters()
Zombie.name = "Rotten Zombie"
Zombie.STR = 5
Zombie.HP = 200
Zombie.MaxHP = 200
Zombie.AGI = 5
Zombie.MoveSet = ["Attack", "Flesh Gnaw"]
Zombie.MaxHP = 325
Zombie.ATTACK = [ZombieSkill]

DMage = Characters()
DMage.name = "Rogue Spellslayer"
DMage.MAGIC = 15
DMage.HP = 130
DMage.MaxHP = 130
DMage.AGI = 5
DMage.MoveSet = ["Pierce", "Corrupt"]
DMage.ATTACK = [DMageSkill]

BossOne = Characters()
BossOne.name = "Breathing Statue of Sin"
BossOne.MAGIC = 20
BossOne.AGI = 5
BossOne.HP = 275
BossOne.LIMIT = 5
BossOne.CurrentLimit = 25
BossOne.MaxHP = 600
BossOne.ATTACK = [StatueRegular]

BossTwo = Characters()
BossTwo.name = "Chained Ghoul of Regret"
BossTwo.MAGIC = 25
BossTwo.AGI = 5
BossTwo.HP = 350
BossTwo.LIMIT = 10
BossTwo.CurrentLimit = 15
BossTwo.MaxHP = 700
BossTwo.ATTACK = [GhoulRegular]

BossThree = Characters()
BossThree.name = "The Blind Swordsman"
BossThree.STR = 30
BossThree.AGI = 15
BossThree.HP = 430
BossThree.LIMIT = 10
BossThree.CurrentLimit = 15
BossThree.MaxHP = 800
BossThree.ATTACK = [BlindRegular]

Monsters = [Samurai, Banshee, Assasin, Zombie, DMage]
Bosses = [BossOne, BossTwo, BossThree]
def FirstEquip(Classes, Hero): #Initial equipment
    Classes[Hero].UpgradesREAL[0] = Classes[Hero].UpgradesREAL[0] + Classes[Hero].TierOne[Classes[Hero].TierOneLIST[Classes[Hero].TierOneLevel]]
    Classes[Hero].UpgradesREAL[1] = Classes[Hero].UpgradesREAL[1] + Classes[Hero].TierTwo[Classes[Hero].TierTwoLIST[Classes[Hero].TierTwoLevel]]
def Initialization(Classes, Hero, Choice):#Removes bonus from the previous set of equips and applies the stronger, new ones.
    if Choice == "1":
        Classes[Hero].TierOneLevel = Classes[Hero].TierOneLevel + 1
        Classes[Hero].UpgradesREAL[0] = Classes[Hero].UpgradesREAL[0] - Classes[Hero].TierOne[Classes[Hero].TierOneLIST[(Classes[Hero].TierOneLevel)-1]]
        Classes[Hero].UpgradesREAL[0] = Classes[Hero].UpgradesREAL[0] + Classes[Hero].TierOne[Classes[Hero].TierOneLIST[Classes[Hero].TierOneLevel]]
        print ("\nCongratulations!", Classes[Hero].name+"'s", Classes[Hero].TierOneLIST[(Classes[Hero].TierOneLevel)-1], "has been upgraded to", Classes[Hero].TierOneLIST[Classes[Hero].TierOneLevel]+"!\n")
    elif Choice == "2":
        Classes[Hero].TierTwoLevel = Classes[Hero].TierTwoLevel + 1
        Classes[Hero].UpgradesREAL[1] = Classes[Hero].UpgradesREAL[1] - Classes[Hero].TierTwo[Classes[Hero].TierTwoLIST[(Classes[Hero].TierTwoLevel)-1]]
        Classes[Hero].UpgradesREAL[1] = Classes[Hero].UpgradesREAL[1] + Classes[Hero].TierTwo[Classes[Hero].TierTwoLIST[Classes[Hero].TierTwoLevel]]
        print ("\nCongratulations!", Classes[Hero].name+"'s", Classes[Hero].TierTwoLIST[(Classes[Hero].TierTwoLevel)-1], "has been upgraded to", Classes[Hero].TierTwoLIST[Classes[Hero].TierTwoLevel]+"!\n")
    elif Choice == "3":
        Meow = random.randrange(6.0,10.0)/10.0
        Classes[Hero].CurrentHP = Classes[Hero].CurrentHP + (float(Meow))*Classes[Hero].HP
        if Classes[Hero].CurrentHP > Classes[Hero].HP:
            Classes[Hero].CurrentHP = Classes[Hero].HP
        print ("\nCongratulations!", Classes[Hero].name, "has been healed for", round((float(Meow)*Classes[Hero].HP)), "HP!\n")
def Adjust(Classes, Hero): #Adjusting player stats with initial equips
    if Hero == 0:
        Berserker.STR, Berserker.HP = Classes[Hero].UpgradesREAL[0], Classes[Hero].UpgradesREAL[1]
    elif Hero == 1:
        Hemomancer.MAGIC, Hemomancer.LS = Classes[Hero].UpgradesREAL[0], Classes[Hero].UpgradesREAL[1]
    elif Hero == 2:
        Weaponmaster.STR, Weaponmaster.AGI = Classes[Hero].UpgradesREAL[0], Classes[Hero].UpgradesREAL[1]
    elif Hero == 3:
        Archmage.MAGIC, Archmage.HP = Classes[Hero].UpgradesREAL[0], Classes[Hero].UpgradesREAL[1]
    elif Hero == 4:
        LoneWolf.STR, LoneWolf.AGI = Classes[Hero].UpgradesREAL[0], Classes[Hero].UpgradesREAL[1]
def Upgrades(Classes, Hero, UPPoints): #Equips/Armor Aspect
    print ("\nYou have", UPPoints, "upgrade points.\n")
    if UPPoints > 0:
        Choice = input("You are eligible for a LEVEL UP! Would you like to commence with it? 'Y' for yes.\n(Warning: It costs one upgrade point)\n--> ")
        if "y" in Choice or "Y" in Choice:
            UPPoints = UPPoints - 1
            while True:
                print ("\nWhat would you like to do?\n(1) Upgrade", Classes[Hero].Upgrades[0]+"?\n(2) Upgrade", Classes[Hero].Upgrades[1]+"?\n(3) Heal")
                Choice = input("--> ")
                if "1" in Choice:
                    if Classes[Hero].TierOneLevel == 4:
                        print ("\nYou have reached the maximum level in this category.")
                    else:
                        Initialization(Classes, Hero, Choice)
                        break
                elif "2" in Choice:
                    if Classes[Hero].TierTwoLevel == 4:
                        print ("\nYou have reached the maximum level in this category.")
                    else:
                        Initialization(Classes, Hero, Choice)
                        break
                elif "3" in Choice:
                    Initialization(Classes, Hero, Choice)
                    break
                else:
                    print ("\nPlease pick a valid choice!")
        else:
            print ("  ")
    return UPPoints
def MapSetUp(Monsters, Bosses, MovementDict, MovementDictDesc, MapDescDict, AllFloors, SpecFloors):#Randomizing of Monsters
    AllFloorsList = ["OneRoomOne", "OneRoomTwo", "OneRoomThree", "OneRoomFour", "OneRoomFive", "OneRoomSix", "OneRoomSeven", "OneRoomEight", "OneRoomNine", "TwoRoomOne", "TwoRoomTwo", "TwoRoomThree", "TwoRoomFour", "TwoRoomFive", "TwoRoomSix", "TwoRoomSeven", "TwoRoomEight", "TwoRoomNine", "TwoRoomTen", "TwoRoomEleven", "ThreeRoomOne", "ThreeRoomTwo", "ThreeRoomThree", "ThreeRoomFour", "ThreeRoomFive", "ThreeRoomSix", "ThreeRoomSeven", "ThreeRoomEight", "ThreeRoomNine", "ThreeRoomTen", "OneSpecOne", "OneSpecTwo", "OneSpecThree", "TwoSpecOne", "TwoSpecTwo", "TwoSpecThree", "ThreeSpecOne", "ThreeSpecTwo", "ThreeSpecThree"]
    moveup = 0
    bosscheck = 0
    for i in range(30):
        AllFloors[AllFloorsList[moveup]] = Monsters[random.randrange(5)]
        moveup = moveup + 1
    for i in range(3):
        Spec = ["Bosses", "Stair", "Treasure"]
        for i in range(3):
            counter = 0
            while counter == 0:
                Sanjeeve = random.randrange(3)
                SpecFloors[AllFloorsList[moveup]] = Spec[Sanjeeve]
                if "X" in Spec[Sanjeeve]:
                    counter = 0
                else:
                    counter = 1
            if "Bosses" in SpecFloors[AllFloorsList[moveup]]:
                SpecFloors[AllFloorsList[moveup]] = Bosses[bosscheck]
                bosscheck = bosscheck + 1
            Spec[Sanjeeve] = "X"
            moveup = moveup + 1
    MapDescFloorList = ["OneRoomOne", "OneRoomTwo", "OneRoomThree", "OneRoomFour", "OneRoomFive", "OneRoomSix", "OneRoomSeven", "OneRoomEight", "OneRoomNine", "TwoRoomOne", "TwoRoomTwo", "TwoRoomThree", "TwoRoomFive", "TwoRoomSix", "TwoRoomSeven", "TwoRoomNine", "TwoRoomTen", "TwoRoomEleven", "ThreeRoomOne", "ThreeRoomTwo", "ThreeRoomThree", "ThreeRoomFour", "ThreeRoomFive", "ThreeRoomSix", "ThreeRoomSeven", "ThreeRoomEight", "ThreeRoomNine", "ThreeRoomTen", "OneSpecOne", "OneSpecTwo", "OneSpecThree", "SpawnPoint1", "TwoSpecOne", "TwoSpecTwo", "TwoSpecThree", "SpawnPoint2", "TwoRoomFour", "TwoRoomEight", "ThreeSpecOne", "ThreeSpecTwo", "ThreeSpecThree", "SpawnPoint3"]
    MapDescOne = ["\nYou stand in a dark hallway where only a solitary candle illuminates your path.\n", "\nYou can see a giant, eerie statue in the corner. It seems to stare at you with cold eyes.\n","\nYou have reached the balcony of the floating castle; mountains and forests whiz past below you. It's a long way down.\n","\nYou are in a strangely chilly room lit up by thousands of small candles.\n",  "\nThe room is filled with smoke. A strong smell of incense fills your nostrils.\n", "\nYou've reached the end of the open hallway. The moon and the clouds of the night sky can be seen.\n", "\nA pond lies in front of you. Inside, you see numerous small fish.\n", "\nA statue with an inscription lies in front of you. The words seems to have been scribbled off.\n", "\nYou traverse through a long, dark hallway. The wooden floor creaks as you walk.\n"]
    MapDescOneSpec = ["\nYou find an empty pedestal in front of you. Where did the statue go... ?\n", "\nYou have encountered a giant gate etched with countless embroideries and gems.\n",  "\nAn empty seat lies in view; it probably belongs to the head priest of the temple.\n", "\nThis is the hidden room from where you have infiltrated the fortress. Your trusty airship lies below.\n"]
    MapDescTwo = ["\nA large apparatus lies in front of you. You probably should not touch it.\n", "\nYou walk into a room filled with clocks. Tick tock, tick tock; they go.\n", "\nA clock ticks loudly along with the monotonous huming of engines.\n", "\nA piece of paper lies atop a dark stain on the ground; 'Beware the Ghoul'...\n", "\nThere are pieces of shattered glass on the floor... Best tread carefully.\n", "\nThere is a bulletin board up ahead with a paper that dates a few months back.\n<We're shutting this place down. Too many casualties from this 'demon'.>\n", "\nAn odd smell attracts you into an old room. However, it is completely empty on the inside.\n", "\nYou walk into an old, rusted room. Inside, you see an old samurai armour with a bolded '23' printed on it.\n", "\nA rusted humanoid robot lays broken on the ground. Its eyes flash a momentary red as you pass by.\n"]
    MapDescTwoSpec = ["\nYou enter a room where a skull lies on the ground amongst a clutter of nuts and bolts...\n", "\nYou've encountered a hidden room with skulls stacked on the shelves... spooky.\n", "\nYou see stains on the floor and the walls of the room... Is it oil or... blood?\n", "\nYou have reached an old engine room. A danger sign is hung on the gate.\n", "\nYou approach a dark, humid room smelling strongly of oil.\nA weird engraving is on the wall to the East... Perhaps it refers to a secret of some sort?\n", "\nYou hear gears whirling behind the rusty hallway walls.\nThe wall to your south sounds hollow... Perhaps it can be broken down?\n"]
    MapDescThree = ["\nYou place your eyes upon the giant harp lying in the middle of the courtyard. It seems to be made out of pure gold...\n", "\nYou walk upon a white bridge that divides the two sections of the courtyard in half.\n", "\nYou have reached the balcony on the third floor. The lights from the cities below look identical to the stars up above.\n", "\nYou are surrounded by roses. Although beautiful, their thorns are as sharp as swords...\n", "\nYou are surrounded by dandelions. Although it is mid-summer, they are still bright yellow.\n", "\nA statue of a giant bear comes in your sight. Although its size is intimidating, its face is pretty cute.\n", "\nYou gaze upon the minature river flowing through the garden. It makes a quiet, serene sound.\n", "\nYou have reached the observatory deck. One can see the whole courtyard from here.\n", "\nLying flat on the paved pathway leading to the topmost area of the fortress, is a broken bust of an ancient Goddess.\n", "\nYou've reached the apex of the floating castle... You can almost see the neighbouring countries from here.\n"]
    MapDescThreeSpec = ["\nA giant throne is up ahead. It is lavishly decorated with treasures from all over the world.\n", "\nA statue of a giant cat comes in your sight. The cat seems to be holding two swords in its paws.\n", "\nYou approach the inner part of the garden. Statues of ancient deities make a circle in the courtyard.\n", "\nSmall flights of stairs lead you to a large open flower garden. The moonlight illuminates the dark atmosphere.\n"]
    #Randomizing of Map Description
    random.shuffle(MapDescOne), random.shuffle(MapDescTwo), random.shuffle(MapDescThree)
    moveup= 0
    for i in range(9):
        MapDescDict[MapDescFloorList[moveup]] = MapDescOne[i]
        moveup = moveup + 1
    for i in range(9):
        MapDescDict[MapDescFloorList[moveup]] = MapDescTwo[i]
        moveup= moveup + 1
    for i in range(10):
        MapDescDict[MapDescFloorList[moveup]] = MapDescThree[i]
        moveup = moveup + 1
    for i in range(4):
        MapDescDict[MapDescFloorList[moveup]] = MapDescOneSpec[i]
        moveup = moveup + 1
    for i in range(6):
        MapDescDict[MapDescFloorList[moveup]] = MapDescTwoSpec[i]
        moveup = moveup + 1
    for i in range(4):
        MapDescDict[MapDescFloorList[moveup]] = MapDescThreeSpec[i]
        moveup = moveup + 1
    return MapDescDict, AllFloors, SpecFloors
def Movement(CurrentPosition, Classes, Hero, Proceed): #Player movement + traps + restrictions
    Walk = 0
    Restriction = []
    while True: #Movement and Restrictions
        if CurrentPosition == 12 or CurrentPosition == 13 or CurrentPosition == 14 or CurrentPosition == 18 or CurrentPosition == 8:
            Walk = input("\nYou can move North(1), East(2), South(3) or West(4)\n--> ")
        elif CurrentPosition == 31 or CurrentPosition == 41:
            Walk = input("\nYou can move North(1), East(2) or South(3)\n--> ")
            Restriction = ["4"]
        elif CurrentPosition == 63 or CurrentPosition == 33:
            Walk = input("\nYou can move East(2), South(3) or West(4)\n--> ")
            Restriction = ["1"]
        elif CurrentPosition == 35:
            Walk = input("\nYou can move North(1), South(3) or West(4)\n--> ")
            Restriction = ["2"]
        elif CurrentPosition == 73:
            Walk = input("\nYou can move North(1), East(2) or West(4)\n--> ")
            Restriction = ["3"]
        elif CurrentPosition == 7 or CurrentPosition == 72:
            Walk = input("\nYou can move East(2) or South(3)\n--> ")
            Restriction = ["1", "4"]
        elif CurrentPosition == 17 or CurrentPosition == 51 or CurrentPosition == 79 or CurrentPosition == 62:
            Walk = input("\nYou can move North(1) or East(2)\n--> ")
            Restriction = ["3", "4"]
        elif CurrentPosition == 9 or CurrentPosition == 74:
            Walk = input("\nYou can move South(3) or West(4)\n--> ")
            Restriction = ["1", "2"]
        elif CurrentPosition == 19 or CurrentPosition == 64 or CurrentPosition == 77 or CurrentPosition == 43:
            Walk = input("\nYou can move North(1) or West(4)\n--> ")
            Restriction = ["2", "3"]
        elif CurrentPosition == 46 or CurrentPosition == 36 or CurrentPosition == 68:
            Walk = input("\nYou can move North(1) or South(3)\n--> ")
            Restriction = ["2", "4"]
        elif CurrentPosition == 32 or CurrentPosition == 34:
            Walk = input("\nYou can move East(2) or West(4)\n--> ")
            Restriction = ["1", "3"]
        elif CurrentPosition == 11 or CurrentPosition == 76:
            Walk = input("\nYou can only move East(2)\n--> ")
            Restriction = ["1", "3", "4"]
        elif CurrentPosition == 15 or CurrentPosition == 52 or CurrentPosition == 80:
            Walk = input("\nYou can only move West(4)\n--> ")
            Restriction = ["1", "2", "3"]
        elif CurrentPosition == 23 or CurrentPosition == 40:
            Walk = input("\nYou can only move North(1)\n--> ")
            Restriction = ["2", "3", "4"]
        elif CurrentPosition == 3 or CurrentPosition == 26 or CurrentPosition == 30 or CurrentPosition == 57 or CurrentPosition == 59:
            Walk = input("\nYou can only move South(3)\n--> ")
            Restriction = ["1", "2", "4"]
        if "1" in Walk or "2" in Walk or "3" in Walk or "4" in Walk or "5" in Walk or "6" in Walk or "7" in Walk or "8" in Walk or "9" in Walk or "0" in Walk:
            if int(Walk) >4 or int(Walk)<1:
                print ("\nPlease pick a valid movement choice.\n")
                return CurrentPosition, 0
        else:
            print ("\nPlease pick a valid movement choice.\n")
            return CurrentPosition, 0
        if CurrentPosition == 41 and Walk == "2": #Trap Question
            t1 = time()
            Answer = input("\nThe strange engraving is a riddle... It says you have five seconds to answer...\nWhat goes on four legs in the morning, on two legs at noon, and on three legs in the evening?\n--> ")
            t2 = time()
            if ("Human" in Answer or "HUMAN" in Answer or "human" in Answer or "Person" in Answer or "PERSON" in Answer or "person" in Answer or "Man" in Answer or "man" in Answer or "MAN" in Answer) and (t2 - t1) <= 5:
                print ("\nThe wall vibrated and opened up; revealing a dark corridor leading to a hidden room.")
                return 43, 1
            else:
                Damage = random.randrange(15,30,3)+1
                print ("\nYou were slashed by a unseen weapon...\n", Classes[Hero].name, "lost", Damage, "HP.")
                Classes[Hero].CurrentHP = Classes[Hero].CurrentHP - Damage
        elif CurrentPosition == 33 and Walk == "3": #Requirement Special Movement
            print ("\nYou find weakness in the wall; something lies behind it. If you are strong enough, you might be able to break it.")
            if Classes[Hero].STR >= 15:
                print ("You break the wall with your fist! Pure strength!\nYou have discovered a hidden corridor.")
                return 43, 1
            elif Classes[Hero].MAGIC >= 15:
                print ("You case a spell on the wall and burn it into a crisp! The Arcane Arts prevails!\nYou have discovered a hidden corridor.")
                return 43, 1
            else:
                print ("You were not able to break the wall. Perhaps you were not meant to do this...\n")
        elif CurrentPosition == 43:
            if Walk == "1":
                print ("\nYou take the hidden tunnel...")
                return 33, 1
            elif Walk == "4":
                print ("\nYou take the hidden corridor...")
                return 41, 1
        elif Walk in Restriction:
            print ("\nPlease pick a valid movement choice.\n")
            return CurrentPosition, 0
        elif Walk not in Restriction:
            if Walk == "1":
                CurrentPosition = CurrentPosition - 5
            elif Walk == "2":
                CurrentPosition = CurrentPosition + 1
            elif Walk == "3":
                CurrentPosition = CurrentPosition + 5
            elif Walk == "4":
                CurrentPosition = CurrentPosition - 1
            return CurrentPosition, 1
def BattleScan(CurrentPosition, Ultimate, Classes, Hero, Key, KeyCount, UPPoints, Monsters):#Function that determines what is in the map; whether it is a fight/treasure/stairs
    if MovementDict[CurrentPosition] == "SAFE" or CurrentPosition == 23 or CurrentPosition == 76 or CurrentPosition == 52:
        print ("There are no monsters in the area; it is safe.\n")
        return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
    elif CurrentPosition == 11 or CurrentPosition == 15 or CurrentPosition == 3 or CurrentPosition == 26 or CurrentPosition == 30 or CurrentPosition == 43 or CurrentPosition == 80 or CurrentPosition == 57 or CurrentPosition == 59:        
        if SpecFloors[MovementDict[CurrentPosition]] == BossOne or SpecFloors[MovementDict[CurrentPosition]] == BossTwo or SpecFloors[MovementDict[CurrentPosition]] == BossThree:
            BadGuy = SpecFloors[MovementDict[CurrentPosition]]
            print (BadGuy.name, "stands in front of you. Prepare for battle!")
            Choice = input("\nYou have encountered the boss of the floor...\nDo you want to engage it in battle? ('Y' for Yes)\n--> ")
            if "Y" in Choice or "y" in Choice:
                mUltimate = 0
                Ultimate, Win = BossBattle(BadGuy, Ultimate, Classes, Hero, mUltimate)
                if Win == 0:
                    print ("Game Over...")
                    GameOver()
                elif Win == 1:
                    MovementDict[CurrentPosition] = "SAFE"
                    Key[KeyCount] = "DEFEATED"
                    KeyCount = KeyCount + 1
                    if random.randrange(10)+1 <= 5:
                        print ("Congratulations! You have unlocked an upgrade point! Access 'Equip' to allocate your LEVEL UP.\n")
                        UPPoints = UPPoints + 1    
                    return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
            else:
                print ("\nYou have chosen not to engage the boss.\n")
                return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
        elif SpecFloors[MovementDict[CurrentPosition]] == "Treasure":
            print ("You have found the treasure room!\nYou have unlocked two upgrade points! Access 'Equip' to allocate your LEVEL UP.\n")
            UPPoints, SpecFloors[MovementDict[CurrentPosition]] = UPPoints + 2, "Done"
            return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
        elif SpecFloors[MovementDict[CurrentPosition]] == "Done":
             print ("You have already discovered the treasure here. The room is empty.\n")
             return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
        elif SpecFloors[MovementDict[CurrentPosition]] == "Stair":
            print ("You have found the pathway to ascension but it shall only open if you have defeated this floor's champion.")
            if CurrentPosition <= 23:
                if Key[0] == "DEFEATED":
                    UP = input("You have defeated the floor boss and are eligible to ascend. However, you cannot come return here. Would you like to proceed? ('Y' for Yes)\n--> ")
                    if "Y" in UP or "y" in UP:
                        CurrentPosition = 52
                        print ("\nThe gate opens...\n"+ MapDescDict[MovementDictDesc[CurrentPosition]])
                        return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
                    else:
                        print ("  ")
                        return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
                else:
                    print ("  ")
                    return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
            elif CurrentPosition > 23 and CurrentPosition < 53:
                if Key[1] == "DEFEATED":
                    UP = input("You have defeated the floor boss and are eligible to ascend. However, you cannot come return here. Would you like to proceed? ('Y' for Yes)\n--> ")
                    if "Y" in UP or "y" in UP:
                        CurrentPosition = 76
                        print ("\nThe gate opens...\n"+ MapDescDict[MovementDictDesc[CurrentPosition]])
                        return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
                    else:
                        print ("  ")
                        return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
                else:
                    print ("  ")
                    return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
            elif CurrentPosition > 55:
                if Key[2] == "DEFEATED":
                    UP = input("You have defeated the floor boss and are eligible to ascend. However, you cannot come back. Would you like to proceed? ('Y' for Yes)\n--> ")
                    if "Y" in UP or "y" in UP:
                        print ("\nThe gate opens...\nYou have arrived at your destination.\n")
                        Victory()
                    else:
                        print ("  ")
                        return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
                else:
                    print ("  ")
                    return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
        elif SpecFloors[MovementDict[CurrentPosition]] in Monsters:
            BadGuy = SpecFloors[MovementDict[CurrentPosition]]
            print (BadGuy.name, "stands in front of you. Prepare for battle!")
            BadGuy.HP = BadGuy.MaxHP
            Ultimate, Win = Battle(BadGuy, Ultimate, Classes, Hero)
            if Win == 0:
                print ("Game Over...")
                GameOver()
            elif Win == 1:
                MovementDict[CurrentPosition] = "SAFE"
                if random.randrange(10)+1 <= 2:
                    print ("Congratulations! You have unlocked an upgrade point! Access 'Equip' to allocate your LEVEL UP.\n")
                    UPPoints = UPPoints + 1    
                return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
    elif AllFloors[MovementDict[CurrentPosition]] == BossOne:
        BadGuy = AllFloors[MovementDict[CurrentPosition]]
        print (BadGuy.name, "stands in front of you. Prepare for battle!")
        Choice = input("\nYou have encountered the boss of the floor...\nDo you want to engage it in battle? ('Y' for Yes)\n--> ")
        if "Y" in Choice or "y" in Choice:
            mUltimate = 0
            Ultimate, Win = BossBattle(BadGuy, Ultimate, Classes, Hero, mUltimate)
            if Win == 0:
                print ("Game Over...")
                GameOver()
            elif Win == 1:
                MovementDict[CurrentPosition] = "SAFE"
                Key[KeyCount] = "DEFEATED"
                KeyCount = KeyCount + 1
                if random.randrange(10)+1 <= 5:
                    print ("Congratulations! You have unlocked an upgrade point! Access 'Equip' to allocate your LEVEL UP.\n")
                    UPPoints = UPPoints + 1    
                return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
        else:
            print ("\nYou have chosen not to engage the boss.\n")
            return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
    elif AllFloors[MovementDict[CurrentPosition]] in Monsters:
        BadGuy = AllFloors[MovementDict[CurrentPosition]]
        print (BadGuy.name, "stands in front of you. Prepare for battle!")
        BadGuy.HP = BadGuy.MaxHP
        Ultimate, Win = Battle(BadGuy, Ultimate, Classes, Hero)
        if Win == 0:
            print ("Game Over...")
            GameOver()
        elif Win == 1:
            MovementDict[CurrentPosition] = "SAFE"
            if random.randrange(10)+1 <= 2:
                print ("Congratulations! You have unlocked an upgrade point! Access 'Equip' to allocate your LEVEL UP.\n")
                UPPoints = UPPoints + 1    
            return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
    return Ultimate, Key, KeyCount, CurrentPosition, UPPoints
def Battle(BadGuy, Ultimate, Classes, Hero):#Regular battles, looped with recursion
    if Classes[Hero].CurrentHP <= 0:
        print ("\n"+ Classes[Hero].name, "has been slain...")
        return Ultimate, 0
    print ("\nThe heat of battle causes", Classes[Hero].name, "to gain some points in the LIMIT gauge...")
    Ultimate = int(Ultimate) + (Classes[Hero].LIMIT*(random.randrange(1,3)+1)) + (random.randrange(5)+1)
    if Ultimate > 100:
        Ultimate = 100
    print (Classes[Hero].name, "has", str(Classes[Hero].CurrentHP)+"/"+str(Classes[Hero].HP), "HP with", Ultimate, "points in the LIMIT gauge!\n"+ BadGuy.name, "holds", BadGuy.HP, "total HP!\n")
    Checking = 0
    print ("Your choices of attack are", Classes[Hero].MoveSet, "\n'1' for regular, '2' for special  ")
    while Checking == 0:
        Attacko = input("What attack would you like to execute? ")
        Possible = ["1", "2"]
        if Attacko not in Possible:
            print ("Please pick a valid move!")
        elif int(Attacko) == 1:
            Checking = 1
        elif int(Attacko) == 2:
            Checking, Ultimate = LimitBreak(Ultimate)
    Damage = Classes[Hero].ExecuteMove[int(Attacko)-1](Classes[Hero], BadGuy)
    BadGuy.HP = BadGuy.HP - Damage
    if BadGuy.HP <= 0:
        print ("\n"+BadGuy.name, "has been defeated!\n")
        return Ultimate, 1
    print ("\n"+BadGuy.name, "is ready to attack!")
    Damage = BadGuy.ATTACK[0](BadGuy, Classes, Hero)
    Classes[Hero].CurrentHP = Classes[Hero].CurrentHP - Damage
    return Battle(BadGuy, Ultimate, Classes, Hero)
def BossBattle(BadGuy, Ultimate, Classes, Hero, mUltimate): #BossBattles, Uses enemy LIMIT as well.
    if Classes[Hero].CurrentHP <= 0:
        print ("\n"+ Classes[Hero].name, "has been slain...")
        return Ultimate, 0
    print ("\nThe heat of battle causes", Classes[Hero].name, "to gain some points in the LIMIT gauge...")
    print (BadGuy.name, "simmers with power. LIMIT gauge rising...\n")
    Ultimate = int(Ultimate) + (Classes[Hero].LIMIT*(random.randrange(1,3)+1)) + (random.randrange(5)+1)
    mUltimate = int(Ultimate) + (BadGuy.LIMIT*(random.randrange(1,3)+1))
    if Ultimate > 100:
        Ultimate = 100
    print (Classes[Hero].name, "has", str(Classes[Hero].CurrentHP)+"/"+str(Classes[Hero].HP), "HP with", Ultimate, "points in the LIMIT gauge!\n"+ BadGuy.name, "has", BadGuy.HP, "total HP!\n")
    Checking = 0
    print ("Your choices of attack are", Classes[Hero].MoveSet, "\n'1' for regular, '2' for special  ")
    while Checking == 0:
        Attacko = input("What attack would you like to execute? ")
        Possible = ["1", "2"]
        if Attacko not in Possible:
            print ("Please pick a valid move!")
        elif int(Attacko) == 1:
            Checking = 1
        elif int(Attacko) == 2:
            Checking, Ultimate = LimitBreak(Ultimate)
    Damage = Classes[Hero].ExecuteMove[int(Attacko)-1](Classes[Hero], BadGuy)
    BadGuy.HP = BadGuy.HP - Damage
    if BadGuy.HP <= 0:
        print ("\n"+ BadGuy.name, "has been defeated!\nYou have eliminated the boss!\nYou can now proceed to higher floors.\n\n     [YOU ARE FULLY HEALED]     \n\n")
        Classes[Hero].CurrentHP = Classes[Hero].HP
        return Ultimate, 1
    print ("\n"+ BadGuy.name, "charges up for an attack!")
    Damage, mUltimate = BadGuy.ATTACK[0](BadGuy, Classes, Hero, mUltimate)
    Classes[Hero].CurrentHP = Classes[Hero].CurrentHP - Damage
    return BossBattle(BadGuy, Ultimate, Classes, Hero, mUltimate)
def StatsCheck(Classes, Hero):#Checking character's stats
    print ("\n"+Classes[Hero].name+"'s health is", str(Classes[Hero].CurrentHP)+"/"+str(Classes[Hero].HP))
    print (Classes[Hero].name+"'s STR is", Classes[Hero].STR)
    print (Classes[Hero].name+"'s MAGIC is", Classes[Hero].MAGIC)
    print (Classes[Hero].name+"'s AGI is", Classes[Hero].AGI)
    print (Classes[Hero].name+"'s Limit Gauge is", str(Ultimate)+"/100\n")
    print (Classes[Hero].name+", the", Classes[Hero].job+", knows two skills:\n"+ Classes[Hero].MoveSet[0], "-", Classes[Hero].Explain[Classes[Hero].MoveSet[0]], "\n"+ Classes[Hero].MoveSet[1], "-", Classes[Hero].Explain[Classes[Hero].MoveSet[1]]+"\n")
def MapCheck(CurrentPosition, Key): #Boss status - Information
    if CurrentPosition <= 23:
        print ("You are currently on floor one.\nBoss Status -> ", Key[0], "\n")
    elif CurrentPosition > 23 and CurrentPosition < 53:
        print ("You are currently on floor two.\nBoss Status -> ", Key[1], "\n")
    elif CurrentPosition > 55:
        print ("You are currently on floor three.\nBoss Status -> ", Key[2], "\n")
def GameOver():
    while True:
        input = ""
def StartStatueMoves(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition):
    KeyValueSwapSPEC = dict((SpecFloors[k], k) for k in SpecFloors)
    KeyValueSwapDICT = dict((MovementDict[k], k) for k in MovementDict)
    StatuePosition = KeyValueSwapDICT[KeyValueSwapSPEC[Bosses[0]]]
    return StatuePosition
def StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow):
    if MovementDict[StatuePosition+PossibleMovement[Meow]] == "SAFE":
        AllFloors[MovementDictDesc[StatuePosition+PossibleMovement[Meow]]] = BossOne
        Placeholder = "SAFE"
    else:
        Placeholder = AllFloors[MovementDict[StatuePosition+PossibleMovement[Meow]]]
        AllFloors[MovementDict[StatuePosition+PossibleMovement[Meow]]] = BossOne
    return AllFloors, Placeholder
def StatueMoves(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc): 
    while True:
        Meow = random.randrange(4)
        PossibleMovement = [-5, 1, 5, -1]
        if StatuePosition == 13:
            AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
            AllFloors[MovementDict[13]] = Placeholder
            StatuePosition = StatuePosition + PossibleMovement[Meow]
            return AllFloors, SpecFloors, StatuePosition
        elif StatuePosition == 8:
            Restriction = [1]
            if Meow+1 not in Restriction:
                AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
                AllFloors[MovementDict[8]] = Placeholder
                StatuePosition = StatuePosition + PossibleMovement[Meow]
                return AllFloors, SpecFloors, StatuePosition
        elif StatuePosition == 12:
            Restriction = [4]
            if Meow+1 not in Restriction:
                AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
                AllFloors[MovementDict[12]] = Placeholder
                StatuePosition = StatuePosition + PossibleMovement[Meow]
                return AllFloors, SpecFloors, StatuePosition
        elif StatuePosition == 14:
            Restriction = [2]
            if Meow+1 not in Restriction:
                AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
                AllFloors[MovementDict[14]] = Placeholder
                StatuePosition = StatuePosition + PossibleMovement[Meow]
                return AllFloors, SpecFloors, StatuePosition
        elif StatuePosition == 18:
            Restriction = [3]
            if Meow+1 not in Restriction:
                AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
                AllFloors[MovementDict[18]] = Placeholder
                StatuePosition = StatuePosition + PossibleMovement[Meow]
                return AllFloors, SpecFloors, StatuePosition
        elif StatuePosition == 7:
            Restriction = [1, 4]
            if Meow+1 not in Restriction:
                AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
                AllFloors[MovementDict[7]] = Placeholder
                StatuePosition = StatuePosition + PossibleMovement[Meow]
                return AllFloors, SpecFloors, StatuePosition
        elif StatuePosition == 17:
            Restriction = [3, 4]
            if Meow+1 not in Restriction:
                AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
                AllFloors[MovementDict[17]] = Placeholder
                StatuePosition = StatuePosition + PossibleMovement[Meow]
                return AllFloors, SpecFloors, StatuePosition
        elif StatuePosition == 9:
            Restriction = [1, 2]
            if Meow+1 not in Restriction:
                AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
                AllFloors[MovementDict[9]] = Placeholder
                StatuePosition = StatuePosition + PossibleMovement[Meow]
                return AllFloors, SpecFloors, StatuePosition
        elif StatuePosition == 11:
            Restriction = [1, 3, 4]
            if Meow+1 not in Restriction:
                AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
                SpecFloors[MovementDict[11]] = Placeholder
                StatuePosition = StatuePosition + PossibleMovement[Meow]
                return AllFloors, SpecFloors, StatuePosition
        elif StatuePosition == 15:
            Restriction = [1, 2, 3]
            if Meow+1 not in Restriction:
                AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
                SpecFloors[MovementDict[15]] = Placeholder
                StatuePosition = StatuePosition + PossibleMovement[Meow]
                return AllFloors, SpecFloors, StatuePosition
        elif StatuePosition == 23:
            Restriction = [2, 3, 4]
            if Meow+1 not in Restriction:
                AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
                SpecFloors[MovementDict[23]] = Placeholder
                StatuePosition = StatuePosition + PossibleMovement[Meow]
                return AllFloors, SpecFloors, StatuePosition
        elif StatuePosition == 3:
            Restriction = [1, 2, 4]
            if Meow+1 not in Restriction:
                AllFloors, Placeholder = StatueMoveCheck(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc, PossibleMovement, Meow)
                SpecFloors[MovementDict[3]] = Placeholder
                StatuePosition = StatuePosition + PossibleMovement[Meow]
                return AllFloors, SpecFloors, StatuePosition
def Victory():
    print ("After long last, you have defeated the Neko Hooligans! With the final boss' bandana clutched in your hands, you breathe in the sweet smell of victory.\nYou gaze upon the world from atop the Floting Castle; it looks so small.\nYou jump from the balcony off into the clouds, only to land in the comfortable leather seat of your airship.\nThe zoom away casting one last look at the large and enigmatic yet sorrowful figure of the floating castle.\nThe cruel regime of the Hooligans is finally ove...\nOh no!\nThis bandana does not belong to the leader of the brigand! The Blind Swordsman was simply a grunt!\nYour adventure is not yet over as Sanjeeve, the leader of the Hooligans, remains ever elusive.\nIt seems like your journey to hunt him down, adventurer, is not yet over.\n\nThank you for playing!")
    while True:
        input = ""
#main
AllFloors = {"OneRoomOne":0, "OneRoomTwo":0, "OneRoomThree":0, "OneRoomFour":0, "OneRoomFive":0, "OneRoomSix":0, "OneRoomSeven":0, "OneRoomEight":0, "OneRoomNine":0, "TwoRoomOne":0, "TwoRoomTwo":0, "TwoRoomThree":0, "TwoRoomFour":0, "TwoRoomFive":0, "TwoRoomSix":0, "TwoRoomSeven":0, "TwoRoomEight":0, "TwoRoomNine":0, "TwoRoomTen":0, "TwoRoomEleven":0, "ThreeRoomOne":0, "ThreeRoomTwo":0, "ThreeRoomThree":0, "ThreeRoomFour":0, "ThreeRoomFive":0, "ThreeRoomSix":0, "ThreeRoomSeven":0, "ThreeRoomEight":0, "ThreeRoomNine":0, "ThreeRoomTen":0}
SpecFloors = {"OneSpecOne":0, "OneSpecTwo":0, "OneSpecThree":0, "TwoSpecOne":0, "TwoSpecTwo":0, "TwoSpecThree":0, "ThreeSpecOne":0, "ThreeSpecTwo":0, "ThreeSpecThree":0}
MovementDict = {23:"SpawnPoint1", 17:"OneRoomOne", 18:"OneRoomTwo", 19:"OneRoomThree", 12:"OneRoomFour", 13:"OneRoomFive", 14:"OneRoomSix", 7:"OneRoomSeven", 8:"OneRoomEight", 9:"OneRoomNine", 11:"OneSpecOne", 3:"OneSpecTwo", 15:"OneSpecThree", 52:"SpawnPoint2", 51:"TwoRoomTwo", 46:"TwoRoomThree", 41:"TwoRoomFour", 36:"TwoRoomFive", 31:"TwoRoomSix", 32:"TwoRoomSeven", 33:"TwoRoomEight", 34:"TwoRoomNine", 35:"TwoRoomTen", 40:"TwoRoomEleven", 43:"TwoSpecOne", 26:"TwoSpecTwo", 30:"TwoSpecThree", 76:"SpawnPoint3", 77:"ThreeRoomOne", 72:"ThreeRoomTwo", 73:"ThreeRoomThree", 74:"ThreeRoomFour", 79:"ThreeRoomFive", 68:"ThreeRoomSix", 63:"ThreeRoomSeven", 62:"ThreeRoomEight", 64:"ThreeRoomNine", 80:"ThreeSpecOne", 57:"ThreeSpecTwo", 59:"ThreeSpecThree"}
MovementDictDesc = {23:"SpawnPoint1", 17:"OneRoomOne", 18:"OneRoomTwo", 19:"OneRoomThree", 12:"OneRoomFour", 13:"OneRoomFive", 14:"OneRoomSix", 7:"OneRoomSeven", 8:"OneRoomEight", 9:"OneRoomNine", 11:"OneSpecOne", 3:"OneSpecTwo", 15:"OneSpecThree", 52:"SpawnPoint2", 51:"TwoRoomTwo", 46:"TwoRoomThree", 41:"TwoRoomFour", 36:"TwoRoomFive", 31:"TwoRoomSix", 32:"TwoRoomSeven", 33:"TwoRoomEight", 34:"TwoRoomNine", 35:"TwoRoomTen", 40:"TwoRoomEleven", 43:"TwoSpecOne", 26:"TwoSpecTwo", 30:"TwoSpecThree", 76:"SpawnPoint3", 77:"ThreeRoomOne", 72:"ThreeRoomTwo", 73:"ThreeRoomThree", 74:"ThreeRoomFour", 79:"ThreeRoomFive", 68:"ThreeRoomSix", 63:"ThreeRoomSeven", 62:"ThreeRoomEight", 64:"ThreeRoomNine", 80:"ThreeSpecOne", 57:"ThreeSpecTwo", 59:"ThreeSpecThree"}
MapDescDict = {"OneRoomOne":"a", "OneRoomTwo":"a", "OneRoomThree":"a", "OneRoomFour":"a", "OneRoomFive":"a", "OneRoomSix":"a", "OneRoomSeven":"a", "OneRoomEight":"a", "OneRoomNine":"a", "TwoRoomOne":"a", "TwoRoomTwo":"a", "TwoRoomThree":"a", "TwoRoomFive":"a", "TwoRoomSix":"a", "TwoRoomSeven":"a", "TwoRoomNine":"a", "TwoRoomTen":"a", "TwoRoomEleven":"a", "ThreeRoomOne":"a", "ThreeRoomTwo":"a", "ThreeRoomThree":"a", "ThreeRoomFour":"a", "ThreeRoomFive":"a", "ThreeRoomSix":"a", "ThreeRoomSeven":"a", "ThreeRoomEight":"a", "ThreeRoomNine":"a", "ThreeRoomTen":"a", "OneSpecOne":"a", "OneSpecTwo":"a", "OneSpecThree":"a", "SpawnPoint1":"a" , "TwoSpecOne":"a", "TwoSpecTwo":"a", "TwoSpecThree":"a", "SpawnPoint2":"a", "TwoRoomFour":"a", "TwoRoomEight":"a", "ThreeSpecOne":"a", "ThreeSpecTwo":"a", "ThreeSpecThree":"a", "SpawnPoint3":"a"}
FloorOneBoss, FloorTwoBoss, FloorThreeBoss = "Undefeated", "Undefeated", "Undefeated"
Key = [FloorOneBoss, FloorTwoBoss, FloorThreeBoss]
CurrentPosition, Ultimate, GAMEOVER, KeyCount, Proceed, UPPoints, StatuePosition  = 23, -1, 0, 0, 0, 0, 0
Name = input ("Welcome to A_BLT_RPG!\nWhat would you like to call yourself? ")
print ("What class would you like to be placed as?\n\n(1) Berserker - A greatsword wielding fighter who grows stronger the closer to death he becomes.\n(2) Hemomancer - A sorcerer who walks a bloody path. Makes use of powers akin to a vampire\n(3) Weaponmaster - A fighter proficient and lethal with any weapon. A truly agile and powerful fighter.\n(4) Archmage - A wizard renowned through the land for their knowledge of the arcane arts; possesses devastating magical prowess.\n(5) Lone Wolf - A former soldier who travels the world in solitude; well versed in modern firearms.")
while Ultimate == -1:
    Hero = input("--> ")
    Options = ["1", "2", "3", "4", "5"]
    if Hero not in Options:
        print ("Please enter a valid choice.")
    else:
        Hero = int(Hero) - 1
        Ultimate = 0
MapDescDict, AllFloors, SpecFloors = MapSetUp(Monsters, Bosses, MovementDict, MovementDictDesc, MapDescDict, AllFloors, SpecFloors)
Classes[Hero].name = Name
print ("\nYour name is", Classes[Hero].name+".", "You belong to the class,", Classes[Hero].job+".", "\nYou are currently infiltrating the Floating Castle, hideout of the notorious guild, Neko Hooligans, for your own personal reasons.\nThe castle is crawling with monsters and beasts... be careful. In order to unlock the next floor, you must first defeat the current floor's boss.\nThere are also treasures on each floor to aid you on your quest. \nGood luck!")
FirstEquip(Classes, Hero)
Adjust(Classes, Hero)
Classes[Hero].CurrentHP = Classes[Hero].HP #Initial Adjustment
StatsCheck(Classes, Hero)
StatuePosition = StartStatueMoves(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition)
print ("As you step off your airship and onto the Floating Castle, you see a frenzied monk running straight towards you.\nHe screams, 'IT MOVES! IT MOVES!' like a madman as he runs past, without seeing you, into the darkness.\nYou do not reveal yourself nor engage him. As you try to decipher what he had tried to convey, you enter the Castle.\nThe first sight you see is much reminiscent of a scene from an old monastery;\nHundreds of beautifully sculpted statues of deities, the smell of burning incense and a small feeling of foreboding of the unknown.\nWhat is it that moves?\n")
while GAMEOVER == 0:
    t1 = time()
    Choice = input("What would you like to do? (Move, Map, Stats, Equip)\n--> ")
    if "Move" in Choice or "move" in Choice or "MOVE" in Choice:
        t2 = time()
        if Key[0] == "Undefeated":
            ItMoves = t2-t1 #Time determines movement
            if ItMoves < 2.5:
                TimeMove = 0
            elif ItMoves < 8:
                TimeMove = 1
            elif ItMoves < 15:
                TimeMove = 2
            elif ItMoves >= 15:
                TimeMove = 3
            for i in range(TimeMove):
                AllFloors, SpecFloors, StatuePosition = StatueMoves(AllFloors, SpecFloors, MovementDict, Bosses, StatuePosition, MovementDictDesc)
        CurrentPosition, Proceed = Movement(CurrentPosition, Classes, Hero, Proceed)
        if Proceed == 1:
            print (MapDescDict[MovementDictDesc[CurrentPosition]])
            Ultimate, Key, KeyCount, CurrentPosition, UPPoints = BattleScan(CurrentPosition, Ultimate, Classes, Hero, Key, KeyCount, UPPoints, Monsters)
    elif "Map" in Choice or "map" in Choice or "MAP" in Choice:
        print (MapDescDict[MovementDictDesc[CurrentPosition]])
        MapCheck(CurrentPosition, Key)
    elif "Stats" in Choice or "STATS" in Choice or "stats" in Choice:
        StatsCheck(Classes, Hero)
    elif "Equip" in Choice or "EQUIP" in Choice or "equip" in Choice:
        print ("\n"+Classes[Hero].name, "is currently equipped with", "'"+Classes[Hero].TierOneLIST[Classes[Hero].TierOneLevel]+"'", "and", "'"+Classes[Hero].TierTwoLIST[Classes[Hero].TierTwoLevel]+"'")
        UPPoints = Upgrades(Classes, Hero, UPPoints)
        Adjust(Classes, Hero)
    else:
        print ("\nCommand not recognized. Please enter a valid input\n")
