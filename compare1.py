# This script compares the performance (time, error) for three algorithms
# with a set number of interations.

import piac
import sys
import math

def bench(lower, step, upper):
	current = lower

	print("Samples, Integral time, Integral error, Monte Carlo time, Monte Carlo error, Grid time, Grid error")
	while (current < upper):
		dim = math.floor(math.sqrt(current))
		real = dim * dim
		it, ip, ie, iess = piac.timefunc(piac.integralpi, dim, dim)
		mt, mp, me, ms = piac.timefunc(piac.montecarlopi, dim, dim)
		gt, gp, ge, gs = piac.timefunc(piac.gridpi, dim, dim)
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
	

