# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:51:15 2018

@author: oyata
"""
import matplotlib.pyplot as plt
import numpy as np

dt = 1
Xs = 0
Ys = 0
Zs = -5000
Vs = 180
Hs = 5000

gammas = 0
phais = 0
Us = 180

ro = 0.736
a = 0.0513
T = 20800

CLa = 4.3
CD0 = 0.0548
K = 3.02
w = 2*3.14/40
m = 7500
g = 9.8
S = 27.9

Xlist = []
Ylist = []
Zlist = []
Vlist = []
Hlist = []
gammalist = []
phailist = []

Xb = Xs
Yb = Ys
Zb = Zs

Vb = Vs

gammab = gammas
phaib = phais
Ub = Us

for i in range(20):
    D = 0.5 * ro * Ub*Ub * S * (CD0 + K*a**2)
    L = 0.5 * ro * Ub*Ub * S * (CLa * a)
    phaidt = 0
    Udt = 0
    gammadt = 0
    
    phai = phaib + phaidt
    U = Ub + Udt
    gamma = gammab + gammadt
    
    Vlist.append(U)
    
    Xdt = Ub*np.cos(gammab)*np.cos(phaib)
    Ydt = Ub*np.cos(gammab)*np.sin(phaib)
    Zdt = -Ub*np.sin(gammab)
    
    X = Xb + Xdt
    Y = Yb + Ydt
    Z = Zb + Zdt
    
    Xlist.append(X)
    Ylist.append(Y)
    Zlist.append(Z)
    Hlist.append(-Z)
    gammalist.append(gamma)
    
    Xb = X
    Yb = Y
    Zb = Z
    
    phaib = phai
    gammab = gamma
    Ub = U
 
pusaib = 0;    
    
for i in range(40):
    D = 0.5 * ro * Ub*Ub * S * (CD0 + K*a**2)
    L = 0.5 * ro * Ub*Ub * S * (CLa * a)
    Udt = -D/m + T/m - g*np.sin(gammab)
    gammadt = (L*np.cos(phaib)/m + T*np.cos(phaib)*np.sin(a)/m  - g*np.cos(gammab))/Ub
    pusaidt = (L/m + T*np.sin(a)/m)*(np.sin(phaib)/np.cos(gammab))/Ub 
    
    phai = (3.14/6)*np.sin(w*i)
    
    U = Ub + Udt
    gamma = gammab + gammadt
    pusai = pusaib + pusaidt
    Vlist.append(U)
    
    Xdt = Ub*np.cos(gammab)*np.cos(pusai)
    Ydt = Ub*np.cos(gammab)*np.sin(pusai)
    Zdt = -Ub*np.sin(gammab)
    
    X = Xb + Xdt
    Y = Yb + Ydt
    Z = Zb + Zdt
    
    Xlist.append(X)
    Ylist.append(Y)
    Zlist.append(Z)
    Hlist.append(-Z)
    
    Xb = X
    Yb = Y
    Zb = Z
    
    Ub = U
    phaib = phai
    gammab = gamma
    pusaib = pusai

for i in range(20):
    D = 0.5 * ro * Ub*Ub * S * (CD0 + K*a**2)
    L = 0.5 * ro * Ub*Ub * S * (CLa * a)
    Udt = -D/m + T/m - g*np.sin(gammab)
    gammadt = (L*np.cos(phaib)/m + T*np.cos(phaib)*np.sin(a)/m  - g*np.cos(gammab))/Ub
    pusaidt = (L/m + T*np.sin(a)/m)*(np.sin(phaib)/np.cos(gammab))/Ub 
    
    phai = 0
    U = Ub + Udt
    gamma = gammab + gammadt
    pusai = pusaib + pusaidt
    
    Vlist.append(U)
    
    Xdt = Ub*np.cos(gammab)*np.cos(phaib)
    Ydt = Ub*np.cos(gammab)*np.sin(phaib)
    Zdt = -Ub*np.sin(gammab)
    
    X = Xb + Xdt
    Y = Yb + Ydt
    Z = Zb + Zdt
    
    Xlist.append(X)
    Ylist.append(Y)
    Zlist.append(Z)
    Hlist.append(-Z)
    
    Xb = X
    Yb = Y
    Zb = Z
    
    Ub = U
    phaib = phai
    gammab = gamma
    pusaib = pusai

t = np.linspace(0,80,80)
plt.plot(t,Hlist)

plt.savefig("Hlist.png")
plt.show()
plt.plot(t,Vlist)
plt.savefig("Vlist.png")
plt.show()

plt.plot(t,Xlist)
plt.savefig("Xlist.png")
plt.show()
plt.plot(t,Ylist)
plt.savefig("Ylist.png")
plt.show()
plt.plot(t,Zlist)
plt.savefig("Zlist.png")
