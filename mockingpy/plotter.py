import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np
import glob
import os
import seaborn as sns

class PlotSpec():
    def __init__(self,files):
        self.path = os.getcwd()
        self.filenames = [filename for filename in glob.glob(self.path+'/'+files)]
        self.colors()
        self.plot()

    def colors(self):
        #purpleblue = ['#642e7c','#7251b7','#8984d6','#93bae1','#8ce2ee']*10
        #icey = ['#003279','#4386bb','#8bbedc','#cccce4','#fbb9cd','#896eb6','#6a1364','#49175f','#020316']*10
        icey2 = ['#0f142d','#112a60','#2a2e62','#205094','#50356f','#3a79b9','#8c7fb2','#84acd5','#babed9','#f0c6d6','#ead8e1']*10
        for color in icey2:
            yield color

    def labels(self):
        labels = [filename.replace(self.path+'/','') for filename in self.filenames]
        for label in labels:
            yield label

    def plot(self):
        x = np.arange(3540.5,3540.5+(4300*0.9),0.9)
        fig, ax = plt.subplots(1,1,figsize=(20,5))
        colors = self.colors()
        labels = self.labels()
        for filename in self.filenames:
            self.data = fits.open(filename)[0].data
            ax.plot(x, self.data, color=next(colors), label=next(labels))
        ax.set_xlabel('wavelength [nm]')
        ax.set_ylabel('flux')
        ax.set_title('Mock spectra')
        leg=ax.legend(bbox_to_anchor=(1, 1))
        plt.tight_layout()
        for line in leg.get_lines():
            line.set_linewidth(10)
        plt.show()




