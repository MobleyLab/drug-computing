#!/bin/env python

"""Motivated by problem 2.18 from Zuckerman's book; extends 2.13 to sum M repeated rolls of dice; generating 300 sums for varying M. Allows examination of shape of distribution with varying M. Some of resulting graphs used in lecture."""

import matplotlib
matplotlib.use('Agg')
from pylab import *
import random

maxnum = 6
N = 1000
trialnr = 3
M = 2
#nbins = 30

values = {}
for trial in range(trialnr):
    if not values.has_key(trial): values[trial] = []
    for n in range(N):
        sum = 0
        for m in range(M):
            sum+= random.randint(1, maxnum)
        values[trial].append( sum/float(M))

    figure()
    n, b, ptc = hist( values[trial], bins = [0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25] )
    #n, b, ptc = hist( values[trial], bins = nbins )
    #n, b, ptc = hist( values[trial]  )
    xlabel('Outcome (average per throw)')
    ylabel('Counts')
    mn = mean( values[trial] )
    sigma = std(values[trial] )
    gauss = normpdf( b, mn, sigma )
    #plot( b, gauss, 'r-')
    savefig( 'histogram_%strials_nr%s_%sthrows.pdf' % (N, trial, M) )
    figure()
    n, b, ptc = hist( values[trial], bins = [0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25], normed = True )
    #n, b, ptc = hist( values[trial], normed = True, bins = nbins )
    #n, b, ptc = hist( values[trial], normed = True)
    xlabel('Outcome (average per throw)')
    ylabel('Probability')
    gauss = normpdf( b, mn, sigma )
    #plot( b, gauss, 'r-')
    savefig( 'histogram_%strials_nr%s_%sthrows_normed.pdf' % (N, trial, M) )
    print "Mean for trial %s is %.2f; stddev is %.2f" % ( trial, mean( values[trial] ), std( values[trial] ) )

