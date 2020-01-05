#!/usr/bin/python3

# Library imports:
# {{{
#----------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#----------------------------------------
# }}}

# Load data:
# {{{
#----------------------------------------
data1 = np.genfromtxt('data/negativen_alpha4_new_energy.txt', delimiter=' ', names=['n', 'alpha', 'flux', 'energy', 'radius', 'A0', 'peakB', 'residue'])
data2 = np.genfromtxt('data/negativen_alpha2_new_energy.txt', delimiter=' ', names=['n', 'alpha', 'flux', 'energy', 'radius', 'A0', 'peakB', 'residue'])
data3 = np.genfromtxt('data/negativen_alpha1_new_energy.txt', delimiter=' ', names=['n', 'alpha', 'flux', 'energy', 'radius', 'A0', 'peakB', 'residue'])
#----------------------------------------
# }}}
# Plot for vortex energy w.r.t n rescaled appropriately:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title('Energy Plot ')
plt.plot(abs(data1['n']), (data1['energy'])/(2*abs(data1['n'])), 'h',c='b')
plt.plot(abs(data2['n']), (data2['energy'])/(abs(data2['n'])), 'h',c='r')
plt.plot(abs(data3['n']), (2*data3['energy'])/abs(data3['n']), 'h',c='g')
ax.set_xscale('log')
plt.xlabel('|n|',FontSize=20)
plt.ylabel(r'$\frac{2}{\alpha} \frac{\mathcal{E}(n)}{2 \pi v^2 |n|}$',FontSize=20)
ax.legend((r'$\alpha =4$',r'$\alpha =2$', r'$\alpha =1$'))
plt.tight_layout()
plt.savefig('python-plots/negative_n_energy_alpha_1_2_4.png')
plt.clf()
#----------------------------------------
# }}}


# Plot for vortex energy w.r.t n rescaled appropriately:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title('Energy Plot ')
plt.plot(abs(data1['n']), (data1['energy'])/(data1['energy'][0]*abs(data1['n'])), 'h',c='b')
plt.plot(abs(data2['n']), (data2['energy'])/(data2['energy'][0]*abs(data2['n'])), 'h',c='r')
plt.plot(abs(data3['n']), (data3['energy'])/(data3['energy'][0]*abs(data3['n'])), 'h',c='g')
ax.set_xscale('log')
plt.xlabel('|n|',FontSize=20)
plt.ylabel(r'$\frac{\mathcal{E}(n)}{\mathcal{E}(1)|n|}$',FontSize=20)
ax.legend((r'$\alpha =4$',r'$\alpha =2$', r'$\alpha =1$'))
plt.tight_layout()
plt.savefig('python-plots/negative_n_energy_alpha_1_2_4_normalizedbyE1.png')
plt.clf()
#----------------------------------------
# }}}





# Plot for A_0 w.r.t n for different values of n:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title('Energy Plot ')
plt.plot(abs(data1['n']), (data1['A0'])-1, 'h',c='b')
plt.plot(abs(data2['n']), (data2['A0'])-1, 'h',c='r')
plt.plot(abs(data3['n']), (data3['A0'])-1, 'h',c='g')
ax.set_xscale('log')
plt.xlabel('|n|',FontSize=20)
plt.ylabel(r'$A_0(0)$',FontSize=20)
ax.legend((r'$\alpha =4$',r'$\alpha =2$', r'$\alpha =1$'))
plt.tight_layout()
plt.savefig('python-plots/negative_n_A0_alpha_1_2_4.png')
plt.clf()
#----------------------------------------
# }}}
