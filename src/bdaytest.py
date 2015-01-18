# partial progress towards the birthday test of Diehard test suite
# no rigorous way to compare distributions is included here, but at least we can visualize

import gen
import dist
import stats

def main():
    n = 1001
    s = 0x123456
    g = gen.alfg(s)
    d = dist.uniform(g.randarray(n),0,50)
    d.sort()
    diff = [0]*1000
    for i in range(0,1000):
    	diff[i] = d[i+1]-d[i]
    stats.uinfo(diff)

if __name__ == '__main__':
    main()
