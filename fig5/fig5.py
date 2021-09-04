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

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
fig, ax1 = plt.subplots(figsize=(13, 8), dpi=300)
cmap = plt.get_cmap("tab10")

ax1.set_xlabel('Time / Myr', fontsize='large')
ax1.set_ylabel('Distance / au', fontsize='large')
ax1.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
ax1.xaxis.set_minor_locator(mticker.AutoMinorLocator())
ax1.yaxis.set_minor_locator(mticker.AutoMinorLocator())
ax1.plot(ts,radius, color='black', lw=4, label='$R_{Sun}(t)$',)
# Single points for grayscale legend
ax1.plot(ts[0],a1[0, 0], '--', color='tab:gray', lw=1, label='Tides OFF')
ax1.plot(ts[0],aT1[0, 0], color='tab:gray', lw=1,
         label='1 $M_\oplus$, Tides ON')
ax1.plot(ts[0],aT10[0, 0], color='tab:gray', lw=2,
         label='10 $M_\oplus$, Tides ON')
ax1.plot(ts[0],aT100[0, 0], color='tab:gray', lw=3,
         label='100 $M_\oplus$, Tides ON')
# Planet semimajor axes plots
for i,init_a in enumerate(init_as):
    ax1.plot(ts,a1[:, i], '--', color=cmap(i), lw=1)
    ax1.plot(ts,aT1[:, i], color=cmap(i), lw=1)
    ax1.plot(ts,aT10[:, i], color=cmap(i), lw=2)
    ax1.plot(ts,aT100[:, i], color=cmap(i), lw=3)
ax1.legend(fontsize='x-large', loc='best', labelspacing=0.1, framealpha=1.0)
ax1.grid()

plt.savefig('../img/fig5.eps', bbox_inches='tight', pad_inches=0.01)
plt.savefig('../img/fig5.pdf', bbox_inches='tight', pad_inches=0.01)
