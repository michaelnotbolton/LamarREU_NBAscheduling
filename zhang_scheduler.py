from NBA import NBA
import pycosat as sat
import itertools
from itertools import combinations, chain
import numpy
import copy
import datetime

start_time = datetime.datetime.now()

nba = NBA()

codes = [team.get_code() for team in nba.teams()]
west_codes = [team.get_code() for team in nba.west_teams()]
east_codes = [team.get_code() for team in nba.east_teams()]

var_list = []

#this generates our list of variables
for home_team in codes: # for each home team
    for away_team in codes: # for each away team/
        if away_team != home_team: #if not the same team
            str_var = home_team + "_" + away_team + "_" #create their prefix
            for day in range(180): # for each day
                var_list += [str_var + str(day)] #add their complete name to the list


# instead of using linear time var_list.index() we can use a constat time dictionary lookup
var_dict = {var:index for (index,var) in enumerate(var_list)} 


clause_list = []

def create_clauses():
    global clause_list

def day_exclusion_clauses(team_codes, daynum): # ensures that the teams in the teams list don't play on the day, daynum
    clauses = []
    for home_team in team_codes: # for each home team
        team_codes_sans_home = copy.copy(team_codes) # copy the set of teams
        team_codes_sans_home.remove(home_team) # and remove the home team, teams don't play themselves
        for away_team in team_codes_sans_home: # for each away team
            clauses.append(str(-var_dict[home_team+"_"+away_team+"_"+str(daynum)])) # a clause of just var ensures that it is false in a solution
    return clauses

def interconference_clauses(): # each team plays two games against every team in the other conference, one home and one away
    clauses = []
    for west_team in west_codes: # built from the point of view of the western conference
        for east_team in east_codes: # every team in the other conference
            home_pairing_var_set = [] # the western team's home game for each interconference pairing
            away_pairing_var_set = [] # the western team's away game for each interconference pairing
            for day in range(180): # populating the arrays for each day of the season
                home_pairing_var_set.append(var_dict[west_team+"_"+east_team+"_"+str(day)])
                away_pairing_var_set.append(var_dict[east_team+"_"+west_team+"_"+str(day)])
            clauses.extend(true_literal_equals_clause(home_pairing_var_set,1)) # each interconference pairing plays exactly one home game for the western conference team
            clauses.extend(true_literal_equals_clause(away_pairing_var_set,1)) # each interconference pairing plays exactly one away game for the western conference team
    return clauses

def one_game_per_team_per_day_clauses():
    clauses = []
    for team in codes:
        codes_sans_one = copy.copy(codes)
        codes_sans_one.remove(team)
        for day in range(180):
            team_day_var_set = []
            for other_team in codes_sans_one:
                team_day_var_set.append(var_dict[team+"_"+other_team+"_"+str(day)])
                team_day_var_set.append(var_dict[other_team+"_"+team+"_"+str(day)])
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

def test():


    #print(len(interconference_clauses()))
    #print(len(one_game_per_team_per_day_clauses()))
    #print(true_equals_literal_clause(["1","2","3","4","5"],3))
    #print(day_exclusion_clauses(123))



    total_time = datetime.datetime.now()-start_time
    print(f"Finished in {total_time}")


test()