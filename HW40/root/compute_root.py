import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import optimize

def f(y, x, b, formula):
    return eval(formula)

def calc(x, a, formula):
    y = odeint(f, -a, [0,x], args=(1, formula))
    return y[1]  # y[0] is int f(x) from 0 to 0

def main():

    # Get arguments

    parser = argparse.ArgumentParser(description='Find root')

    parser.add_argument('formula', type=str, help='f(x)')

    parser.add_argument('--xmin', type=float, default = 0, help='min x')

    parser.add_argument('--xmax', type=float, default = 100, help='max x')

    parser.add_argument('--a', type=float, default = 10, help='a')

    args = parser.parse_args()

    # Get base string

    my_str_base = 'int_0^root (' + args.formula + ') dx - ' + str(args.a)

    # Get compute root of \int_0^x f(x') dx' - a

    root = optimize.brentq(
               calc, args.xmin, args.xmax, args=(args.a, args.formula)
           )

    my_str = '\nRoot of ' + my_str_base +  ' in [' + str(args.xmin) + \
            ', ' + str(args.xmax) + '] is ' + str(root)

    print(my_str)

    # Check

    check = calc(root, args.a, args.formula)

    my_str2 = '\nCheck: ' + my_str_base + ' = ' + str(check[0])

    print(my_str2 + '\n')

if __name__ == "__main__":
    main()

