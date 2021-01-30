import time
import psutil
import os
import numpy as np
import rebound
import reboundx

# initialize constants
T0 = 12388.5e6          # Sun's age ~ 5 Myr pre-TRGB (sim start)
M0 = 0.8868357536545315 # initial mass of star
# init. param. update interval-rel. vars
intervals = np.array([1e-1])
finalas = np.zeros(intervals.size)
max_mems = np.zeros(intervals.size)
runtimes = np.zeros(intervals.size)

def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem # return the memory usage in MB

def makesim():
    sim = rebound.Simulation()
    sim.units = ('yr', 'AU', 'Msun')
    sim.add(m=M0)
    sim.add(m=1e-3, a=5)
    sim.collision = "direct"
    rebx = reboundx.Extras(sim)
    tides = rebx.load_force("tides_constant_time_lag")
    rebx.add_force(tides)
    return sim, rebx, tides

def makesubdir(name):
    if not os.path.exists(name):
        os.makedirs(name)

def writetxt(times, values, path='data.txt'):
    with open(path, 'w') as f: # will overwrite existing file
        for i in range(times.size):
            f.write('%.16E\t%.16E\n' % (times[i], values[i]))

# load MESA data
data = np.loadtxt('../input/m.txt') # return (N, 2) array
mtimes = data[:, 0]                 # return only 1st col
masses = data[:, 1]                 # return only 2nd col
data = np.loadtxt('../input/r.txt')
rtimes = data[:, 0]
Rsuns = data[:, 1]                  # data in Rsun units
data = np.loadtxt('../input/l.txt')
ltimes = data[:, 0]
Lsuns = data[:, 1]                  # data in Lsun units

# conversions and precalculations
radii = np.zeros(Rsuns.size)        # convert Rsun to AU
for i,r in enumerate(Rsuns):
    radii[i] = r * 0.00465047       # 215 Rsun ~ 1 AU
watts = np.zeros(Lsuns.size)        # convert Lsun to W (MKS units)
for i,l in enumerate(Lsuns):
    watts[i] = l * 3.828e26         # IAU Resolution B3 conversion
lumins = np.zeros(watts.size)       # convert W to sim units
for i,w in enumerate(watts):
    lumins[i] = (w *((6.7e-12)**2)*(5e-31))/((3.2e-8)**3)
t_fs = np.zeros(lumins.size)        # precalculate t_f (Eq. 1)
for i,l in enumerate(lumins):
    t_fs[i] = np.cbrt(masses[i]*radii[i]**2/l)
taus = np.zeros(t_fs.size)          # precalc tau (Eq. 2)
G = 4*np.pi**2                      # units of AU, yr, and Msun
for i,t_f in enumerate(t_fs):
    taus[i] = 2.*radii[i]**3/G/masses[i]/t_f

# main loop
for i,interval in enumerate(intervals):
    # initialize sim and create Interpolator objects
    timer_start = time.perf_counter()
    sim, rebx, tides = makesim()
    starmass = reboundx.Interpolator(rebx, mtimes, masses, 'spline')
    starradius = reboundx.Interpolator(rebx, rtimes, radii, 'spline')
    startau = reboundx.Interpolator(rebx, ltimes, taus, 'spline')

    # update Sun's mass and radius accordingly
    ps = sim.particles
    ps[0].m = starmass.interpolate(rebx, t=T0)
    ps[0].r = starradius.interpolate(rebx, t=T0)
    ps[0].params["tctl_k1"] = 0.038 # ~ lambda_2, Schroder & Smith (2008)
    ps[0].params["tctl_tau"] = startau.interpolate(rebx, t=T0)
    ps[0].params["Omega"] = 0 # explicitly set to 0 (would be 0 by default)

    # initialize main sim
    tmax = 5e6                      # max sim integration time
    Nup = int(tmax/interval)        # no. of param updates
    ts = np.linspace(0., tmax, Nup)
    mem_psutil = np.zeros(Nup)      # mem usage tracking
    
    try:
        for j,t in enumerate(ts):
            sim.move_to_com()
            sim.integrate(t)
            ps[0].m = starmass.interpolate(rebx, t=T0+sim.t) # update params
            ps[0].r = starradius.interpolate(rebx, t=T0+sim.t)
            ps[0].params["tctl_tau"] = startau.interpolate(rebx, t=T0+sim.t)          
            mem_psutil[j] = memory_usage_psutil() # record mem usage (MB)
    except rebound.Collision as error:
        finalas[i] = ps[1].a
    finalas[i] = ps[1].a

    # performance
    max_mems[i] = np.amax(mem_psutil)
    timer_stop = time.perf_counter() 
    runtime = timer_stop - timer_start
    runtimes[i] = runtime
    # cout
    h = runtime // 3600
    remainder = runtime - h*3600
    m = remainder // 60
    s = remainder - m*60
    if h != 0:
        print('Wall time: %dh %dmin %ds'%(h, m, s))
    elif m != 0:
        print('Wall time: %dmin %ds'%(m, s))
    else:
        print('Wall time: %ds'%(s))
# fout
makesubdir('output')
writetxt(intervals, max_mems, 'output/maxmems.txt')
writetxt(intervals, runtimes, 'output/runtimes.txt')
writetxt(intervals, finalas, 'output/finalas.txt')
