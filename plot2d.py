# Make sure you install all these packages
# i.e. : matplotlib, netCDF4, numpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import netCDF4
import numpy as np

# Going to use example data in ./data/* which is
# average of history files from a 
# control run of AM2rad
data = netCDF4.Dataset('./data/day_ave.nc')

# get sigma and latitude variables
sig_ = data.variables['sigma'][:]
lat_ = data.variables['lat'][:]

# To list variables in file, do 
# > print(data.variables)

# Let's get temperature as an example
temp = data.variables['temp'][:]

# Check that variable is right shape
# > print(temp.shape)

# Plot temperature in 2d plot

plt.figure(1)
lat, sig = np.meshgrid(lat_, sig_)
# cmap to change color map
plt.pcolor(lat,sig, temp, cmap='RdBu_r')
plt.axis([lat.min(), lat.max(), sig.max(), sig.min()])
plt.colorbar()
# plt.clim(mini,maxi) to impose bounds
plt.xticks(np.linspace(-90, 90, 7))
plt.xlabel('Latitude (deg N)')
plt.ylabel('Sigma level (p/ps)')
plt.title('Temperature (K) (300ppm)')
fig = plt.gcf()
plt.show()
# fig.savefig('saving_directory/fig1.eps')

# Plot temperature with contours
# This is a fancier way, for a paper for example.

plt.figure(2)
# determine lower bound, upper bound and number of contours
temp_min = 200
temp_max = 300
temp_num = 11

lat, sig = np.meshgrid(lat_, sig_)
levels = np.linspace(temp_min,temp_max,temp_num)
col = cm.RdBu(np.linspace(1, 0, len(levels)))
cs = plt.contourf(lat, sig, temp, levels, colors=col, extend="both")
plt.axis([lat.min(), lat.max(), sig.max(), sig.min()])
cb = plt.colorbar()
# change contour color here
plt.contour(cs, colors='k')
plt.xticks(np.linspace(-90, 90, 7))
plt.yticks(np.linspace(1,0,6))
plt.xlabel('Latitude (deg)')
plt.ylabel('Sigma level (p/ps)')
plt.title('Temperature (K) (300ppm)')
fig = plt.gcf()
plt.show()
#fig.savefig('fig2.eps')
