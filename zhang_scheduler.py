from NBA import NBA
import pycosat as sat
import itertools
from itertools import combinations, chain
import numpy
import copy
import datetime
import os
try:
    import _pickle as pickle
except:
    import pickle

version = [1]
#KEEP THIS UPDATED - increment every time addtional clause methods are added or clause methods are changed


#start day assumed as the 3rd Tuesday of October
start_date = datetime.datetime(2020,10,20)



previous_exists = os.path.exists("./clauses.pkl")
if previous_exists:
    with open("./version.txt") as f:
        versions_line = eval(f.readline())
        up_to_date = (versions_line == version)

start_time = datetime.datetime.now()
def elapsed():
    time = datetime.datetime.now() - start_time
    time = str(int(time.total_seconds()//1)) + " sec"
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

#list of intraconference, interdivision games that won't be played this season, home game listed first
#this is for the 2018-2019 season
#add generation method (previous 5 year's schedules -> current year's no_play_list)
no_play_list = ["ATL_BKN","ATL_CLE","BKN_IND","BKN_ORL","BOS_CHI","BOS_WAS","CHA_IND","CHA_TOR","CHI_CHA","CHI_NYK","CLE_ORL","CLE_PHI","DAL_DEN","DAL_LAL","DEN_LAL","DEN_MEM","DET_ATL","DET_BKN","GSW_SAS","GSW_UTA","HOU_LAC","HOU_MIN","IND_MIA","IND_TOR","LAC_MIN","LAC_NOP","LAL_MEM","LAL_OKC","MEM_OKC","MEM_PHX","MIA_CHI","MIA_NYK","MIL_BOS","MIL_WAS","MIN_DAL","MIN_PHX","NOP_GSW","NOP_POR","NYK_CHA","NYK_CLE","OKC_GSW","OKC_SAS","ORL_BOS","ORL_MIL","PHI_MIA","PHI_MIL","PHX_HOU","PHX_POR","POR_HOU","POR_SAC","SAC_DAL","SAC_DEN","SAS_SAC","SAS_UTA","TOR_ATL","TOR_DET","UTA_LAC","UTA_NOP","WAS_DET","WAS_PHI",""]

var_list = []

#this generates our list of variables
for home_team in codes: # for each home team
    for away_team in codes: # for each away team/
        if away_team != home_team: #if not the same team
            str_var = home_team + "_" + away_team + "_" #create their prefix
            for day in range(180): # for each day
                var_list += [str_var + str(day)] #add their complete name to the list


# instead of using linear time var_list.index() we can use a constat time dictionary lookup
var_dict = {var:index+1 for (index,var) in enumerate(var_list)}
index_to_var_dict = {index+1:var for (index,var) in enumerate(var_list)}

clause_list = []

def read_static_clauses():
    global clause_list
    global version
    global previous_exists
    global up_to_date

    if (not previous_exists) or (not up_to_date):
        print("Updating local clauses.pkl")
        if previous_exists:
            os.remove("./clauses.pkl")

        #clause_list += day_exclusion_clauses() #add day clauses
        #print(f"Day exlusion clauses added at time {elapsed()} with {len(clause_list)} clauses")

        # clause_list += intraconference_clauses() #add intraconference clauses
        # print(f"IntraCon Clauses added at time {elapsed()} with {len(clause_list)} clauses")

        clause_list += interconference_clauses() #add interconference clauses
        print(f"InterCon Clauses added at time {elapsed()} with {len(clause_list)} clauses")

        clause_list += one_game_per_team_per_day_clauses()
        print(f"1 game/team/day clauses added at time {elapsed()} with {len(clause_list)} clauses")

        print(version,file=open("./version.txt","w+"))

        pickle_on = open("clauses.pkl","wb")
        pickle.dump(clause_list,pickle_on)
        pickle_on.close()

        '''
        with open("./clauses.pkl","a") as f:

            #f.write(f"{clause_list}") '''

        print(f"Added static clauses to text file at time {elapsed()}")

    else:
        print("Reading from clauses.pkl")

        pickle_off = open("clauses.pkl","rb")
        clause_list = pickle.load(pickle_off)
        pickle_off.close()
        '''
        with open("./clauses.pkl") as f:
            f.readline()
            clause_list = eval(f.readline())
            '''
        print(f"Read static clauses ad time {elapsed()} with {len(clause_list)} clauses")

def create_clauses():
    global clause_list

    read_static_clauses() #add previously saved clauses


# needs work
def day_exclusion_clauses(team_codes, daynum): # ensures that the teams in the teams list don't play on the day, daynum
    clauses = []
    for home_team in team_codes: # for each home team
        team_codes_sans_home = copy.copy(team_codes) # copy the set of teams
        team_codes_sans_home.remove(home_team) # and remove the home team, teams don't play themselves
        for away_team in team_codes_sans_home: # for each away team
            clauses.append(0-var_dict[home_team+"_"+away_team+"_"+str(daynum)]) # a clause of just var ensures that it is false in a solution
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

def intraconference_clauses(): # each team plays 4 games against each other team in their division
    clauses = []
    for conference in [east_codes, west_codes]: # these clauses need to be generated for both conferences
        for team in conference: # for each team in the conference
            for other_team in conference:
                if team != other_team: # teams don't play themselves
                    team_pair_var_set = []
                    for day in range(180): # to get this game for every day of the season
                        team_pair_var_set.append(var_dict[team+"_"+other_team+"_"+str(day)])
                    if team+"_"+other_team not in no_play_list: # check that they need to play four games not 1
                        clauses.extend(true_literal_equals_clause(team_pair_var_set,2))
                    else: # if they're set to play only three games this season and team is the the home team for the dropped game
                        clauses.extend(true_literal_equals_clause(team_pair_var_set,1))
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

def games_in_nights_blocking_clauses(num_games, num_nights):
    clauses = []
    for team in codes: # for each team
        games_on_days = [] # a list of lists, the first entry is a list of the games playable on the first day
        for day in range(180): # since the above list is populated by day
            games_today = [] # these are the games played by team on this day
            for other_team in codes: # for each opponent
                if team != other_team: # teams can't play themselves
                    games_today.append(var_dict[team+"_"+other_team+"_"+str(day)]) # home game
                    games_today.append(var_dict[other_team+"_"+team+"_"+str(day)]) # away game
            games_on_days.append(games_today) # appending this todays games to the list
        for day in range(180-num_nights+1): # every possible set of num_nights adjacent nights by the first night
            games_to_block = [] # all the possible games team might play in that set of num_nights
            for i in range(num_nights): # building games_to_block by day
                games_to_block.extend(games_on_days[day+i]) # adding each nights games
            clauses.extend(true_literal_leq_clause(games_to_block, num_games)) #adding those blocking clauses
            

# ensures exactly k of the n variables in n_vars is true
def true_literal_equals_clause(n_vars,k):
    clauses = []
    for comb in itertools.combinations(n_vars,len(n_vars)-k+1): # for each combination of n-k+1 variables, to ensure at least k variables are true
        clause = []
        for element in comb: # parses through the elements of the combination to build the associated clause
            clause += [element]
        clauses.append(clause)
    for comb in itertools.combinations(n_vars,k+1): # for each combination of n-(n-k)+1 = k+1 variables, to ensure at least n-k variables are false
        clause = []
        for element in comb: # parses through the elements of the combination to build the associated clause
            clause += [0-element] # the negative is because we want to ensure the variables are false
        clauses.append(clause)
    return clauses

# ensures at most k of the n variables in n_vars is true
def true_literal_leq_clause(n_vars,k):
    clauses = []
    clauses = [[(0-element) for element in comb] for comb in itertools.combinations(n_vars,(k+1))]
    for comb in itertools.combinations(n_vars,k+1): # for each combination of n-(n-k)+1 = k+1 variables, to ensure at least n-k variables are false
        clause = []
        for element in comb: # parses through the elements of the combination to build the associated clause
            clause += [0-element] # the negative is because we want to ensure the variables are false
        clauses.append(clause)
    return clauses

def schedule(solution):
    schedule = {i:[] for i in range(1,181)}
    for game in solution:
        game = game.split("_")
        schedule[int(game[2])].append(game)

    schedule = {day:schedule[day] for day in schedule.keys() if schedule[day] !=[]}

    max_length = max([len(schedule[key]) for key in schedule.keys()])

    strings = ["" for i in range(max_length+1)]
    for key in schedule.keys():
        col_head = start_date + datetime.timedelta(days=key)
        col_head = col_head.strftime("%B %d |")

        strings[0] += col_head
        for i in range(max_length):
            if i<len(schedule[key]):
                strings[i+1] += schedule[key][i][1] + " @ " + schedule[key][i][0] + "|"
            else:
                strings[i+1] += "          "

    str_schedule = ""
    for string in strings:
        str_schedule  += string + "\n"

    return str_schedule

def solve():
    global clause_list
    solution = sat.solve(clause_list)
    solution = [index_to_var_dict[n] for n in solution if n>0]

    scheduled = schedule(solution)

    print(scheduled,file=open("./solution.txt","w+"))
    print(f"Solved at time {elapsed()} with {len(clause_list)} clauses")


def test():
    # print(true_literal_equals_clause(range(180),2))

    create_clauses()

    solve()

    print(f"Finished in {elapsed()}")
test()
