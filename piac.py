import sys
import time
import math
import random
import numba

@numba.jit(parallel=True, nopython=True)
def integralpi(n, m):
	numsamples = n*m
	totalsum = 0
	step = 1.0/numsamples

	for i in numba.prange(numsamples):
		x = (i + 0.5) * step
		totalsum += 4.0/(1.0 + (x * x))

	p = totalsum * step
	return p, abs(p - math.pi)
	
@numba.jit(parallel=True, nopython=True)
def montecarlopi(n, m):
	numsamples = n*m

	count = 0
	for a in numba.prange(numsamples):
		x = random.random()
		y = random.random()
		if ((x*x + y*y) <= 1):
			count += 1

	p = 4*count/numsamples
	return p, abs(p - math.pi)

@numba.jit(parallel=True, nopython=True)
def gridpi(n, m):
	p = math.pi
	xstep = 1.0/n
	ystep = 1.0/m

	count = 0
	for a in numba.prange(n):
		for b in range(m):
			x = 0.0 + (a * xstep)
			y = 0.0 + (b * ystep)
			if ((x*x + y*y) <= 1):
				count += 1

	p = 4*count/(n*m)


	return p, abs(p - math.pi)


def timefunc(function, n, m):
	start = time.time()
	p, err = function(n,m)
	stop = time.time()
	return (stop - start), p, err


