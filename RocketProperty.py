#
#
#
#

import krpc

con = krpc.connect()
ave = con.space_center.active_vessel

def getfuel():
    #print("All Fuel:")
    return [[[x.name, x.amount] for x in ave.resources.all],
            [z.name for z in ave.resources.all],
            [z.amount for z in ave.resources.all]]

def getorbit():
    #print("All Orbit Property")
    ReOrbit = []
    x = [x  if x[0] != '_' else '' for x in dir(ave.orbit)]
    a = []
    [[exec("a.append(ave.orbit."+y+")",{'a':a, 'ave':ave}) if y != '' else '' for y in [x if x[0] != '_' else '' for x in dir(ave.orbit)]]]
    count = len(x)-len(a)
    for i in a:
     count += 1   
     try:
        if str(type(float(i))) == "<class 'float'>":
            ReOrbit.append([x[count],i])
     except TypeError:
        pass
    return ReOrbit

def getengine():
    problem = ['auto_mode_switch','gimbal_limit','gimbal_locked','mode','modes']
    engine_property = []
    a = []
    b = []
    index = 0
    for x in ave.parts.engines:
        for y in dir(x):
            if y[0] != '_':
                flag = False
                for z in problem:
                    if y == z:
                        flag = True                  
                if flag != True:
                    exec('a.append([y,ave.parts.engines[index].'+y+'])',{'a':a,'ave':ave,'index':index,'y':y})
                                            
        index += 1
    for x in a:
        if str(type(x[1])) == "<class 'bool'>":
            b.append(x)
        if str(type(x[1])) == "<class 'float'>":
            b.append(x)
    return b

def activ():
    ave.control.activate_next_stage()

def onoff(size):
    ave.control.throttle = size

def aopil():
    ave.auto_pilot.engage()

def pos(x,y):
    ave.auto_pilot.target_pitch_and_heading(x,y)

