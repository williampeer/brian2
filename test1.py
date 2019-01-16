from brian2 import *
%matplotlib inline

start_scope()

# Params.
C_m = (2*10**-8)*farad  # Capacitance of membrane
g_K = (60*10**-5)*siemens  # conductance of sodium channel
g_l = (0.1 * e**-5)*siemens  # electrical (linear) conductance of leak channel
V_l = -65*mV  # leak voltage
V_K = -90*mV  # sodium leak voltage
n = 0  # initially, no gates open?
eqs='''
alpha_n = 0.01 * (10 - (V_m/mV)) / (exp((10 - (V_m/mV))/(10)) - 1) : 1
beta_n = 0.125 * exp(-V_m/(80*mV)) : 1
dn/dt = (alpha_n * (1 - n) - beta_n * n)/ms : 1
dV_m/dt = (I_K - g_K * (V_m - V_K) - g_l * (V_m - V_l))/C_m : volt
I_K : amp
'''
# I_K = g_K * n * (V_m ** 4) * (V_m - V_K) : amp
# I = Cm * (dVm/dt) + g_K * (Vm - VK) + g_l * (Vm - Vl)

group = NeuronGroup(1, eqs,
                    threshold='V_m > -40*mV',
                    refractory='V_m > -40*mV',
                    method='exponential_euler')

group.V_m = V_K
statemon = StateMonitor(group, 'V_m', record=True)
spikemon = SpikeMonitor(group, variables='V_m')
figure(figsize=(9, 4))
for l in range(5):
    group.I_K = rand()*50*nA
    run(10*ms)
    axvline(l*10, ls='--', c='k')
axhline(V_l/mV, ls='-', c='lightgray', lw=3)
plot(statemon.t/ms, statemon.V_m[0]/mV, '-b')
plot(spikemon.t/ms, spikemon.V_m/mV, 'ob')
xlabel('Time (ms)')
ylabel('V_m (mV)');