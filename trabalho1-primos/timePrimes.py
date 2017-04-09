"""
Comparacao de tempo entre algoritmos de primalidade
"""
import millerRabin
import fermat
import datetime
import random

values = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

def primes():
    for val in values:
        print '%d bits: ' % val

        start = datetime.datetime.now()
        prime = False
        while not prime:
            prime = millerRabin.is_prime(random.getrandbits(val), 40)
        end = datetime.datetime.now()
        delta = end - start
        print '\tMiller-Rabin: %dms' % (delta.total_seconds() * 1000)

        start = datetime.datetime.now()
        prime = False
        while not prime:
            prime = fermat.is_prime(random.getrandbits(val), 40)
        end = datetime.datetime.now()
        delta = end - start
        print '\tFermat: %dms' % (delta.total_seconds() * 1000)

def main():
    primes()

if __name__ == '__main__':
    main()
