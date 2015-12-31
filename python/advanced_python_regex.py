import pandas as pd
import re
import string
import csv
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

def read_file(file_path):
    data = []
    dictionary = {}
    with open(file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    header  = data[0]
    body = data[1:]
        
    for i in range(len(header)):
        column = []
        for row in body:
            column.append(row[i])
        dictionary[header[i]] = column
    return dictionary


def main():
    faculty = pd.DataFrame.from_csv("~/repos/dsp/python/faculty.csv")
### Q1
    print "############Question 1: Count of different degree types are:############\n".upper()
    degrees = faculty[' degree']
    unique_degrees = get_unique_degree(degrees)
    acronyms = generate_match_list(unique_degrees)
    print get_degree_counts(degrees, acronyms)
    print "\n"
### Q2
    print "############Question 2: Count of different faculty types is:############\n".upper()
    titles = faculty[' title']
    title_template = get_words_by_length(titles, length_atleast=4)
    print get_title_counts(titles, title_template)
    print "\n"
### Q3
    print "############Question 3: list of email addresses############\n".upper()
    faculty = read_file('faculty.csv')
    emails = faculty[' email']
    for i in emails: 
        print i 
    print "\n"
### Q4
    faculty = read_file('faculty.csv')
    emails = faculty[' email']
    email_domains = map(lambda x: re.findall(r'@.*', x), emails)
    email_domains = [i[0] for i in email_domains]
    email_domains = set(email_domains)

    print "############Question 4: list of different email domains:############\n".upper()
    for i in email_domains:
        print i




if __name__ == "__main__":
    main()
