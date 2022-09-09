import sys
import time
import math
import random
import numba

@numba.jit(parallel=True, nopython=True)
def integralpi(n, m):
	stats = ''
	numsamples = n*m
	totalsum = 0
	step = 1.0/numsamples

	for i in numba.prange(numsamples):
		x = (i + 0.5) * step
		totalsum += 4.0/(1.0 + (x * x))

	p = totalsum * step
	return p, abs(p - math.pi), stats
	
@numba.jit(parallel=True, nopython=True)
def montecarlopi(n, m):
	numsamples = n*m
	stats = ''

	count = 0
	for a in numba.prange(numsamples):
		x = random.random()
		y = random.random()
		if ((x*x + y*y) <= 1):
			count += 1

	p = 4*count/numsamples
	return p, abs(p - math.pi), stats

@numba.jit(parallel=True, nopython=True)
def gridpi(n, m):
	p = math.pi
	xstep = 1.0/n
	ystep = 1.0/m
	stats = ''

	count = 0
	for a in numba.prange(n):
		for b in range(m):
			x = 0.0 + (a * xstep)
			y = 0.0 + (b * ystep)
			if ((x*x + y*y) <= 1):
				count += 1

	p = 4*count/(n*m)


	return p, abs(p - math.pi), stats

def ensemble(n, m, i):
	stats = {}

	sump = 0.0
	minp = math.inf
	maxp = 0.0
	for a in range(i):
		temp_p, temp_e, temp_s = montecarlopi(n,m)
		sump += temp_p
		maxp = max(maxp, temp_p)
		minp = min(minp, temp_p)

	p = sump/i

	stats['min'] = minp
	stats['max'] = maxp
	stats['mean'] = p

	return p, abs(p - math.pi), stats


def timefunc(function, *args, **kwargs):
	start = time.time()
	p, err, stats = function(*args, **kwargs)
	stop = time.time()
	return (stop - start), p, err, stats

# precompile
tt, tp, te, ts = timefunc(integralpi, 1, 1)
tt, tp, te, ts = timefunc(montecarlopi, 1, 1)
tt, tp, te, ts = timefunc(gridpi, 1, 1)
