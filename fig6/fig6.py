import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# load REBOUND data
data = np.loadtxt('output/tides/m.txt')  # return (N, 2) array
ts = data[:, 0]/1e6                      # return only 1st col
mass = data[:, 1]                        # return only 2nd col
data = np.loadtxt('output/tides/r.txt')
radius = data[:, 1]                # data in AU
names = [r'$a_J$', r'$a_S$', r'$a_U$', r'$a_N$']
namest = [r'$a_{J,tides}$',r'$a_{S,tides}$',r'$a_{U,tides}$',r'$a_{N,tides}$']
# colors = ['tab:orange', 'tab:red', 'tab:green', 'tab:blue']
colorst = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
a, at = np.zeros([4, ts.size]), np.zeros([4, ts.size])
for i in range(4):
    fname = 'output/a_{:d}.txt'.format(i+1)
    data = np.loadtxt(fname)
    a[i, :] = data[:, 1]
    fname = 'output/tides/a_{:d}.txt'.format(i+1)
    data = np.loadtxt(fname)
    at[i, :] = data[:, 1]

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(6, 5),
                               gridspec_kw={'height_ratios': [1, 3]})
fig.subplots_adjust(hspace=0)

ax1.set_ylabel("$M_{Sun}(t)$ / $M_{\odot}$", fontsize='large')
ax1.yaxis.set_minor_locator(mticker.AutoMinorLocator())
ax1.plot(ts, mass, color='black', label=r'$\eta=0.5$')
ax1.grid()
ax1.legend(fontsize='medium', loc='best', labelspacing=0.1, framealpha=1.0)

ax2.set_xlabel('Time / Myr', fontsize='large')
ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
ax2.set_ylabel('Distance / au', fontsize='large')
ax2.set_yscale('log')
ax2.set_ylim(1e-2, 1e2)
# Planet semimajor axes plots
for i in range(3, -1, -1):
    ax2.plot(ts, a[i, :], color=colorst[i], label=names[i])
    if i == 0:
        ax2.plot(ts, at[i, :], ':', color='black', label=namest[i])
ax2.plot(ts,radius, color='black', label='$R_{Sun}(t)$',)
ax2.legend(fontsize='medium', loc=(.0455, .251), labelspacing=0.1, framealpha=1.0)
ax2.grid()

plt.savefig('../img/fig6.eps', bbox_inches='tight', pad_inches=0.01)
plt.savefig('../img/fig6.pdf', bbox_inches='tight', pad_inches=0.01)
# plt.savefig('../img/fig6.png', bbox_inches='tight', dpi=300)
plt.show()
