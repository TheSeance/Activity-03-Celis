import statsEquation as stats
import EVequation as EV
import math


#object = module.statsEquation()

def StatCalculator():
    hpbase = int(input("Base HP stat: "))
    hplevel = int(input("Target Level of Pokemon: "))
    hpIV = int(input("Individual Value (0-31): "))
    if hpIV > 31:
        print("Please select a value from 0-31 only")
        
    hpEV = int(input("Effort Value (0-255): "))
    if hpEV > 255:
        print("Please select a value from 0-255 only")
        StatCalculator()
    pnature = """
            0 - Hardy     5 - Bold     10 - Timid     15 - Modest     20 - Calm
            1 - Lonely    6 - Docile   11 - Hasty     16 - Mild       21 - Gentle
            2 - Brave     7 - Relaxed  12 - Serious   17 - Quiet      22 - Sassy
            3 - Adamant   8 - Impish   13 - Jolly     18 - Bashful    23 - Careful
            4 - Naughty   9 - Lax      14 - Naive     19 - Rash       24 - Quirky """
    print(pnature)
    snature = int(input("Pokemon Nature: "))
    if snature > 24:
        print("Please select from 0 - 24 (as given above)")
        StatCalculator()

    hpstat = stats.statsEquation.hpcal(hpbase, hpIV, hpEV, hplevel)
    attackstat = stats.statsEquation.attackcal(hpbase, hpIV, hpEV, hplevel, snature)
    defensestat = stats.statsEquation.defensecal(hpbase, hpIV, hpEV, hplevel, snature)
    atkspeedstat = stats.statsEquation.atkspeedcal(hpbase, hpIV, hpEV, hplevel, snature)
    defspeedstat = stats.statsEquation.defspeedcal(hpbase, hpIV, hpEV, hplevel, snature)
    speedstat = stats.statsEquation.speedcal(hpbase, hpIV, hpEV, hplevel, snature)

    print("HP stat: ", round(hpstat,2))
    print("Attack: ", round(attackstat,2))
    print("Defense: ", round(defensestat,2))
    print("Sp.Attack: ", round(atkspeedstat,2))
    print("Sp.Defense: ", round(defspeedstat,2))
    print("Speed: ", round(speedstat,2))



def EVcalculator():
    #Hingi ng mga needed values
    slevel = int(input("Target Level of the Pokemon: "))
    sbase = int(input("Base value of Stat: "))
    sIV = int(input("Individual Value (0-31): "))
    if sIV > 31:
        print("Please select a value from 0-31 only")
        EVcalculator()
    sEV = int(input("Effort Value (0-255): "))
    if sEV > 255:
        print("Please select a value from 0-255 only")
        EVcalculator()
    pnature = """
            0 - Hardy     5 - Bold     10 - Timid     15 - Modest     20 - Calm
            1 - Lonely    6 - Docile   11 - Hasty     16 - Mild       21 - Gentle
            2 - Brave     7 - Relaxed  12 - Serious   17 - Quiet      22 - Sassy
            3 - Adamant   8 - Impish   13 - Jolly     18 - Bashful    23 - Careful
            4 - Naughty   9 - Lax      14 - Naive     19 - Rash       24 - Quirky """
    print(pnature)
    snature = int(input("Pokemon Nature: "))
    if snature > 24:
        print("Please select from 0 - 24 (as given above)")
        EVcalculator()

    #Compute
    sattackstat = stats.statsEquation.attackcal(sbase, sIV, sEV, slevel, snature)
    sdefensestat = stats.statsEquation.defensecal(sbase, sIV, sEV, slevel, snature)
    satkspeedstat = stats.statsEquation.atkspeedcal(sbase, sIV, sEV, slevel, snature)
    sdefspeedstat = stats.statsEquation.defspeedcal(sbase, sIV, sEV, slevel, snature)
    sspeedstat = stats.statsEquation.speedcal(sbase, sIV, sEV, slevel, snature)

    evattack = EV.EVequation.evatk(sattackstat,sbase, sIV, sEV, slevel, snature)
    evdefense = EV.EVequation.evdef(sdefensestat,sbase, sIV, sEV, slevel, snature)
    evspattack = EV.EVequation.evspatk(satkspeedstat,sbase, sIV, sEV, slevel, snature)
    evspdefense = EV.EVequation.evspdef(sdefspeedstat,sbase, sIV, sEV, slevel, snature)
    evspeed = EV.EVequation.evspeed(sspeedstat,sbase, sIV, sEV, slevel, snature)


    #Ask user   
    choice = int (input("1 - Single Stat or 2 - All Stats"))
    if choice > 2:
            print("Please select from 1 and 2 only")
            EVcalculator()
        
    elif choice == 1:
        print("1 - Attack \n2 - Defense \n3 - Sp.Attack \n4 - Sp.Defense \n5 - Speed")
        choice1 = int(input("Please select from 1-5: "))
        if choice1 > 5:
            print("please select from 1-5 only")
            EVcalculator()
        elif choice1 == 1:
            print("Attack : " , round(evattack,2))
        elif choice1 == 2:
            print("Defense : " , round(evdefense,2))
        elif choice1 == 3:
            print("Sp.Attack : " , round(evspattack,2))
        elif choice1 == 4:
            print("Sp.Defense : " , round(evspdefense,2))
        elif choice1 == 5:
            print("Speed : " , round(evspeed,2))
            

    elif choice == 2:
        print("Attack : " , round(evattack,2))
        print("Defense : " , round(evdefense,2))
        print("Sp.Attack : " , round(evspattack,2))
        print("Sp.Defense : " , round(evspdefense,2))
        print("Speed : " , round(evspeed,2))

def Menu():
    print("Pokemon HP/Other stat and EV Calculator")
    print("1 - HP/Other stat Calculator \n2 - EV Calculator")
    userinput = int(input(" Select from 1 and 2: "))
    if userinput == 1:
        StatCalculator()
    elif userinput == 2:
        EVcalculator()
    else:
        print("Please select from 1 and 2 only")
        Menu()

Menu()
user1=input("Do you want the program to run again? y/n")
if user1 == "Y" or "y":
    Menu()
else:
    print("Thank you! Have a great day")
    exit()

        
