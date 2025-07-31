def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        return True
    
def nextPrime(a):
    if a<=1:
        return 2
    else:
        prime=a+1
        while not isPrime(prime):
            prime+=1
        return prime
isPrime(10)
print(nextPrime(11))