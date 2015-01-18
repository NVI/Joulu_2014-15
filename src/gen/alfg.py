# an example of a 32-bit additive lagged Fibonacci generator (ALFG)
# many parameters could be used, here we use j=30, k=127 from TAOCP (ref. Wikipedia)

class alfg(object):
    def __init__(self,seed): # initializes the generator with a seed
        self.idx = 0
        self.arr = [0]*127
        for i in range(0,127):
            self.arr[i] = ((seed+i)*(0xffffffff-seed-i)*i)%0x100000000
        self.generate()
        self.generate()
    
    def generate(self): # generates 127 new numbers for extraction method
        for i in range(0,127):
            self.arr[i] = (self.arr[i]+self.arr[(i+97)%127])%0x100000000
    
    def extract(self): # extracts an integer from [0, 2**32-1]
        if (self.idx == 0):
            self.generate()
        y = self.arr[self.idx]
        ++self.idx
        self.idx %= 127
        return y
    
    def randarray(self,n): # extracts n floats from [0,1]
        v = [0]*n
        for i in range(0,n):
            v[i] = self.extract()/0xffffffff
        return v
