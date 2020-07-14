from nba import NBA
import pycosat as sat
import itertools
from itertools import combinations, chain 
import numpy

nba = NBA()

codes = [team.get_code() for team in nba.lst_teams]