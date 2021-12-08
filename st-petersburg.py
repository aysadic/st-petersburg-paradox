# A simulation script written for St. Petersburg Paradox with
#
# (C) 2021 Ayberk Sadıç, Istanbul, Turkey
# Released under GNU General Public License v3 (GPLv3)
# GitHub: aysadic
# email ayberksadic[]gmail.com

import matplotlib.pyplot as plt
import numpy as np

noToss=8
pot=np.zeros(noToss)
wealth=10*np.ones(noToss)
for k in range(0,noToss):
    pot[k]=2**k
    wealth[k]=wealth[k]**k

utilityBefore=np.log(wealth)    
utilityAfter=np.log(wealth+pot)
price=utilityAfter-utilityBefore

print(pot)
print(wealth)
print(utilityBefore)
print(utilityAfter)

plt.title("St.Petersburg Rewards")
plt.xlabel("Number of Tosses")
plt.ylabel("Pot")
plt.plot(range(noToss),pot,color="red")
plt.grid()
plt.show()

