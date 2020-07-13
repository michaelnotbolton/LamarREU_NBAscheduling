import pycosat as sat

def resolveCNFtoList(cnf):
    cnf = cnf.split("\n")
    cnf_array = [line.split(" ") for line in cnf]
    cnf_array = [line for line in cnf_array if clean(line)]
    for i, line in enumerate(cnf_array):
        cnf_array[i] = [c for c in line if clean2(c)]
        cnf_array[i] = [int(c) for c in cnf_array[i]]
    return(cnf_array)

def clean(arr):
    if arr[0]=="c" or arr[0] =="p":
        return False
    if arr == ['']:
        return False
    return True

def clean2(c):
    if (c != "0") and (c != ''):
        return True
    return False

class Pycosat_Solver:
    '''A wrapper for DIMACS format'''


    def __init__(self, dimac):
        self.dimac = dimac
        self.cnf = resolveCNFtoList(self.dimac)


    def solve(self,list_cnf=None):
        if list_cnf == None:
            list_cnf = self.cnf
        return sat.solve(list_cnf)

    def solve_iter(self,list_cnf=None,propopagate_limit=None):
        if list_cnf == None:
            list_cnf = self.cnf
        print(list_cnf)
        if propopagate_limit == None:
            return sat.itersolve(list_cnf)
        else:
            return sat.itersolve(list_cnf,prop_limit=propopagate_limit)



#unit testing code
''''
sample_cnf = "1 2 0 \n \
-1 -2 0 \n \
3 4 0 \n \
-3 -4 0 \n \
1 3 0 \n \
-1 -3 0 \n \
2 4 0 \n \
-2 -4 0\n"

def test_solve():
    satengine = Pycosat_Solver(sample_cnf)
    solution = satengine.solve()
    print(solution)

def test_iter():
    satengine = Pycosat_Solver(sample_cnf)
    solution = satengine.solve_iter()
    for i,sol in enumerate(solution):
        print(str(i))
        print(sol)

#test_solve()
test_iter()
'''