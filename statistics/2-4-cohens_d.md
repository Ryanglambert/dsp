[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Cohen's D for first babies' weights relative to 'not first born' babies. 

recall:

cohen's D = (Mean_population - Mean_intervention)/std_pooled


calculated:

    pooled_variance = (firsts.totalwgt_lb.var()*len(firsts) + \
    others.totalwgt_lb.var()*len(others))/(len(others) + len(firsts))
    pooled_std = np.sqrt(pooled_variance)

    cohens_d = (firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean())/\
    pooled_std

    print "Cohen's D is: ", cohens_d

    [out]: Cohen's D is:  -0.0886729270726
