# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists are mutable (changeable) and tuples are immutable(unchangeable).  

You can't use a list as a key because of the way dictionaries work.  I believe python will let you "technically" use a list as a dictionary key but you would be losing out on the quick lookup time (O(1)) for a dictionary.  

When you request a value with a key, the key is run through the hash function which returns a specific value corresponding to the numerical location (in memory) for that specific value.  

This is fast because there's no "look up" involved.  There's no "Searching involved".  

In order for this to work, the key must stay the same.  It must stay the same so that the returned value from the hash function for that key always gets you to the same numerical location/bucket(in memory).  

If you use a mutable (changeable) object, this won't always be the case.  If your key can change then the hash function will no longer send you the correct "bucket"

example of why dictionaries are so fast.

if I have a dictionary that has 1024 buckets and my hash function is : h(x) = x*8:

my_dict[3] = 'hello' <<<--- this will store 'hello' into the (3*8) bucket "24"

When I look up my_dict[3] all the computer has to do is a multiplication (which computers are incredibly fast at doing O(1))




---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

##### How lists and sets are similar. 
**How are they similar?**
Sets and lists are both muteable(changeable). Sets only contain unique values that aren't ordered. Lists contain values without regard for uniqueness and are ordered. 

    
**SETS**

Use Example: 

    let's say want to know the number of unique entries in some data?  

    in: set = {1,2,2,2,2}
    in: set
    out: {1,2}
    
Putting these into the **set** allowed me to see what unique entities there are in the data. 

**Sets** are also great for what their name implies "set theory" You can do unions, differences, and other mathematical operations within set theory fast.  


Use Example:

    set1 = {1,2,3}
    set2 = {3,4,5}
    in: set1.union(set2)
    out: {1,2,3,4,5}

Implementing this with **lists** would involve searching O(log(n)) before comparing O(1).  It would e a lot slower.  

Performance of finding an element: 
- Membership of 1 element in a set is O(1)


**LISTS**

Lists are useful anywhere order is needed.  Sets do not have this.  

Performance: 
- Lists can return indexes based on a search O(n) if unsorted O(log(n)) if sorted.
- Lists can be sliced with O(1) (once you know what part you want to slice)
Useful for: 
- when you have ranges of sorted data you'd like to return
    - dates, orders, sequential information of some kind

**Why are they different?**

The two biggest differences:

- Sets use only hashed values, without storing any other information.  
- Lists don't hash, but do keep order. 
    - This gives you order which sets can't give
    - Membership checking is slower because you'd have to search first ( O(log(n)) once sorted)


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

**What is Lambda?**
*lambda* is a way to define a function.  It is used for defining a function anonymously(without namespace).

*def* generates a function with namespace that you call elsewhere.  This hides the logic of the function which is sometimes desired.  However, in cases where you want to communicate exactly what is happening, you will defer to a lambda function which communicates intent more directly.  

**Example**

	In [29]: listofnames
	Out[29]: 
	['ryan lambert',
	 'raechel lambert',
	 'paul lambert',
	 'poo bear',
	 'severus snape']
	
Sorted by first name

	In [30]: sorted(listofnames, key=(lambda x: x.split(" ")[0]))
	Out[30]: 
	['paul lambert',
	 'poo bear',
	 'raechel lambert',
	 'ryan lambert',
	 'severus snape']
	
Sorted by last name

	In [31]: sorted(listofnames, key=(lambda x: x.split(" ")[1]))
	Out[31]: 
	['poo bear',
	 'ryan lambert',
	 'raechel lambert',
	 'paul lambert',
	 'severus snape']


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

**list comprehensions** are a compact way to construct a list and communicate logical intent.  They're usually accomplished in one line.  

**examples for map vs comprehension**

    In [58]: listofnames
    Out[58]: 
    ['ryan lambert',
     'raechel lambert',
     'paul lambert',
     'poo bear',
     'severus snape']
    
    In [49]: map(lambda x: len(x), listofnames)
    Out[49]: [12, 15, 12, 8, 13]
    
    In [50]: [len(word) for word in listofnames]
    Out[50]: [12, 15, 12, 8, 13]

**examples for filter vs comprehension**

    In [59]: filter(lambda x: len(x) < 14, listofnames)
    Out[59]: ['ryan lambert', 'paul lambert', 'poo bear', 'severus snape']
    
    In [60]: [i for i in listofnames if len(i) < 14]
    Out[60]: ['ryan lambert', 'paul lambert', 'poo bear', 'severus snape']

**how do these compare?**

Though similar, map and filter *seem* to give a clearer "intent" for what you're trying to do to the list. Using a list comprehension requires you to read further into the line to see what you're goal is in the comprehension. Though, upon some reading on stackoverflow it appears there are differing views on what people prefer to look at. 

In both cases, whether you use one of the builtin functions (map or filter) or a list comprehension you are accomplishing the same thing. 

**demonstrate dict comprehensions**

    In [92]: keys
    Out[92]: ['key1', 'key2', 'key3']
    
    In [93]: values
    Out[93]: ['value1', 'value2', 'value3']
    
    In [94]: {keys[i[0]]: values[i[0]] for i in enumerate(keys)}
    Out[94]: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

**demonstrate set comprehensions**

    In [98]: values = [1,1,1,1,1,2,2,2,2]

    In [99]: {i for i in values}
    Out[99]: {1, 2} 

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)


---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





