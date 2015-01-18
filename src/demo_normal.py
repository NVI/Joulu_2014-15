import gen
import dist
import stats

def main():
    n = 1000 # number of pseudorandoms
    s = 0x123456 # seed value for generator
    g = gen.mt19937_64(s) # using generator MT19937_64
    d = dist.normal(g.randarray(n),0,1) # normal distribution with generator above, mean 0, deviation 1
    stats.info(d) # print basic statistics and visualize

if __name__ == '__main__':
    main()
