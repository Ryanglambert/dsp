[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)


The question is asking what percentage of the United States population falls within the height requirements for blue man group.  

It seems it is more appropriate for a confidence interval in this case.  And for fun I will apply it to each critical z.  

My answers: 
```
cdf(z_critical_upper) - cdf(z_critical_lower) = total area under curve

0.8323 -  0.4996  = .3327

% 33.27 Can be Blue Men

Lower bound for lower z_crticical is:  (0.47, 0.51) CI 95%
Upper bound for upper z_critical is:  (0.81, 0.86) CI 95%
```


for reference please see my python notebook: https://github.com/Ryanglambert/dsp/blob/master/statistics/For%20Computation.ipynb
