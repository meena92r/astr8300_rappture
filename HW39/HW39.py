# ----------------------------------------------------------------------
#  GRAPH
#
#  This simple example shows how you can use the Rappture toolkit
#  to handle I/O for a simple simulator--in this case, one that
#  evaluates an x/y graph
#
# ======================================================================
#  AUTHOR:  Michael McLennan, Purdue University
#  Copyright (c) 2004-2012  HUBzero Foundation, LLC
#
#  See the file "license.terms" for information on usage and
#  redistribution of this file, and for a DISCLAIMER OF ALL WARRANTIES.
# ======================================================================

import Rappture
import sys
from math import *
import numpy as np
from scipy.integrate import odeint
from scipy import optimize

def f(x, formula):
    return eval(formula)

def calc(y, x, formula):
    return eval(formula)

def main():
    io = Rappture.library(sys.argv[1])

    xmin = float(io.get('input.number(min).current'))
    xmax = float(io.get('input.number(max).current'))
    y0 = float(io.get('input.number(Y0).current'))
    npts = int(io.get('input.number(Npts).current'))
    formula = io.get('input.string(formula).current')

    x = np.linspace(xmin, xmax, npts)
    sol = odeint(calc, y0, x, args=(formula,))

    io.put('output.curve(result0).about.label','f(X) vs X',append=0)
    io.put('output.curve(result0).yaxis.label','f(X)')
    io.put('output.curve(result0).xaxis.label','X')

    io.put('output.curve(result1).about.label','Integral of f(X) vs X',append=0)
    io.put('output.curve(result1).yaxis.label','Integral of f(X)')
    io.put('output.curve(result1).xaxis.label','X')

    for i in range(npts):
        io.put(
               'output.curve(result0).component.xy',
               '%g %g\n' % (x[i],f(x[i],formula)), append=1
              )
        io.put(
               'output.curve(result1).component.xy',
               '%g %g\n' % (x[i],sol[i][0]), append=1
              )

    root = optimize.brentq(f, xmin, xmax, args=(formula,))

    my_str = 'Root of f(x) in the range ' + str(xmin) + ' to ' + \
             str(xmax) + ' is ' + str(root)

    io.put('output.string(result2).about.label', 'Root')
    io.put('output.string(result2).current', my_str)

    Rappture.result(io)

if __name__ == "__main__":
    main()

