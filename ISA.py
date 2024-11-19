from math import *

"""International Standard Atmosphere (ISA) Model
    Given altitude returns density of air.
"""

def ISA(altitude):

    # ISA DATAS
    g=9.80665
    R=287.0
    T0=288.15
    p0=101325.0
    a=-0.0065

    # Menu

    # h
    if 11e3 < altitude <= 20e3:
        a=0
    if 20e3 < altitude <= 32e3:
        a=0.001
    if 32e3 < altitude <= 47e3:
        a=2.8e-3
    if 47e3 < altitude <= 51e3:
        a=0
    if 51e3 < altitude <= 71e3:
        a=-2.8e-3
    if 71e3 < altitude <= 86e3:
        a=-2e-3
    else:
        a=a

    # T [K]
    if 0 < altitude <= 11e3:
        T0=T0
        T1=T0+a*(altitude - 0)
    if 11e3 < altitude <= 20e3:
        T0=216.65
        T1=T0+a*(altitude - 11e3)
    if 20e3 < altitude <= 32e3:
        T0=216.65
        T1=T0+a*(altitude - 20e3)
    if 32e3 < altitude <= 47e3:
        T0=228.65
        T1=T0+a*(altitude - 32e3)
    if 47e3 < altitude <= 51e3:
        T0=270.65
        T1=T0+a*(altitude - 47e3)
    if 51e3 < altitude <= 71e3:
        T0=270.65
        T1=T0+a*(altitude - 51e3)
    if 71e3 < altitude <= 86e3:
        T0=214.65
        T1=T0+a*(altitude - 71e3)
    elif altitude>86e3:
        T1=184.65
        
    # p [Pa]
    global density
    if 0 < altitude <= 11e3:
        p0=p0
        density = (p0*(T1/T0)**(-g/(a*R)))/(R*T1)
        #-------------------------
    elif 11e3 < altitude <= 20e3:
        p0=22625.791489552423
        density = (p0*exp(-g*(altitude - 11e3)/(R*T1)))/(R*T1)
        #-------------------------
    elif 20e3 < altitude <= 32e3:
        p0=5471.935071950124
        density = (p0*(T1/T0)**(-g/(a*R)))/(R*T1)
        #-------------------------
    elif 32e3 < altitude <= 47e3:
        p0=867.2549941197717
        density = (p0*(T1/T0)**(-g/(a*R)))/(R*T1)
        #-------------------------
    elif 47e3 < altitude <= 51e3:
        p0=110.76657692324365
        density = (p0*exp(-g*(altitude - 47e3)/(R*T1)))/(R*T1)
        #-------------------------
    elif 51e3 < altitude <= 71e3:
        p0= 66.84829644367129
        density = (p0*(T1/T0)**(-g/(a*R)))/(R*T1)
        #-------------------------
    elif 71e3 < altitude <= 86e3:
        p0=3.949000889093089
        density = (p0*(T1/T0)**(-g/(a*R)))/(R*T1)
    elif altitude>86e3:
        p0=0.301619
        density= (p0*exp(-g*(altitude - 86e3)/(R*T1)))/(R*T1)     
                
    return density
