[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)


    If I surveyed the children to infer family size then I would expect to receive n**2 observations of family size for each family where "n" is the number of children.   this is because there are three respondents who will speak for every family that has 3 children in it.  This makes it likely to here from children coming from families of 3 children 3 times more than actual. 

    To correct for this I can weight them according to what family size they're claimed to be from.  
    i.e. If a child says they're from a family of size 3, I will weight that entry of family size by 1/3 when I calculate the probability mass function(normalized data).
    
    More generally in the form of an equation: 

    P(num_children) = number of stated children / number of stated children / total number of respondents

    From the question:

This is the unbiased data

    |Ch   |Probability  |
    | --- |:-----:|
    |0    | 0.4662|
    |1    | 0.2141|
    |2    | 0.1963|
    |3    | 0.0871|
    |4    | 0.0256|
    |5    | 0.0107|

This is the biased data

    |Ch   |Probability  |
    | --- |:-----:|
    |0    | 0.0,  |
    |1    | 0.2089|
    |2    | 0.3832|
    |3    | 0.2552|
    |4    | 0.1002|
    |5    | 0.0523|


Please see my notebook for reference: https://github.com/Ryanglambert/dsp/blob/master/statistics/For%20Computation.ipynb


