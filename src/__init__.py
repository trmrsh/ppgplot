"""
implements pgplot for Python.

This works with numpy arrays. The documentation of the 
functions is only partially complete. In general they 
follow the calling sequence of the original PGPLOT, but 
usually skip the number of points since these are 
contained within the numpy arrays. You will still need
to look at the PGPLOT documentation for a complete 
explanation of the various parameters.

As example of use (plotting a sinusoid)
is as follows:

import numpy as npy
from ppgplot import *

x = npy.linspace(0,10.,100)
y = sin(x)

pgopen('/xs')
pgenv(0.,10.,-1.1,1.1,0,0)
pglab('Angle (rad)', 'y = sin(x)','')
pgline(x,y)
pgclos()


Note how the call to pgline does not require the number of points (it even 
does not need the same number of points, but will plot up to the minimum number
in x and y).
"""

from _ppgplot import *

