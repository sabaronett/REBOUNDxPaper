import numpy as np
import os
import psutil
import rebound
import reboundx
import time
from progress.bar import IncrementalBar

# initialize constants
T0 = 1.2264762530663698e10 # Sun's age ~110 Myr pre-TRGB (sim start)

def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem # return the memory usage in MB

def makesim():
    sim = rebound.Simulation()
    sim.integrator = "whfast"
    sim.units = ('yr', 'AU', 'Msun')
    sim.add('Sun')
    sim.add('Jupiter')
    sim.add('Saturn')
    sim.add('Uranus')
    sim.add('Neptune')
    sim.move_to_com()
    sim.dt = 0.5
    sim.status()
    rebx = reboundx.Extras(sim)
    return sim, rebx#, tides

def makesubdir(name):
    if not os.path.exists(name):
        os.makedirs(name)

def writetxt(times, values, path='data.txt'):
    with open(path, 'w') as f:      # will overwrite existing file
        for i in range(times.size):
            f.write('%.16E\t%.16E\n' % (times[i], values[i]))

# load MESA data
data = np.loadtxt('input/eta_0.5/m.txt') # return (N, 2) array
mtimes = data[:, 0]                      # return only 1st col
masses = data[:, 1]                      # return only 2nd col
data = np.loadtxt('input/eta_0.5/r.txt')
rtimes = data[:, 0]
Rsuns = data[:, 1]                       # data in Rsun units

# conversions and precalculations
radii = np.zeros(Rsuns.size)        # convert Rsun to AU
for i,r in enumerate(Rsuns):
    radii[i] = r * 0.00465047       # 215 Rsun ~ 1 AU

# initialize sim and create Interpolator objects
timer_start = time.perf_counter()
sim, rebx = makesim()
sim.ri_whfast.safe_mode = 0  # boost WHFast performance (advanced)
sim.ri_whfast.corrector = 11 # increase WHFast accuracy (advanced)
starmass = reboundx.Interpolator(rebx, mtimes, masses, 'spline')
starradius = reboundx.Interpolator(rebx, rtimes, radii, 'spline')

# update Sun's mass and radius accordingly
ps = sim.particles
ps[0].m = starmass.interpolate(rebx, t=T0)
ps[0].r = starradius.interpolate(rebx, t=T0)

# initialize main sim
tmax = 250e6                    # max sim integration time
Nup = 10000                     # 25 kyr param update interval
ts = np.linspace(0., tmax, Nup)
mass, radius = np.zeros(Nup), np.zeros(Nup)
a = np.zeros((len(ps), Nup))    # record semiaxis vs sim.t
mem_psutil = np.zeros(Nup)      # mem usage tracking

with IncrementalBar('Integrating...', max=Nup, suffix=('%(percent).1f%% '+
                    '[ %(elapsed_td)s / %(eta_td)s ]')) as bar:
    for i,t in enumerate(ts):
        mem_psutil[i] = memory_usage_psutil()
        sim.move_to_com()
        mass[i] = sim.particles[0].m                            # for outputs
        radius[i] = sim.particles[0].r
        for j in range(1, len(ps)):
            a[j,i] = ps[j].a
        ps[0].m = starmass.interpolate(rebx, t=T0+sim.t)             # update params
        ps[0].r = starradius.interpolate(rebx, t=T0+sim.t)
        sim.ri_whfast.recalculate_coordinates_this_timestep = 1 # for mass mod.
        sim.integrator_synchronize()                            # for corrector
        sim.integrate(t)                                        # til next Nup
        bar.next()                                              # update bar

# write semiaxes vs sim.t
makesubdir('output')  # create file output directory
writetxt(ts, mass, 'output/m.txt')
writetxt(ts, radius, 'output/r.txt')
for i in range(1, len(ps)):
    fname = 'output/a_{:d}.txt'.format(i)
    writetxt(ts, a[i,:], path=fname)
# write performance metrics
with open('output/fig6.out.txt', 'w') as f:
    timer_stop = time.perf_counter() 
    runtime = timer_stop - timer_start
    h = runtime // 3600
    remainder = runtime - h*3600
    m = remainder // 60
    s = remainder - m*60
    if h != 0:
        f.write('Wall time: %dh %dmin %ds'%(h, m, s))
    elif m != 0:
        f.write('Wall time: %dmin %ds'%(m, s))
    else:
        f.write('Wall time: %ds'%(s))
    f.write('\nMax. memory used: {:.1f} MB'.format(np.amax(mem_psutil)))
