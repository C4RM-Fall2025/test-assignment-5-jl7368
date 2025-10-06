import numpy as np

def FizzBuzz(start, finish):
    v = np.arange(start, finish + 1).astype(object)
    mask3 = (v % 3 == 0)
    mask5 = (v % 5 == 0)
    mask15 = (v % 15 == 0)
    v[mask3] = 'fizz'
    v[mask5] = 'buzz'
    v[mask15] = 'fizzbuzz'
    return v
