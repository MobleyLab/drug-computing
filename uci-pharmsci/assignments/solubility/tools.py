from numpy import *

def rmserr( set1, set2 ):
    """Compute and return RMS error for two sets of equal length involving the same set of samples."""
    tot = 0.
    for i in range(len(set1)):
        tot+= (set1[i] - set2[i])**2
    return sqrt(tot/float(len(set1)))


def correl(x,y ):
    """For two data sets x and y of equal length, calculate and return r, the product moment correlation. """
    if len(x)!=len(y):
        print("ERROR: Data sets have unequal length.\n")
        raise LengthError


    #Compute averages (try not to require numerical library)
    avgx=sum(x)/float(len(x))
    avgy=sum(y)/float(len(y))

    #Compute standard deviations
    sigmax_sq=0
    for elem in x:
        sigmax_sq+=(elem-avgx)**2
    sigmax_sq=sigmax_sq/float(len(x))
    sigmay_sq=0
    for elem in y:
        sigmay_sq+=(elem-avgy)**2
    sigmay_sq=sigmay_sq/float(len(y))

    sigmax=sqrt(sigmax_sq)
    sigmay=sqrt(sigmay_sq)

    #Compute numerator of r
    num=0
    for i in range(len(x)):
        num+=(x[i]-avgx)*(y[i]-avgy)
    #Compute denominator of r
    denom=len(x)*sigmax*sigmay

    corr = num/denom
    return corr


def percent_within_half( x, y):
    """Takes two sets, x and y, of equal length, and returns the percentage of values within 0.5 units."""

    diff = x - y
    indices = where( abs(diff) < 0.5 )
    return 100.*float(len(indices[0]) )/float(len(x))
