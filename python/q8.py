import csv 
import numpy as np
import pandas as pd
# import pdb

football = pd.DataFrame.from_csv('~/repos/dsp/python/football.csv')
football['win/loss difference'] = football['Wins'] - football['Losses']

smallest_difference = \
football[football['win/loss difference'] == football['win/loss difference'] \
.apply(lambda x: abs(x)).min()]

print "These teams had the lowest difference between wins and losses: "
for i in smallest_difference.index:
    print i
# find the smallest difference between "for" and "against" goals

# def read_data(data):
#     data_list = []
#     with open(data, 'rb') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',')
#         for row in reader:
#             data_list.append(row)
#     headers = data_list[0]
#     body = data_list[1:]
#     data_dict = {headers[i]: [row[i] for row in body] for i in range(len(headers))}
#     # return data_dict
#     return data_dict

# data = read_data('/Users/ryanlambert/repos/dsp/python/football.csv')
# pdb.set_trace()


# def get_min_score_difference(self, parsed_data):
#   # COMPLETE THIS FUNCTION
#     pass

# def get_team(self, index_value, parsed_data):
#   # COMPLETE THIS FUNCTION
#     pass
