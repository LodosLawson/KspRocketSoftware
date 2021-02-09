#
#
#
#
import krpc
import RocketProperty
import time
import os

con = krpc.connect()
ave = con.space_center.active_vessel

FUEL = RocketProperty.getfuel()
ORBIT = RocketProperty.getorbit()
ENGINE = RocketProperty.getengine()

FUELINDEX = 0
ORBITINDEX = 0
ENGINEINDEX = 0

os.system("cls")
while True:
    print("-"*25,"FUEL PROPERTY","-"*25)
    for x in FUEL[0]:
        print("""|{}\t{}""".format(x[0],x[1]))
    print("-"*25,"ORBIT ROPERTY","-"*25)
    for x in ORBIT:
        print("""|{}\t{}""".format(x[0],x[1]))
    print("-"*25,"ENGINE PROPERTY","-"*25)
    for x in ENGINE:
        print("""|{}\t{}""".format(x[0],x[1]))

    #time.sleep(1)
    FUEL = RocketProperty.getfuel()
    ORBIT = RocketProperty.getorbit()
    ENGINE = RocketProperty.getengine()
    os.system("cls")
