import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# load REBOUND data
data = np.loadtxt('tides_on/1Mearth/output/m.txt')  # return (N, 2) array
ts = data[:, 0]/1e6                                 # return only 1st col
mass = data[:, 1]                                   # return only 2nd col
data = np.loadtxt('tides_on/1Mearth/output/r.txt')
radius = data[:, 1]                                 # data in AU
init_as = np.arange(0.4, 1.51, 0.2)                 # in AU
aT1 = np.zeros([ts.size, init_as.size])
aT10 = np.zeros([ts.size, init_as.size])
aT100 = np.zeros([ts.size, init_as.size])
a1 = np.zeros([ts.size, init_as.size])
for i,init_a in enumerate(init_as):
    fname = 'tides_on/1Mearth/output/{:.1f}au.txt'.format(init_a)
    data = np.loadtxt(fname)
    aT1[:, i] = data[:, 1]
    fname = 'tides_on/10Mearth/output/{:.1f}au.txt'.format(init_a)
    data = np.loadtxt(fname)
    aT10[:, i] = data[:, 1]
    fname = 'tides_on/100Mearth/output/{:.1f}au.txt'.format(init_a)
    data = np.loadtxt(fname)
    aT100[:, i] = data[:, 1]
    fname = 'tides_off/1Mearth/output/{:.1f}au.txt'.format(init_a)
    data = np.loadtxt(fname)
    a1[:, i] = data[:, 1]

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
fig, ax1 = plt.subplots(figsize=(13, 8), dpi=300)
cmap = plt.get_cmap("tab10")

ax1.set_xlabel('Time / Myr', fontsize='large')
ax1.set_ylabel('Distance / AU', fontsize='large')
ax1.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
ax1.xaxis.set_minor_locator(mticker.AutoMinorLocator())
ax1.yaxis.set_minor_locator(mticker.AutoMinorLocator())
ax1.plot(ts,radius, color='black', lw=3, label='$R_\odot(t)$',)
for i,init_a in enumerate(init_as):
    if i == 0:
        ax1.plot(ts,a1[:, i], '--', color=cmap(i), lw=1,
                 label='Tides OFF')
    else:
        ax1.plot(ts,a1[:, i], '--', color=cmap(i), lw=1)
for i,init_a in enumerate(init_as):
    if i == 0:
        ax1.plot(ts,aT1[:, i], color=cmap(i), lw=1,
                 label='1 $M_\oplus$, Tides ON')
        ax1.plot(ts,aT10[:, i], color=cmap(i), lw=1.5,
                 label='10 $M_\oplus$, Tides ON')
        ax1.plot(ts,aT100[:, i], color=cmap(i), lw=2,
                 label='100 $M_\oplus$, Tides ON')
    else:
        ax1.plot(ts,aT1[:, i], color=cmap(i), lw=1)
        ax1.plot(ts,aT10[:, i], color=cmap(i), lw=1.5)
        ax1.plot(ts,aT100[:, i], color=cmap(i), lw=2)
ax1.legend(fontsize='x-large', loc='best', labelspacing=0.1, framealpha=1.0)
ax1.grid()

plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))
# plt.savefig('../img/fig5.eps', bbox_inches='tight', pad_inches=0.01)
# plt.savefig('../img/fig5.pdf', bbox_inches='tight', pad_inches=0.01)
plt.savefig('../img/fig5.png', bbox_inches='tight', dpi=300)
# plt.show()
