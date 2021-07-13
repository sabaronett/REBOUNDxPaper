import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# load memory output data
data = np.loadtxt('engulftimes.txt') # return (N, 2) array
interval = data[:, 0]                # return only 1st col
engulftimes = data[:, 1]/1e6         # return only 2nd col
data = np.loadtxt('eng_runtimes.txt')
eng_runtimes = data[:, 1]/60
data = np.loadtxt('finalas.txt')
finalas = data[:, 1]
data = np.loadtxt('exp_runtimes.txt')
exp_runtimes = data[:, 1]/60

# compute fractional errors against most accurate estimate
engulfFEs = np.abs(engulftimes - engulftimes[0])/engulftimes[0]
finalaFEs = np.abs(finalas - finalas[0])/finalas[0]

# Init subplot
fig, (ax1, ax3) = plt.subplots(nrows=2, ncols=1, sharex=True,
                               gridspec_kw={'height_ratios': [1, 1]},
                               figsize=(6, 5))
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
c1, c2 = 'tab:blue', 'tab:orange'    # def colors for plots/labels

# Top Plot: Engulfment Times
ax2 = ax1.twinx() # instantiate a second axes that shares the same x-axis

# left y-axis
ax1.set_ylabel('$\delta t_{eng}$', color=c1, fontsize='large')
ax1.tick_params(axis='y', labelcolor=c1)
ax1.yaxis.set_minor_locator(mticker.AutoMinorLocator())
ax1.loglog(interval, engulfFEs, marker='o', color=c1,
    label='$\delta t_{eng},\,\delta a_{f}$')
# right y-axis
ax2.set_ylabel('Runtime / min', color=c2, fontsize='large')
ax2.tick_params(axis='y', labelcolor=c2)
ax2.yaxis.set_minor_locator(mticker.AutoMinorLocator())
ax2.semilogx(interval, eng_runtimes, marker='^', markersize=4, color=c2,
    label='Runtime')
ax1.grid()

# Bottom Plot: Final Semiaxis
# x-axis
ax3.set_xlabel('Parameter Update Interval / yr', fontsize='large')
# left y-axis
ax3.set_ylabel('$\delta a_{f}$', color=c1, fontsize='large')
ax3.tick_params(axis='y', labelcolor=c1)
ax3.yaxis.set_minor_locator(mticker.AutoMinorLocator())
ax3.loglog(interval, finalaFEs, marker='o', color=c1)
# right y-axis
ax4 = ax3.twinx() # instantiate a second axes that shares the same x-axis
ax4.set_xlim(2.3e6, 4.5e-2)
ax4.set_ylabel('Runtime / min', color=c2, fontsize='large')
ax4.tick_params(axis='y', labelcolor=c2)
ax4.yaxis.set_minor_locator(mticker.AutoMinorLocator())
ax4.loglog(interval, exp_runtimes, marker='^', markersize=4, color=c2)
ax3.grid()

# FINAL DISPLAY
fig.legend(fontsize='medium', loc='upper center', labelspacing=0.1,
    framealpha=1.0, bbox_to_anchor=(.5, .94))
fig.tight_layout()
fig.subplots_adjust(hspace=0)
# plt.show()
plt.savefig('../img/fig4.eps', bbox_inches='tight', pad_inches=0.01)
plt.savefig('../img/fig4.pdf', bbox_inches='tight', pad_inches=0.01)
# plt.savefig('fig4.png', bbox_inches='tight', dpi=300)
