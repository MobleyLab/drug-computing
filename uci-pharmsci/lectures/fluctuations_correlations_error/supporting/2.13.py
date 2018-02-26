#!/bin/env python

"""Problem motivated by 2.13 of Zuckerman's book; some resulting graphs used in lecture content. Randomly generates integers corresponding to rolling six sided dice; plots histograms for three trials for varying numbers of dice rolls. Calculates mean of each data set as well."""

import matplotlib
matplotlib.use('Agg')
from pylab import *
import random

maxnum = 6
N = 6
trialnr = 3

values = {}
for trial in range(trialnr):
    if not values.has_key(trial): values[trial] = []
    for n in range(N):
        values[trial].append( random.randint(1,maxnum) )

    figure()
    hist( values[trial], bins = [ 1, 2, 3, 4, 5, 6,7] )
    xlabel('Outcome')
    ylabel('Counts')
    savefig( 'histogram_%strials_nr%s.pdf' % (N, trial) )
    print "Mean for trial %s is %.2f; stddev is %.2f" % ( trial, mean( values[trial] ), std( values[trial] ) )

