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
        name_file = open(os.getcwd() + os.sep + "teams_small.csv","r")
        self.lst_teams = []
        self.lst_w_teams = []
        self.lst_w_nw_teams = []
        self.lst_w_p_teams = []
        self.lst_w_sw_teams = []
        self.lst_e_teams = []
        self.lst_e_a_teams = []
        self.lst_e_c_teams = []
        self.lst_e_se_teams = []
        for line in name_file:
            teaminfo = line.split(",")
            teaminfo[4] = teaminfo[4][0:len(teaminfo[4])]
            team = Team(teaminfo[4],teaminfo[3],teaminfo[0],teaminfo[1],teaminfo[2],teaminfo[5])
            self.lst_teams.append(team)
            if team.get_conference() == "West":
                self.lst_w_teams.append(team)
                if team.get_division() == "Southwest":
                    self.lst_w_sw_teams.append(team)
                elif team.get_division() == "Pacific":
                    self.lst_w_p_teams.append(team)
                else:
                    self.lst_w_nw_teams.append(team)
            else:
                self.lst_e_teams.append(team)
                if team.get_division() ==  "Southeast":
                    self.lst_e_se_teams.append(team)
                elif team.get_division() == "Atlantic":
                    self.lst_e_a_teams.append(team)
                else:
                    self.lst_e_c_teams.append(team)

    def west_teams(self):
        return self.lst_w_teams

    def west_northwest_teams(self):
        return self.lst_w_nw_teams
    
    def west_pacific_teams(self):
        return self.lst_w_p_teams

    def west_southwest_teams(self):
        return self.lst_w_sw_teams

    def east_teams(self):
        return self.lst_e_teams

    def east_atlantic_teams(self):
        return self.lst_e_a_teams

    def east_central_teams(self):
        return self.lst_e_c_teams

    def east_southeast_teams(self):
        return self.lst_e_se_teams

    def teams(self):
        return self.lst_teams
