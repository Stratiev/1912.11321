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
data_n_1_param1 = np.genfromtxt('data/solutions/dimensionless_solution_n-1_alpha1.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_1_param2 = np.genfromtxt('data/solutions/dimensionless_solution_n-1_alpha2.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_1_param3 = np.genfromtxt('data/solutions/dimensionless_solution_n-1_alpha3.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_1_param4 = np.genfromtxt('data/solutions/dimensionless_solution_n-1_alpha4.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_1_param5 = np.genfromtxt('data/solutions/dimensionless_solution_n-1_alpha5.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_2_param1 = np.genfromtxt('data/solutions/dimensionless_solution_n-2_alpha1.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_3_param1 = np.genfromtxt('data/solutions/dimensionless_solution_n-3_alpha1.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_4_param1 = np.genfromtxt('data/solutions/dimensionless_solution_n-4_alpha1.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_5_param1 = np.genfromtxt('data/solutions/dimensionless_solution_n-5_alpha1.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_p1_param1 = np.genfromtxt('data/solutions/dimensionless_solution_n1_alpha1.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_p2_param1 = np.genfromtxt('data/solutions/dimensionless_solution_n2_alpha1.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_p3_param1 = np.genfromtxt('data/solutions/dimensionless_solution_n3_alpha1.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_p4_param1 = np.genfromtxt('data/solutions/dimensionless_solution_n4_alpha1.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
data_n_p5_param1 = np.genfromtxt('data/solutions/dimensionless_solution_n5_alpha1.csv', delimiter=',', names=['x', 'B', 'f', 'A0', 'Atheta','A0`', 'energy'])
#----------------------------------------
# }}}


# Compare profiles for n=1 relative to coupling strength:
# {{{
#----------------------------------------
# Plot f:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title('Scalar Field Profiles for n=-1', FontSize=25)
plt.plot(data_n_1_param1['x'], data_n_1_param1['f'], '-',LineWidth=1.6,c='b')
plt.plot(data_n_1_param2['x'], data_n_1_param2['f'], '-',LineWidth=1.6,c='r')
plt.plot(data_n_1_param3['x'], data_n_1_param3['f'], '-',LineWidth=1.6,c='g')
plt.plot(data_n_1_param4['x'], data_n_1_param4['f'], '-',LineWidth=1.6,c='m')
plt.plot(data_n_1_param5['x'], data_n_1_param5['f'], '-',LineWidth=1.6,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\hat{f}(\hat{r})$',FontSize=20)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0,right=30)
ax.legend((r'$\alpha =1$', r'$\alpha =2$',r'$\alpha =3$',r'$\alpha =4$',r'$\alpha =5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_n-1_fvsalpha')
plt.clf()
#----------------------------------------
# }}}

# Plot B:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title('Magnetic Field Profiles for n=-1', FontSize=25)
plt.plot(data_n_1_param1['x'], data_n_1_param1['B'], '-',LineWidth=1.6,c='b')
plt.plot(data_n_1_param2['x'], data_n_1_param2['B'], '--',LineWidth=1.6,c='r')
plt.plot(data_n_1_param3['x'], data_n_1_param3['B'], '-',LineWidth=1.6,c='g')
plt.plot(data_n_1_param4['x'], data_n_1_param4['B'], '-',LineWidth=1.6,c='m')
plt.plot(data_n_1_param5['x'], data_n_1_param5['B'], '-',LineWidth=1.6,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\hat{B}(\hat{r})$',FontSize=20)
ax.set_ylim(bottom=-1.02)
ax.set_xlim(left=0,right=30)
ax.legend((r'$\alpha =1$', r'$\alpha =2$',r'$\alpha =3$',r'$\alpha =4$',r'$\alpha =5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_n-1_Bvsalpha')
plt.clf()
#----------------------------------------
# }}}

# Plot Electric Field:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title('Electric Field Profiles for n=-1', FontSize=25)
plt.plot(data_n_1_param1['x'], data_n_1_param1['A0`'], '-',LineWidth=1.6,c='b')
plt.plot(data_n_1_param2['x'], data_n_1_param2['A0`'], '--',LineWidth=1.6,c='r')
plt.plot(data_n_1_param3['x'], data_n_1_param3['A0`'], '-',LineWidth=1.6,c='g')
plt.plot(data_n_1_param4['x'], data_n_1_param4['A0`'], '-',LineWidth=1.6,c='m')
plt.plot(data_n_1_param5['x'], data_n_1_param5['A0`'], '-',LineWidth=1.6,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\hat{E}(\hat{r})$',FontSize=20)
ax.set_ylim(bottom=-0.1)
ax.set_xlim(left=0,right=30)
ax.legend((r'$\alpha =1$', r'$\alpha =2$',r'$\alpha =3$',r'$\alpha =4$',r'$\alpha =5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_n-1_Evsalpha')
plt.clf()
#----------------------------------------
# }}}

# Plot Energy:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title('Energy Density for n=-1', FontSize=25)
plt.plot(data_n_1_param1['x'], data_n_1_param1['energy'], '-',LineWidth=1.6,c='b')
plt.plot(data_n_1_param2['x'], data_n_1_param2['energy'], '--',LineWidth=1.6,c='r')
plt.plot(data_n_1_param3['x'], data_n_1_param3['energy'], '-',LineWidth=1.6,c='g')
plt.plot(data_n_1_param4['x'], data_n_1_param4['energy'], '-',LineWidth=1.6,c='m')
plt.plot(data_n_1_param5['x'], data_n_1_param5['energy'], '-',LineWidth=1.6,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\frac{\mathcal{E}(\hat{r})}{2 \pi v^2}$',FontSize=20)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0,right=30)
ax.legend((r'$\alpha =1$', r'$\alpha =2$',r'$\alpha =3$',r'$\alpha =4$',r'$\alpha =5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_n-1_energyvsalpha')
plt.clf()
#----------------------------------------
# }}}

# Plot Energy*r:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title('Energy Density for n=-1', FontSize=25)
plt.plot(data_n_1_param1['x'], data_n_1_param1['energy']*data_n_1_param1['x'], '-',LineWidth=1.6,c='b')
plt.plot(data_n_1_param2['x'], data_n_1_param2['energy']*data_n_1_param2['x'], '--',LineWidth=1.6,c='r')
plt.plot(data_n_1_param3['x'], data_n_1_param3['energy']*data_n_1_param3['x'], '-',LineWidth=1.6,c='g')
plt.plot(data_n_1_param4['x'], data_n_1_param4['energy']*data_n_1_param4['x'], '-',LineWidth=1.6,c='m')
plt.plot(data_n_1_param5['x'], data_n_1_param5['energy']*data_n_1_param5['x'], '-',LineWidth=1.6,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\frac{\hat{r}*\mathcal{E}(\hat{r})}{2 \pi v^2}$',FontSize=20)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0,right=30)
ax.legend((r'$\alpha =1$', r'$\alpha =2$',r'$\alpha =3$',r'$\alpha =4$',r'$\alpha =5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_n-1_energyrvsalpha')
plt.clf()
#----------------------------------------
# }}}

# Plot Charge Density:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title('Charge Density Profiles for n=-1', FontSize=25)
plt.plot(data_n_1_param1['x'], data_n_1_param1['A0'], '-',LineWidth=1.6,c='b')
plt.plot(data_n_1_param2['x'], data_n_1_param2['A0'], '--',LineWidth=1.6,c='r')
plt.plot(data_n_1_param3['x'], data_n_1_param3['A0'], '-',LineWidth=1.6,c='g')
plt.plot(data_n_1_param4['x'], data_n_1_param4['A0'], '-',LineWidth=1.6,c='m')
plt.plot(data_n_1_param5['x'], data_n_1_param5['A0'], '-',LineWidth=1.6,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\hat{A}_0(\hat{r})$',FontSize=20)
ax.set_ylim(bottom=-0.4)
ax.set_xlim(left=0,right=30)
ax.legend((r'$\alpha =1$', r'$\alpha =2$',r'$\alpha =3$',r'$\alpha =4$',r'$\alpha =5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_n-1_A0vsalpha')
plt.clf()
#----------------------------------------
# }}}

# Plot Atheta:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title(r'$A_{\theta}$ Profiles for n=-1', FontSize=25)
plt.plot(data_n_1_param1['x'], data_n_1_param1['Atheta'], '-',LineWidth=1.6,c='b')
plt.plot(data_n_1_param2['x'], data_n_1_param2['Atheta'], '--',LineWidth=1.6,c='r')
plt.plot(data_n_1_param3['x'], data_n_1_param3['Atheta'], '-',LineWidth=1.6,c='g')
plt.plot(data_n_1_param4['x'], data_n_1_param4['Atheta'], '-',LineWidth=1.6,c='m')
plt.plot(data_n_1_param5['x'], data_n_1_param5['Atheta'], '-',LineWidth=1.6,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\hat{A}_{\theta}(\hat{r})$',FontSize=20)
ax.set_ylim(bottom=-1.1)
ax.set_xlim(left=0,right=30)
ax.legend((r'$\alpha =1$', r'$\alpha =2$',r'$\alpha =3$',r'$\alpha =4$',r'$\alpha =5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_n-1_fluxvsalpha')
plt.clf()
#----------------------------------------
# }}}

#----------------------------------------
# }}}

# Compare profiles for alpha=1 for various values of n:
# {{{
#----------------------------------------
# Plot f:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title(r'Scalar Field Profiles for $\alpha=1$', FontSize=15)
plt.plot(data_n_1_param1['x'], data_n_1_param1['f'], '-',LineWidth=1.1,c='b')
plt.plot(data_n_2_param1['x'], data_n_2_param1['f'], '-',LineWidth=1.1,c='r')
plt.plot(data_n_3_param1['x'], data_n_3_param1['f'], '-',LineWidth=1.1,c='g')
plt.plot(data_n_4_param1['x'], data_n_4_param1['f'], '-',LineWidth=1.1,c='m')
plt.plot(data_n_5_param1['x'], data_n_5_param1['f'], '-',LineWidth=1.1,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\hat{f}(\hat{r})$',FontSize=20)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0,right=15)
ax.legend((r'$n=-1$', r'$n=-2$',r'$n=-3$',r'$n=-4$',r'$n=-5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_alpha_1_fvsn')
plt.clf()
#----------------------------------------
# }}}

# Plot B:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title(r'Magnetic Field Profiles for $\alpha=1$', FontSize=15)
plt.plot(data_n_1_param1['x'], data_n_1_param1['B'], '-',LineWidth=1.1,c='b')
plt.plot(data_n_2_param1['x'], data_n_2_param1['B'], '-',LineWidth=1.1,c='r')
plt.plot(data_n_3_param1['x'], data_n_3_param1['B'], '-',LineWidth=1.1,c='g')
plt.plot(data_n_4_param1['x'], data_n_4_param1['B'], '-',LineWidth=1.1,c='m')
plt.plot(data_n_5_param1['x'], data_n_5_param1['B'], '-',LineWidth=1.1,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\hat{B}(\hat{r})$',FontSize=20)
ax.set_ylim(bottom=-1.01)
ax.set_xlim(left=0,right=15)
ax.legend((r'$n=-1$', r'$n=-2$',r'$n=-3$',r'$n=-4$',r'$n=-5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_alpha_1_Bvsn')
plt.clf()
#----------------------------------------
# }}}

# Plot Electric Field:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title(r'Electric Field Profiles for $\alpha=1$', FontSize=15)
plt.plot(data_n_1_param1['x'], data_n_1_param1['A0`'], '-',LineWidth=1.1,c='b')
plt.plot(data_n_2_param1['x'], data_n_2_param1['A0`'], '-',LineWidth=1.1,c='r')
plt.plot(data_n_3_param1['x'], data_n_3_param1['A0`'], '-',LineWidth=1.1,c='g')
plt.plot(data_n_4_param1['x'], data_n_4_param1['A0`'], '-',LineWidth=1.1,c='m')
plt.plot(data_n_5_param1['x'], data_n_5_param1['A0`'], '-',LineWidth=1.1,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\hat{E}(\hat{r})$',FontSize=20)
ax.set_ylim(bottom=-0.02)
ax.set_xlim(left=0,right=15)
ax.legend((r'$n=-1$', r'$n=-2$',r'$n=-3$',r'$n=-4$',r'$n=-5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_alpha_1_Evsn')
plt.clf()
#----------------------------------------
# }}}

# Plot Energy:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title(r'Energy Density Profiles for $\alpha=1$', FontSize=15)
plt.plot(data_n_1_param1['x'], data_n_1_param1['energy'], '-',LineWidth=1.1,c='b')
plt.plot(data_n_2_param1['x'], data_n_2_param1['energy'], '-',LineWidth=1.1,c='r')
plt.plot(data_n_3_param1['x'], data_n_3_param1['energy'], '-',LineWidth=1.1,c='g')
plt.plot(data_n_4_param1['x'], data_n_4_param1['energy'], '-',LineWidth=1.1,c='m')
plt.plot(data_n_5_param1['x'], data_n_5_param1['energy'], '-',LineWidth=1.1,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\frac{\mathcal{E}(\hat{r})}{2 \pi v^2}$',FontSize=20)
ax.set_ylim(bottom=0,top=2)
ax.set_xlim(left=0,right=15)
ax.legend((r'$n=-1$', r'$n=-2$',r'$n=-3$',r'$n=-4$',r'$n=-5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_alpha_1_energyvsn')
plt.clf()
#----------------------------------------
# }}}

# Plot Charge Density:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title(r'Charge density profile for $\alpha=1$', FontSize=15)
plt.plot(data_n_1_param1['x'], data_n_1_param1['A0'], '-',LineWidth=1.1,c='b')
plt.plot(data_n_2_param1['x'], data_n_2_param1['A0'], '-',LineWidth=1.1,c='r')
plt.plot(data_n_3_param1['x'], data_n_3_param1['A0'], '-',LineWidth=1.1,c='g')
plt.plot(data_n_4_param1['x'], data_n_4_param1['A0'], '-',LineWidth=1.1,c='m')
plt.plot(data_n_5_param1['x'], data_n_5_param1['A0'], '-',LineWidth=1.1,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\hat{A}_0(\hat{r})$',FontSize=20)
ax.set_ylim(bottom=-0.38)
ax.set_xlim(left=0,right=15)
ax.legend((r'$n=-1$', r'$n=-2$',r'$n=-3$',r'$n=-4$',r'$n=-5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_alpha_1_A0vsn')
plt.clf()
#----------------------------------------
# }}}

# Plot Atheta:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title(r'$A_{\theta}$ profile for $\alpha=1$', FontSize=15)
plt.plot(data_n_1_param1['x'], data_n_1_param1['Atheta'], '-',LineWidth=1.1,c='b')
plt.plot(data_n_2_param1['x'], data_n_2_param1['Atheta'], '-',LineWidth=1.1,c='r')
plt.plot(data_n_3_param1['x'], data_n_3_param1['Atheta'], '-',LineWidth=1.1,c='g')
plt.plot(data_n_4_param1['x'], data_n_4_param1['Atheta'], '-',LineWidth=1.1,c='m')
plt.plot(data_n_5_param1['x'], data_n_5_param1['Atheta'], '-',LineWidth=1.1,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\hat{A}_{\theta}(\hat{r})$',FontSize=20)
ax.set_ylim(bottom=-5.1)
ax.set_xlim(left=0,right=15)
ax.legend((r'$n=-1$', r'$n=-2$',r'$n=-3$',r'$n=-4$',r'$n=-5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_alpha_1_fluxvsn')
plt.clf()
#----------------------------------------
# }}}


# Plot Energy*r:
# {{{
#----------------------------------------
ax=plt.gca()
plt.title(r'Energy Density Profiles for $\alpha=1$', FontSize=15)
plt.plot(data_n_1_param1['x'], data_n_1_param1['energy']*data_n_1_param1['x'], '-',LineWidth=1.1,c='b')
plt.plot(data_n_2_param1['x'], data_n_2_param1['energy']*data_n_2_param1['x'], '-',LineWidth=1.1,c='r')
plt.plot(data_n_3_param1['x'], data_n_3_param1['energy']*data_n_3_param1['x'], '-',LineWidth=1.1,c='g')
plt.plot(data_n_4_param1['x'], data_n_4_param1['energy']*data_n_4_param1['x'], '-',LineWidth=1.1,c='m')
plt.plot(data_n_5_param1['x'], data_n_5_param1['energy']*data_n_5_param1['x'], '-',LineWidth=1.1,c='tab:orange')
plt.xlabel(r'$\hat{r}$',FontSize=20)
plt.ylabel(r'$\frac{\hat{r}*\mathcal{E}(\hat{r})}{2 \pi v^2}$',FontSize=20)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0,right=15)
ax.legend((r'$n=-1$', r'$n=-2$',r'$n=-3$',r'$n=-4$',r'$n=-5$'))
plt.tight_layout()
plt.savefig('python-plots/solution_plots/solution_dimensionless_alpha_1_energyrvsn')
plt.clf()
#----------------------------------------
# }}}

#----------------------------------------
# }}}
