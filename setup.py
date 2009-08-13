from distutils.core import setup, Extension
from distutils.sysconfig import get_python_inc, get_python_lib
import os
import sys
import numpy

###################################################################
# build the extension
#

define_macros      = []
undef_macros       = []
extra_compile_args = []
include_dirs       = []

libraries    = ["cpgplot", "pgplot", "X11", "png", "m", "z", "gfortran"]
library_dirs = ["/usr/X11R6/lib"]

include_dirs.append(numpy.get_include())
undef_macros.append('USE_NUMARRAY')

if os.name == "posix":
    if os.environ.has_key("PGPLOT_DIR"):
        library_dirs.append(os.environ["PGPLOT_DIR"])
        include_dirs.append(os.environ["PGPLOT_DIR"])
    else:
        print >>sys.stderr, "Environment variable PGPLOT_DIR not defined!"
else:
    raise Exception, "os not supported"

ext_pgplot = Extension('_ppgplot',
                       include_dirs  = include_dirs,
                       libraries     = libraries,
                       library_dirs  = library_dirs,
                       runtime_library_dirs = library_dirs,
                       define_macros = define_macros,
                       sources       = [os.path.join('src','_ppgplot.c')])


###################################################################
# the package
#

setup(name="ppgplot",
      version="0.99",
      description="Python interface to PGPLOT",
      author="Tom Marsh (ppgplot from Nick Patavlis and Scott Ransom)",
      author_email="t.r.marsh@warwick.ac.uk",
      packages=['ppgplot'],
      package_dir={'ppgplot':'src'},
      ext_modules=[ext_pgplot])
