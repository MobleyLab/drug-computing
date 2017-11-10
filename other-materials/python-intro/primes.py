def nextprime(primelist):
    #find the maximum term in primelist and start one more than it
    k = max(primelist) + 1
    #starting at this number find the next integer that is
    #not divisible by any number in primelist
    while True:
        FoundDivisor = False
        #search current primes for a divisor; if found, k not a prime
        for prime in primelist:
            if k % prime == 0:
                FoundDivisor = True
                #break the loop since we don't need to test further
                break
        #check if we found any divisors
        if FoundDivisor:
            #try the next number
            k += 1
        else:
            #found a prime; return it
            return k

#set the max prime
upperlimit = 50

#find all primes less than or equal to this value
l = [2]
while l[-1] < upperlimit:
    l.append(nextprime(l))

#trim out the last element, which is greater than upperlimit
l = l[:-1]

#print out the list
print(l)
