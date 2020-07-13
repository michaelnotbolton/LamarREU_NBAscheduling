from nba import NBA

nba = NBA()
#for an enumeration of the teams and their fields,
#run this for statement

for team in nba.lst_teams:
    print(team) 


print(nba.dict_divisions)
divisions = nba.dict_divisions.keys() # treat each divison as a team to get 1 team per divison

#Input? How to encode the problem. Graph? translate to graph and then the graph answer back?


#SAT Problems-

#       Variables. Which ones?

#       Clauses - What is "pre" structure vs "clause" structur