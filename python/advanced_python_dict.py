import csv
import pdb
import re

def main():
    dictionary = {}
    with open('faculty.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            pdb.set_trace
            try: 
                dictionary[row[0].split()[-1]].append([
                            row[1],
                            row[2][:row[2].find("Professor") + len("Professor")], 
                            row[3],
                            ]
                        )
            except KeyError:
                dictionary[row[0].split()[-1]] = [
                        [
                        row[1],
                        row[2][:row[2].find("Professor") + len("Professor")], 
                        row[3],
                        ]
                    ]

    # for value in dictionary['Li']:
    #     print value
    print "######### Question 6 ########"
    for i in range(3):
        print dictionary.keys()[i], str(dictionary[dictionary.keys()[i]]).strip("[]")
        
# reset_dictionary for question 7 
    dictionary = {}

    with open('faculty.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            pdb.set_trace
            try: 
                dictionary[(row[0].split()[0], row[0].split()[-1])].append([
                            row[1],
                            row[2][:row[2].find("Professor") + len("Professor")], 
                            row[3],
                            ]
                        )
            except KeyError:
                dictionary[(row[0].split()[0], row[0].split()[-1])] = [
                        [
                        row[1],
                        row[2][:row[2].find("Professor") + len("Professor")], 
                        row[3],
                        ]
                    ]
    print "######### Question 7 ########"
    for i in range(3):
        print dictionary.keys()[i], str(dictionary[dictionary.keys()[i]]).strip("[]")




if __name__ == '__main__':
    main()
