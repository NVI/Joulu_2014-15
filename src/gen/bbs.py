# an example of the Blum Blum Shub generator (BBS)
# when (large) parameters p, q are not known, BBS has good cryptographical properties
# here we use p = 100000007, q = 300000119 for the sake of an example (primes p, q from Wolfram Alpha)

class bbs(object):
    def __init__(self,seed): # initializes the generator with a seed
        self.p = 100000007
        self.q = 300000119
        self.idx = 0
        self.arr = [0xffffffff + seed]*32
    
    def generate(self): # generates 32 new numbers for extraction method
        for i in range(0,32):
            self.arr[i] = (self.arr[(i+31)%32])**2
            self.arr[i] %= self.p*self.q
    
    def extract(self): # extracts an integer from [0, 2**32-1]
        if (self.idx == 0):
            self.generate()
        y = self.arr[self.idx]%0x100000000
        ++self.idx
        self.idx %= 32
        return y
    
    def randarray(self,n): # extracts n floats from [0,1]
        v = [0]*n
        for i in range(0,n):
            v[i] = self.extract()/0xffffffff
        return v
