#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Stefan Landmann 
"""
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap

def scaled_colormap(colormap: str, exponent: float, x_max=10000):
    
    #Define the scaling function. Here we use a power-law scaling
    def scaling_function(x,exponent,x_max=10000):
        if x<x_max/2:
            return(x_max/2-x_max/2*(abs((x-x_max/2)/(x_max-x_max/2)))**exponent)
        else:
            return(x_max/2+x_max/2*(abs((x-x_max/2)/(x_max-x_max/2)))**exponent)
            
    scaled_values=[scaling_function(x,exponent,x_max) for x in np.linspace(0,x_max-1,x_max)]
    colormap_values=cm.get_cmap(colormap)(np.linspace(0,1,x_max))
    scaled_colormap_values=[colormap_values[int(x)] for x in scaled_values]
    return(ListedColormap(scaled_colormap_values))
