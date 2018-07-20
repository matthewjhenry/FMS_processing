# Make sure all these packages are installed
# i.e. : numpy, netCDF4, matplotlib
import numpy as np
import matplotlib.pyplot as plt
import netCDF4

def mean_lat(lat,val):
    if(lat.shape[0] != val.shape[0]):
        print("Latitude and value vectors not of same size.")
        return 0
    else :
        # assume lat in degrees
        w = np.cos(lat*np.pi/180)
        return np.sum(val*w)/np.sum(w)

# Then as an example, let's plot the surface temperature
# with a horizontal line where the average is.

# Going to use example data in ./data/* which is
# average of history files from a 
# control run of AM2rad
data = netCDF4.Dataset('./data/day_ave.nc')

# get sigma and latitude variables
sig_ = data.variables['sigma'][:]
lat_ = data.variables['lat'][:]

# To list variables in file, do 
# > print(data.variables)

# Get surface temperature
surf_temp = data.variables['temp'][:][29,:]

# Check that variable is right shape
# > print(surf_temp.shape)

plt.figure(1)

# plot surface temperature
plt.plot(lat_,surf_temp,'k',label='300ppm')

# plot horizontal line
plt.axhline(y=mean_lat(lat_,surf_temp), color='r')

plt.legend(loc='best')
plt.grid()
plt.xticks(np.linspace(-90,90,7))
plt.xlim(-90,90)
plt.xlabel('Latitude (deg N)')
plt.ylabel('K')
plt.title('Surface temperature (300ppm)')
fig = plt.gcf()
plt.show()
#fig.savefig('directory/filename.eps')
