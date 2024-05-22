import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc4
import os
import requests
import os
import argparse
import datetime as dt
import pandas as pd
import statsmodels.api as sm
from scipy.interpolate import interp1d
import datetime as dt
from scipy import stats
from scipy import linalg
import statsmodels.formula.api as smf

def plotting_model(site_result, all_data):
    """ 
    
    Function to plot linear models 
    
    Parameters
    ----------
    site_result : list
        A list containing the linear regression result, site label, and figure label

    all_data : list
        A list containing kelp canopy data, SST data, and site label
        
    Returns
    -------
    Plots of linear regressions with R^2 values, labeled with an asterisk if significant

    """
    index = 0
    for result in site_result:
        
        slope = result[0].slope
        intercept = result[0].intercept
        r2 = result[0].rvalue**2
        pvalue = result[0].pvalue*6

        c1 = result[0].slope
        c0 = np.exp(result[0].intercept)
        
        site = all_data[index]

        plt.figure()
        plt.plot(site[1]['SST'], site[0]['kelp_area_m2'], '.')
        plt.title(result[2])
        dense_sst = np.linspace(np.min(site[1]['SST']), np.max(site[1]['SST']), 100)
        if pvalue < 0.05:
            plt.plot(dense_sst, c0*np.exp(c1*dense_sst), 'r-', label='R$^2$ ='+str(round(r2,3))+'*')
            plt.ylabel(result[1] + ' Kelp Canopy Area (m$2$)')
            plt.xlabel(result[1] + ' Winter Average SST ($^{\circ}$C)')
            plt.legend(loc='best')
            plt.show()
            index = index +1

        else:
            plt.plot(dense_sst, c0*np.exp(c1*dense_sst), 'r-', label='R$^2$ ='+str(round(r2,3)))
            plt.ylabel(result[1] + ' Kelp Canopy Area (m$2$)')
            plt.xlabel(result[1] + ' Winter Average SST ($^{\circ}$C)')
            plt.legend(loc='best')
            plt.show()
            index = index +1


def printing_results(site_results):

    """ 
    
    Function to plot linear models 
    
    Parameters
    ----------
    site_result : list
        A list containing the linear regression result, site label, and figure label
        
    Returns
    -------
    Site, R^2 value, p-value, and standard error

    """
    for result in site_results:

        pvalue=result[0].pvalue*6
        r2 = result[0].rvalue**2
        standard_error = result[0].stderr
        print (result[1], 'R^2 =', round(r2, ndigits=3), 'p-value =', round(pvalue, ndigits=3), 
               'Standard error =', round(standard_error, ndigits=3) )