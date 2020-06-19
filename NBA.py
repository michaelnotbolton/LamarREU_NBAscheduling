import os
class Team:
    '''A structure to hold team information'''

    def __init__(self, conf, div, name, reg_name, home):
        self.conference = conf
        self.division = div
        self.name = name
        self.regional_name = reg_name
        self.hometown = home

    def get_conference(self):
        return self.conference

    def get_name(self):
        return self.name
    
    def get_division(self):
        return self.division

    def get_regional_name(self):
        return self.regional_name

    def get_hometown(self):
        return self.hometown

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

lst_conferences = ["West","East"]
lst_divisions = ["Atlantic","Central","Northwest","Pacific","Southeast","Southwest"]

class NBA:
    def __init__(self):
        name_file = open(os.getcwd() + "\\teams.csv","r")
        self.lst_teams = []
        self.lst_w_teams = []
        self.lst_e_teams = []
        for line in name_file:
            teaminfo = line.split(",")
            teaminfo[4] = teaminfo[4][0:len(teaminfo[4])-1]
            team = Team(teaminfo[4],teaminfo[3],teaminfo[2],teaminfo[1],teaminfo[0])
            self.lst_teams.append(team)
            if team.get_conference == "West":
                self.lst_w_teams.append(team)
            else:
                self.lst_e_teams.append(team)

    def west(self):
        return self.lst_w_teams

    def east(self):
        return self.lst_e_teams



league = NBA()

print(league.west())

for team in league.west():
    print("done")
    print(team.get_conference())