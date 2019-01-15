from brian2 import *
%matplotlib inline


start_scope()

# Params.
tau=10ms  #

Cm = (2*10**-8) farad  # Capacitance of membrane
# dt=tau ?
g_K = (60*10**-5) siemens
g_l = (0.1 * e**-5) siemens  # electrical (linear) conductance of leak channel
eqs='''
I = Cm * (dVm/dt) + g_K * (Vm - VK) + g_l * (Vm - Vl)

'''