# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:47:26 2023

@author: HP
"""

# Python code for the final steady drawing  ( Not for the animation ) :

import numpy as np
import matplotlib.pyplot as plt

# Create an array of theta values in degrees (e.g., from 0 to 113*360 degrees)
theta_degrees = np.linspace(0, 113*360, 10000)

# Convert degrees to radians
theta_radians = np.deg2rad(theta_degrees)

# Calculate z(theta) using the formula , 1j is imaginary number
z = np.exp(theta_radians * 2j) + np.exp(np.pi * theta_radians * 2j)

# Separate the real and imaginary parts of z
x = np.real(z)
y = np.imag(z)

# Create a plot with specific settings
plt.figure(figsize=(10, 10))  # Set a square figure 10x10 inches
plt.plot(x, y, color='orange', linewidth=0.5)  # Set line color to white and line width to 0.5

plt.gca().set_facecolor('black') # Set background color to black
plt.gca().set_aspect('equal')  # Equal aspect ratio
plt.grid(False)  # Turn off the grids
plt.xlim(-12.5, 12.5) # X-axis limit
plt.ylim(-12.5, 12.5) # Y-axis limit

plt.show() # Display the plot