# A simulation script written for St. Petersburg Paradox with
#
# (C) 2021 Ayberk Sadıç, Istanbul, Turkey
# Released under GNU General Public License v3 (GPLv3)
# GitHub: aysadic
# email ayberksadic[]gmail.com

import matplotlib.pyplot as plt
import numpy as np

noHeadToss=8
pot=np.zeros(noHeadToss)
wealth=np.zeros(noHeadToss)
wins=np.zeros(noHeadToss)
pWin=np.zeros(noHeadToss)
for k in range(0,noHeadToss):
    pot[k]=2**(k+1)
    wealth[k]=np.sum(wealth[0:k])+pot[k]
    wins[k]= np.array([2**(t+1) for t in range (0,k+1)]).sum()
    pWin[k]=1/(2**(k+1))

print(pot)
print(wealth)
print(wins)
print(pWin)

w=np.arange(1000)
u=np.log(w)

#plt.figure(figsize=(10,4))
#plt.subplot(1,2,1)
fig, ax1 = plt.subplots()
ax1.set_title('St.Petersburg Game Winnings and Probabilities')
ax1.set_xlabel('Number of Winning Coin Tosses')
ax1.set_ylabel('Winnings [$]')
ax1.plot(range(1,noHeadToss+1),wins,color='blue')
ax1.grid()
ax2 = ax1.twinx()
ax2.set_ylabel('Probability of Win [%]')
ax2.plot(range(1,noHeadToss+1),100*pWin,color='green')
fig.tight_layout()
plt.show()
""" plt.title("St.Petersburg Game Rewards")
plt.xlabel("Number of Winning Coin Tosses")
plt.ylabel("Winnings [$]")
plt.plot(range(noHeadToss),wins,color="blue")
plt.plot(range(noHeadToss),pWin,color="green")
plt.xticks(range(noHeadToss))
plt.grid()
plt.show() """

#plt.subplot(1,2,2)
plt.title("Bernoulli's Logarithmic Utility Function")
plt.xlabel("Wealth")
plt.ylabel("Utility")
plt.plot(w,u,color="red")
plt.yticks([])
plt.xticks([])
""" plt.xscale('log') """
#plt.grid()
plt.show()

