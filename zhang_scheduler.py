from NBA import NBA
import pycosat as sat
import itertools
from itertools import combinations, chain
import numpy

nba = NBA()

codes = [team.get_code() for team in nba.lst_teams]

var_list = []

for home_team in codes: # for each home team
    codes_sans_home = codes
    codes_sans_home.remove(home_team)
    for away_team in codes_sans_home: # for each away team/
        print(home_team+"_"+away_team)
        for i in range(180): # for each day
            if home_team+"_"+away_team+"_"+str(i) == "PHI_CHI_123":
                print("wlek")
            var_list += home_team+"_"+away_team+"_"+str(i)

clause_list = []

def create_clauses():
    global clause_list

def day_exclusion_clauses(daynum):
    clauses = []
    for home_team in codes: # for each home team
        codes_sans_home = codes
        codes_sans_home.remove(home_team)
        for away_team in codes_sans_home: # for each away team
            clauses += str(-var_list.index(home_team+"_"+away_team+"_"+str(daynum)))
print(len(var_list))
print(day_exclusion_clauses(13))
