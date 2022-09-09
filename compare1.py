# This script compares the performance (time, error) for three algorithms
# with a set number of interations.

from piac import *
import sys

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
	

