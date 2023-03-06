import matplotlib.pyplot as plt

fig, axs = plt.subplots(2,2)

weekdays = ['H', 'K', 'Sz', 'Cs', 'P']

# Hallgatok
axs[0][0].plot(weekdays, [6,5,2,1,1], label="Erik", marker='o', linewidth = 7, color='#ff00ff')
axs[0][0].plot(weekdays, [4,3,2,2,1], label="Balazs", marker='v', linestyle = '--')
axs[0][0].plot(weekdays, [4,3,0,2,1], label="Gergo", marker='d', linestyle='')
axs[0][0].set_title('Hallgatok oraterhelese')
axs[0][0].set_ylabel('Oraszam (db)')
axs[0][0].set_ybound(1,4)


# Mate
axs[0][0].legend()
axs[0][1].bar(weekdays,[7,4,0,2,0])
axs[0][1].set_title('Mate oraterhelese')

# ???
axs[1][0].scatter([0,10,50],[0,20,-10],[10,140,50],color=['red','blue','red'])


plt.show()