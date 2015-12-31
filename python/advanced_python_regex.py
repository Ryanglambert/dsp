import pandas as pd
import re
import string
# import string << probly won't need

def clean_acronym(s):
    exclude = set(string.punctuation)
    s = ''.join(ch for ch in s if ch not in exclude)
    s = s.lower()
    return s

def get_unique_degree(df):
    df = pd.unique(df)
    df = [i.strip() for i in df]
    df = [i.split(" ") for i in df]
    df = [val for sublist in df for val in sublist]
    df = map(clean_acronym, df)
    df = pd.unique(df)
    return df

def generate_match_list(simple_acronyms):
    acronyms = []
    for i in simple_acronyms:
        acronyms.append(tuple(i))
    return acronyms

def get_degree_counts(degrees, acronyms):
    degree_occurences = {}
    for acronym in acronyms:
        key = r"(?i)" + r"%s\.*"*len(acronym) % acronym
        # pdb.set_trace()
        num_occurences = degrees.str.contains(key).sum()
        degree_occurences[clean_acronym(acronym)] = num_occurences
    return pd.Series(degree_occurences).sort_values(ascending=False)

def get_words_by_length(words, length_atleast=4):
    filter_string = r"\b\w{" + str(length_atleast) + r",}\b"
    return tuple(set(tuple(re.findall(filter_string,word)) for word in words))

def get_title_counts(titles, title_filter):
    title_occurences = {}
    # unique_titles = pd.unique(titles)
    for title in title_filter:
        key = r'(?i)' + r'(\b%s\b).*' * len(title)  % title
        num_occurences = titles.str.contains(key).sum()  ## hitting the limit of my abilities
        title_occurences[title] = num_occurences
    return title_occurences


def main():
    faculty = pd.DataFrame.from_csv("~/repos/dsp/python/faculty.csv")
### Q1
    degrees = faculty[' degree']
    unique_degrees = get_unique_degree(degrees)
    acronyms = generate_match_list(unique_degrees)
    print get_degree_counts(degrees, acronyms)
### Q2
    titles = faculty[' title']
    title_template = get_words_by_length(titles, length_atleast=4)
    print get_title_counts(titles, title_template)



if __name__ == "__main__":
    main()
