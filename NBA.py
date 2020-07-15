import os
class Team:
    '''A structure to hold team information'''

    def __init__(self, conf, div, name, reg_name, home, code):
        self.conference = conf
        self.division = div
        self.name = name
        self.regional_name = reg_name
        self.hometown = home
        self.code = code

    def get_conference(self):
        return self.conference

    def get_division(self):
        return self.division

    def get_name(self):
        return self.name

    def get_regional_name(self):
        return self.regional_name

    def get_hometown(self):
        return self.hometown

    def get_code(self):
        return self.code

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

lst_conferences = ["West","East"]
lst_divisions = ["Atlantic","Central","Northwest","Pacific","Southeast","Southwest"]

class NBA:
    ''' A structure for NBA organization '''
    def __init__(self):
        name_file = open(os.getcwd() + os.sep + "teams.csv","r")
        self.lst_teams = []
        self.lst_w_teams = []
        self.lst_e_teams = []
        self.dict_divisions = {}
        for line in name_file:
            teaminfo = line.split(",")
            teaminfo[4] = teaminfo[4][0:len(teaminfo[4])]
            team = Team(teaminfo[4],teaminfo[3],teaminfo[0],teaminfo[1],teaminfo[2],teaminfo[5])
            self.lst_teams.append(team)
            if team.get_conference() == "West":
                self.lst_w_teams.append(team)
            else:
                self.lst_e_teams.append(team)
            if team.get_division() in self.dict_divisions.keys():
                self.dict_divisions[team.get_division()].append(team)
            else:
                self.dict_divisions.update({team.get_division():[team]})

    def west_teams(self):
        return self.lst_w_teams

    def east_teams(self):
        return self.lst_e_teams

    def division_list(self,div):
        return self.dict_divisions[div]

    def teams(self):
        return self.lst_teams

    def west_divisions(self):
        lst_divs = []
        for team in self.lst_teams:
            if team.get_conference()=="West":
                lst_divs.append(team)
        return lst_divs

    def east_divisions(self):
        lst_divs = []
        for team in self.lst_teams:
            if team.get_conference()=="East":
                lst_divs.append(team)
        return lst_divs
