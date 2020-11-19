import matplotlib.pyplot as plt
import numpy as np

# Read in the energies from a file
eng = np.loadtxt("energies")[:,1]

# Create a list with 10 elements that you will use to hold the variances
variances = 10*[0]

# Your code goes here

# This will draw a graph of your variances
x = np.linspace( 1, 11, 10 )
plt.plot( x, variances, 'ko')
plt.plot( [1,10], [total_var,total_var], 'b-' )
plt.savefig( "block_variances.png")
