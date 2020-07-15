from NBA import NBA
import pycosat as sat
import itertools
from itertools import combinations, chain
import numpy
import copy
import datetime
import pickle

start_time = datetime.datetime.now()
def elapsed():
    time = datetime.datetime.now() - start_time
    time = str(time.total_seconds()//1) + " sec"
    return time

nba = NBA()

# lists of three letter team codes for every team in the league, conferences, and divisions
codes = [team.get_code() for team in nba.teams()]
west_codes = [team.get_code() for team in nba.west_teams()]
west_northwest_codes = [team.get_code() for team in nba.west_northwest_teams()]
west_pacific_codes = [team.get_code() for team in nba.west_pacific_teams()]
west_southwest_codes = [team.get_code() for team in nba.west_southwest_teams()]
east_codes = [team.get_code() for team in nba.east_teams()]
east_atlantic_codes = [team.get_code() for team in nba.east_atlantic_teams()]
east_central_codes = [team.get_code() for team in nba.east_central_teams()]
east_southeast_codes = [team.get_code() for team in nba.east_southeast_teams()]


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

def read_static_clauses():
    return ""

def create_clauses():
    global clause_list

    read_static_clauses() #add previously saved clauses

    #clause_list += interconference_clauses() #add interconference clauses
    #print(f"InterCon Clauses added at time {elapsed()} with {len(clause_list)} clauses")

    #clause_list += one_game_per_team_per_day_clauses()
    #print(f"1 game/team/day clauses added at time {elapsed()} with {len(clause_list)} clauses")
    

# needs work
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
    for team in codes: # for each team
        for day in range(180): # for each day of the season for said team
            team_day_var_set = [] # the set of all games a team can play on a specific day
            for other_team in codes: # populating the set of all games a team can play on a specific day opponent wise
                if team != other_team: # teams can't play themselves
                    team_day_var_set.append(var_dict[team+"_"+other_team+"_"+str(day)]) # home game
                    team_day_var_set.append(var_dict[other_team+"_"+team+"_"+str(day)]) # away game
            clauses.extend(true_literal_leq_clause(team_day_var_set,1)) # limiting the set to at most one can be true
    return clauses

# ensures exactly k of the n variables in n_vars is true
def true_literal_equals_clause(n_vars,k):
    clauses = []
    for comb in itertools.combinations(n_vars,len(n_vars)-k+1): # for each combination of n-k+1 variables, to ensure at least k variables are true
        clause = ""
        for element in comb: # parses through the elements of the combination to build the associated clause
            clause += str(element) + " "
        clauses.append(clause.strip())
    for comb in itertools.combinations(n_vars,k+1): # for each combination of n-(n-k)+1 = k+1 variables, to ensure at least n-k variables are false
        clause = ""
        for element in comb: # parses through the elements of the combination to build the associated clause
            clause += "-" + str(element) + " " # the negative is because we want to ensure the variables are false
        clauses.append(clause.strip())
    return clauses

# ensures at most k of the n variables in n_vars is true
def true_literal_leq_clause(n_vars,k):
    clauses = []
    for comb in itertools.combinations(n_vars,k+1): # for each combination of n-(n-k)+1 = k+1 variables, to ensure at least n-k variables are false
        clause = ""
        for element in comb: # parses through the elements of the combination to build the associated clause
            clause += "-" + str(element) + " " # the negative is because we want to ensure the variables are false
        clauses.append(clause.strip())
    return clauses

def save_static_clauses():
    
    print(clause_list,file=open("./clauses.txt",'a'))

def test():

    
    #print(len(interconference_clauses()))
    #print(len(one_game_per_team_per_day_clauses()))
    #print(true_equals_literal_clause(["1","2","3","4","5"],3))
    #print(day_exclusion_clauses(123))

    create_clauses()
    save_static_clauses()

    print(f"Finished in {elapsed()}")
test()