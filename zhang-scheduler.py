from nba import NBA
import pycosat as sat
import itertools
from itertools import combinations, chain
import numpy

nba = NBA()

codes = [team.get_code() for team in nba.lst_teams]

var_list = []

for home_team in codes: # for each home team
    codes_sans_home = codes.remove(home_team)
    for away_team in codes_sans_home: # for each away team
        for i in range(180): # for each day
            var_list += home_team+"_"+away_team+"_"+i

clause_list = []
