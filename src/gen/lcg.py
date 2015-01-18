# an example of a 32-bit linear congruential generator (LCG)
# historically most common generator, still used in e.g. Java
# many parameters could be used, here we use a=1664525, c=1013904223 from Numerical Recipes (ref. Wikipedia)

class lcg(object):
    def __init__(self,seed): # initializes the generator with a seed
        self.a = 1664525
        self.c = 1013904223
        self.idx = 0
        self.arr = [0]*1000
        for i in range(0,1000):
            self.arr[i] = ((seed+i)*(0xffffffff-seed-i)*i)%0x100000000
        self.generate()
        self.generate()
    
    def generate(self): # generates 1000 new numbers for extraction method
        for i in range(0,1000):
            self.arr[i] = (self.a*self.arr[(i+999)%1000]+self.c)%0x100000000
    
    def extract(self): # extracts an integer from [0, 2**32-1]
        if (self.idx == 0):
            self.generate()
        y = self.arr[self.idx]
        ++self.idx
        self.idx %= 1000
        return y
    
    def randarray(self,n): # extracts n floats from [0,1]
        v = [0]*n
        for i in range(0,n):
            v[i] = self.extract()/0xffffffff
        return v
