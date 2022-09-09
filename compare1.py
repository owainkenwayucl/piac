# This script compares the performance (time, error) for three algorithms
# with a set number of interations.

from piac import *
import sys
import math

def bench(lower, step, upper):
	current = lower

	# precompile
	tt, tp, te = timefunc(integralpi, 1, 1)
	tt, tp, te = timefunc(montecarlopi, 1, 1)
	tt, tp, te = timefunc(gridpi, 1, 1)

	print("Samples, Integral time, Integral error, Monte Carlo time, Monte Carlo error, Grid time, Grid error")
	while (current < upper):
		dim = math.floor(math.sqrt(current))
		real = dim * dim
		it, ip, ie = timefunc(integralpi, dim, dim)
		mt, mp, me = timefunc(montecarlopi, dim, dim)
		gt, gp, ge = timefunc(gridpi, dim, dim)
		print(str(real) + ", " + str(it) + ", " + str(ie) + ", " + str(mt) + ", " + str(me) + ", " + str(gt) + ", " + str(ge) + ", " )

		current += step


if __name__ == '__main__':
	begin = 1000
	stop = 10000
	step = 100

	if len(sys.argv) > 1:
		begin = int(sys.argv[1])
	if len(sys.argv) > 2:
		step = int(sys.argv[2])
	if len(sys.argv) > 3:
		stop = int(sys.argv[3])

	bench(begin, step, stop)
	

