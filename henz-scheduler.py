from nba import NBA
import pycosat as sat
import itertools
from itertools import combinations, chain 
import numpy

nba = NBA()

codes = [team.get_code() for team in nba.lst_teams]

var_list = []
poss_var = ["_H","_A","_B"]

for team in codes: #for each team
    for i in range(180): # for each day
        new_vars = [team+"_"+str(i)+a for a in poss_var]
        var_list += new_vars

var_map = {team:index for (index,team) in enumerate(var_list)}

clause_list = [] #he's gonna be a fat boi

def create_clauses():
    global clause_list
    #for each HAB Set, only one may be true
    clause_list += hab_clauses() #Adds 4 clauses for every 3 HAB set (len(var_list)/3)*4
    #clause_list += max_games_limit_clauses() #adds a lot of clauses

def hab_clauses():
    hab_clause_list = []
    for i in range(int(len(var_list)/3)):
        start_i = i*3
        vars3 = [start_i+1,start_i+2,start_i+3]
        hab_clause_list += [vars3]
        for j in range(3):
            tempvars = [1 for i in range(3)]
            tempvars[j] = -1
            tempvars = list(numpy.multiply(vars3,tempvars))
            hab_clause_list += [tempvars]
    return hab_clause_list

def tl_equal(subvars,n):
    return list(map(set, itertools.combinations(subvars, n)))

def max_games_limit_clauses():
    limit_clauses = []

    return limit_clauses




create_clauses()
solution = sat.solve(clause_list)
print(solution)