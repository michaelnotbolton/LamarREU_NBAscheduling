from NBA import NBA
import pycosat as sat
import itertools
from itertools import combinations, chain
import numpy
import copy

nba = NBA()

codes = [team.get_code() for team in nba.teams()]
west_codes = [team.get_code() for team in nba.west_teams()]
east_codes = [team.get_code() for team in nba.east_teams()]

var_list = []

for home_team in codes: # for each home team
    codes_sans_home = copy.copy(codes)
    codes_sans_home.remove(home_team)
    for away_team in codes_sans_home: # for each away team/
        for day in range(180): # for each day
            var_list.append(home_team+"_"+away_team+"_"+str(day))




clause_list = []

def create_clauses():
    global clause_list

def day_exclusion_clauses(daynum):
    clauses = []
    for home_team in codes: # for each home team
        codes_sans_home = copy.copy(codes)
        codes_sans_home.remove(home_team)
        for away_team in codes_sans_home: # for each away team
            clauses.append(str(-var_list.index(home_team+"_"+away_team+"_"+str(daynum))))
    return clauses

def conference_clauses():
    clauses = []
    for west_team in west_codes:
        for east_team in east_codes:
            home_pairing_var_set = []
            away_pairing_var_set = []
            for day in range(180):
                home_pairing_var_set.append(var_list.index(west_team+"_"+east_team+"_"+str(day)))
                away_pairing_var_set.append(var_list.index(east_team+"_"+west_team+"_"+str(day)))
            clauses.extend(true_literal_equals_clause(home_pairing_var_set,1))
            clauses.extend(true_literal_equals_clause(away_pairing_var_set,1))
    return clauses

def one_game_per_team_per_day_clauses():
    clauses = []
    for team in codes:
        codes_sans_one = copy.copy(codes)
        codes_sans_one.remove(team)
        for day in range(180):
            team_day_var_set = []
            for other_team in codes_sans_one:
                team_day_var_set.append(var_list.index(team+"_"+other_team+"_"+str(day)))
                team_day_var_set.append(var_list.index(other_team+"_"+team+"_"+str(day)))
            clauses.extend(true_literal_leq_clause(team_day_var_set,1))
    return clauses

def true_literal_equals_clause(n_vars,k):
    clauses = []
    for comb in itertools.combinations(n_vars,len(n_vars)-k+1):
        clause = ""
        for element in comb:
            clause += str(element) + " "
        clauses.append(clause.strip())
    for comb in itertools.combinations(n_vars,k+1):
        clause = ""
        for element in comb:
            clause += "-" + str(element) + " "
        clauses.append(clause.strip())
    return clauses

def true_literal_leq_clause(n_vars,k):
    clauses = []
    for comb in itertools.combinations(n_vars,k+1):
        clause = ""
        for element in comb:
            clause += "-" + str(element) + " "
        clauses.append(clause.strip())
    return clauses


print(len(conference_clauses()))
# print(len(one_game_per_team_per_day_clauses()))
# print(true_equals_literal_clause(["1","2","3","4","5"],3))
# print(day_exclusion_clauses(123))
