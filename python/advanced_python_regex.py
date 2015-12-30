import pandas as pd
import re
import string
# import string << probly won't need

def clean_acronym(s):
    exclude = set(string.punctuation)
    s = ''.join(ch for ch in s if ch not in exclude)
    s = s.lower()
    return s

def get_unique(df):

    unique_degrees = pd.unique(df)
    unique_degrees = [i.strip() for i in unique_degrees]
    unique_degrees = [i.split(" ") for i in unique_degrees]
    unique_degrees = [val for sublist in unique_degrees for val in sublist]
    unique_degrees = map(clean_acronym, unique_degrees)
    unique_degrees = pd.unique(unique_degrees)
    return unique_degrees

def generate_match_list(simple_acronyms):
    acronyms = []
    for i in simple_acronyms:
        acronyms.append(tuple(i))
    return acronyms

def get_degree_counts(degrees):
    degree_occurences = {}
    for acronym in acronyms:
        key = r"(?i)" + r"%s\.*"*len(acronym) % acronym
        # pdb.set_trace()
        num_occurences = degrees.str.contains(key).sum()
        degree_occurences[clean_acronym(acronym)] = num_occurences
    return pd.Series(degree_occurences).sort_values(ascending=False)

faculty = pd.DataFrame.from_csv("~/repos/dsp/python/faculty.csv")
degrees = faculty[' degree']
unique_degrees = get_unique(degrees)
acronyms = generate_match_list(unique_degrees)

print get_degree_counts(degrees)


