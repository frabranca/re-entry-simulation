from math import *
import matplotlib.pyplot as plt 
from ISA import ISA
print("***RE-ENTRY SIMULATION***")
print()


#-----------------define constants
S = 2.81        #[m^2] reference area
CD = 1.60       #drag coefficient
G = 6.6741e-11  #[Nm^2/kg^2]
M = 5.972e24    #[kg] Earth mass
R = 6371000     #[m] Earth radius
hft = 325000    #[ft] altitude
vft = 22500     #[ft/s]
jdeg= 1.5       #[deg]
t = 0           #[s] initial time
dt = 0.1        #[s] time step
p1 = 0.301619   #[Pa]
T1 = 184.65     #[K]
g = 9.80665     #[m/s^2] gravity

#-------------------
m = 1207.8257628
h = hft*0.3048
v = vft*0.3048
j = jdeg*pi/180

#-------------
CD_drogue = 1.75
S_drogue = .7
S_main = 107

#-------------
x = 0
vx = abs(v*cos(j))
vy = - abs(v*sin(j))

# plot results
ttab=[]
htab=[]
vtab=[]
xtab=[]
gtab=[]

message32 = False
message11 = False
droguedpl = False
maindpl = False
message9800ft = False
splashdown = False

while h>=0:
    #-----------------formulas (force positive up!!)
    rho1 = ISA(h)
    Fgrav = -(G*M*m)/((R + h)**2)

    if droguedpl and not maindpl:
        Fdrag = CD*0.5*rho1*(v**2)*S + CD_drogue*0.5*rho1*(v**2)*S_drogue
    elif not droguedpl and maindpl:
        Fdrag = CD*0.5*rho1*(v**2)*S + CD_drogue*0.5*rho1*(v**2)*S_main
    else:
        Fdrag = CD*0.5*rho1*(v**2)*S

    Dx = -Fdrag*abs(cos(j))
    Dy = Fdrag*abs(sin(j))
    
    Ftoty = Fgrav + Dy
    Ftotx = Dx
    t = t + dt
    ay = Ftoty/m
    ax = Ftotx/m
    a=sqrt(ax**2 + ay**2)
    vy = vy + ay*dt
    vx = vx + ax*dt
    h = h + vy*dt
    x = x + vx*dt
    v = sqrt(vx**2+vy**2)
    j = abs(atan2(vy,vx))
    #print(round(a/g,2),round(h/0.3048,2),round(t/60,3))
    #-----------------------
    
    
    #----------
    ttab.append(t/60)
    htab.append(h/(1000*0.3048))
    vtab.append(v/0.3048)
    xtab.append(x/(1000*0.3048))
    gtab.append(sqrt(ax**2+ay**2)/g)

    if h <= 32000 and not message32:
        print("\nThe speed at 32 km altitude is:", round(v,2),"m/s")
        print("\nThe flight path angle at 32 km altitude is:", round(j*180/pi,2),"deg")
        message32=True
                
    if h <= 11000 and not message11:
        print("\nThe speed at 11 km altitude is:", round(v,2),"m/s")
        print("\nThe flight path angle at 11 km altitude is:", round(j*180/pi,2),"deg")
        #print(rho1)
        message11 = True
        
    if v <= 186*0.514444 and not droguedpl:
        tdrogue=t
        droguedpl=True
        #print(rho1)
        print("\nThe drogue chute is deployed at", round(h),"m when the speed is:",round(v/0.514444,0),"kts")
    
    if h <= 10000*0.3048 and not maindpl:
        maindpl=True
        tmain=t
        #print(rho1)
        #print(round(v,3))
        print("\nThe time between the chutes depoyments is",round(t-tdrogue,1),"s")
        print("\nThe speed at the main chute deployment is:",round(v/0.3048,2),"ft/s")
        
    if h <= 9800*0.3048 and not message9800ft:
        message9800ft=True
        print("\nThe speed at 9800 ft is",round(v/0.3048,3),"ft/s")
        #print(round(v,3))
        
    if h <= 0 and not splashdown:
        print("\nThe splash down occurs",round((t-tmain)/60,3),"min after the main chute deployment, when the speed is:",round(v/0.3048,4),"ft/s")
        splashdown= True

plt.plot()

plt.subplot(221)
plt.plot(htab,vtab, "r-")
plt.title("Speed vs Altitude")
plt.xlabel("Altitude [kft]")
plt.ylabel("Speed [ft\s]")


plt.subplot(222)
plt.plot(ttab,gtab,"b-")
plt.title("Decelaration vs Time")
plt.xlabel("Time [min]")
plt.ylabel("Deceleration [g's]")

plt.subplot(223)
plt.plot(xtab,htab, "g-")
plt.title("Y vs X")
plt.xlabel("X position [km]")
plt.ylabel("Y position [kft]")


plt.subplot(224)
plt.plot(ttab,htab, "y-")
plt.title("Altitude vs Time")
plt.xlabel("Time [min]")
plt.ylabel("Altitude [kft]")

plt.show()

dummy = input("Please press enter...")
