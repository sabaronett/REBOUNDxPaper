import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

# load data outputs
data = np.loadtxt('output/r.txt')
ts = data[:, 0]/1e6             # return only 1st col
rs = data[:, 1]                 # au
aj0s = sorted(list(Path('output').glob('*au.txt')))
ajs = np.zeros((len(aj0s), ts.size))
for i,aj0 in enumerate(aj0s):
    data = np.loadtxt(aj0)
    ajs[i, :] = data[:, 1]

fig, ax = plt.subplots()
lw = 0.6
ax.fill_between(ts, rs, color='tab:red', label='$R_{Sun}$')
ax.grid()
ax.plot(ts, ajs[-1], lw=lw, color='tab:green', label='$a_{J,esc}}$')
for i,aj0 in enumerate(ajs[:,0]):
    if aj0 <= 1.69:
        ax.plot(ts, ajs[i, :], lw=lw, color='tab:red')
    elif 1.69 < aj0 < 1.71:
        ax.plot(ts, ajs[i, :], lw=lw, color='black', label='$a_{J,min}$')
    elif 1.87 < aj0 < 1.89:
        ax.plot(ts, ajs[i, :], '--', lw=lw, color='black', label='$a_{J,tide}}$')
    else:
        ax.plot(ts, ajs[i, :], lw=lw, color='tab:green')
ax.plot(ts, ajs[0], lw=lw, color='tab:red', label='$a_{J,eng}}$')
ax.legend(loc='best', ncol=2, labelspacing=0.1, framealpha=1.0)
ax.set(xlim=(0, 60), ylim=(0, 3.5))
ax.set_xlabel('Time / Myr', fontsize='large')
ax.set_ylabel('Distance / au', fontsize='large')
ax.xaxis.set_minor_locator(mticker.AutoMinorLocator())
ax.yaxis.set_minor_locator(mticker.AutoMinorLocator())

plt.savefig('../img/fig7.eps', bbox_inches='tight', pad_inches=0.01)
plt.savefig('../img/fig7.pdf', bbox_inches='tight', pad_inches=0.01)
# plt.savefig('../img/fig7.png', bbox_inches='tight', dpi=300)
plt.show()
