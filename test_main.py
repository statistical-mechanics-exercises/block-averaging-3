import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_FinalVar(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[1].get_xydata()
        this_x, this_y = zip(*figdat)
        N = len( eng )
        mean = sum( eng ) / N
        mean2 = sum( np.power(eng,2) ) / N 
        myvar = (N/(N-1))*( mean2 - mean*mean )
        self.assertTrue( np.abs( myvar - this_y[1] )<1e-7, "The value of total_var is incorrect" )
        
    def test_BlockVar(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range(10) :
            thisav = sum( eng[i*100:(i+1)*100] ) / 100
            thisav2 = sum( np.power(eng[i*100:(i+1)*100],2) ) / 100
            myvar = (100/99)*( thisav2 - thisav*thisav )
            self.assertTrue( np.abs( myvar - this_y[i] )<1e-7, "One or more of the values of the block variances are wrong" )
