# Calculating the standard deviation

In this exercise we are going to remind ourselves how to compute the variance.  We will also see that computing the error is not simply a matter of computing the variance.

Recall that the sample variance is given by:

![](https://render.githubusercontent.com/render/math?math=\langle(E-\langle\E\rangle)^2\rangle=\frac{N}{N-1}\left[\frac{1}{N}\sum_{t=1}^NE_t^2-\left(\frac{1}{N}\sum_{t=0}^NE_t\right)^2\right])

For this exercise I want you to calculate this quantity for:

* The first 100 energies in this file
* The second 100 energies in this file
* The third 100 energies in the file 
* and so on. 

The values for these 10 variances should be stored in the array called `variances`, which I have already created for you and which you will notice is plotted in the final few lines of Python in the panel on the left.

In addition to computing these 10 values for the block variance I would also like you to compute the variance using all the data in the trajectory.  The value of this variance should be stored in a variable called `total_var`.  You will notice that the plotting commands at the end of the script show the value of this total variance as a straight, blue line.

When you plot the final graph you should find that black dots illustrating the block variances should all be reasonably close to the blue line.  This makes sense - both sets of calculations that you are performing here are estimating the same quantity.  The only difference is that when you compute the variances from each block of data you have fewer data points.  
