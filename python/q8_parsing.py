#!/usr/local/bin/python
# The football.csv file contains the results from the English Premier League. 
## The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv
import numpy as np

    def read_data(data):
        header = []
        body = []
        with open(data, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header.append(reader[0])
            for row in reader[1:]:
                body.append(row)
        return header, body

print read_data('~/repos/dsp/python/football.csv')

     # COMPLETE THIS FUNCTION

      

    def get_min_score_difference(self, parsed_data):
      # COMPLETE THIS FUNCTION

    def get_team(self, index_value, parsed_data):
      # COMPLETE THIS FUNCTION
