class statsEquation():
    #naturevalue = 0
    
    #Calculation of HP
    def hpcal(base, IV, EV, level):
        hp = (((2 * base + IV +(EV/4)*level)/100)+ level)+ 10
        return hp

    #Calculation of Attack Stat
    def attackcal(base, IV, EV, level, snature):
        naturevalue = 0
        if snature == 1 or snature == 2 or snature == 3 or snature == 4:
            naturevalue = 1.1
        elif snature == 5 or snature == 10 or snature == 15 or snature == 20:
            naturevalue = 0.9
        else:
            naturevalue = 1.0
        attack = ((((2 * base + IV +(EV/4))*level)/100)+5)*naturevalue
        return attack


    #Calculation of Defense Stat
    def defensecal(base, IV, EV, level, snature):
        naturevalue = 0
        if snature == 5 or snature == 7 or snature == 8 or snature == 9:
            naturevalue = 1.1
        elif snature == 1 or snature == 11 or snature == 16 or snature == 21:
            naturevalue = 0.9
        else:
            naturevalue = 1.0
        defense = ((((2 * base + IV +(EV/4))*level)/100)+5)*naturevalue
        return defense


    #Calculation of Sp.Attack Stat
    def atkspeedcal(base, IV, EV, level, snature):
        naturevalue = 0
        if snature == 15 or snature == 16 or snature == 17 or snature == 19:
            naturevalue = 1.1
        elif snature == 3 or snature == 8 or snature == 13 or snature == 23:
            naturevalue = 0.9
        else:
            naturevalue = 1.0
        atkspeed = ((((2 * base + IV +(EV/4))*level)/100)+5)*naturevalue
        return atkspeed


    #Calculation of Sp.Defense Stat
    def defspeedcal(base, IV, EV, level, snature):
        naturevalue = 0
        if snature == 20 or snature == 21 or snature == 22 or snature == 23:
            naturevalue = 1.1
        elif snature == 4 or snature == 9 or snature == 14 or snature == 19:
            naturevalue = 0.9
        else:
            naturevalue = 1.0
        defspeed = ((((2 * base + IV +(EV/4))*level)/100)+5)*naturevalue
        return defspeed


    #Calculation of Speed Stat
    def speedcal(base, IV, EV, level, snature):
        naturevalue = 0
        if snature == 10 or snature == 11 or snature == 13 or snature == 14:
            naturevalue = 1.1
        elif snature == 2 or snature == 7 or snature == 17 or snature == 22:
            naturevalue = 0.9
        else:
            naturevalue = 1.0
        speed = ((((2 * base + IV +(EV/4))*level)/100)+5)*naturevalue
        return speed
    
        
    
