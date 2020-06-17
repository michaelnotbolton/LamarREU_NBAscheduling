#read in string
#graphstring = input("Input:")
graphstring = "{0: [1, 2], 1: [0, 2], 2: [0, 1]}"

graph = eval(graphstring)

print(graph)
keys = graph.keys()

edges = []
for key in keys:
    for child in graph[key]:
        if not(((key,child) in edges) or ((child,key) in edges)):
            edges.append((key,child))

def number_of_vars():
    #number of edges
    n = len(edges)
    return n

def number_of_clauses():
    #4 clauses for every edge
    n = 4*number_of_vars
    # how many clauses for each vertex?

    return n
    
variable_count = 0
#compile CNF piece by piece
def create_cnf():
    str_cnf = ""
    str_cnf += comments()
    str_cn += pline()
    str_cnf += "c Edge Clauses \n"
    str_cn += edges_clauses()
    return str_cnf

def comments():
    str_comments = "\
    c Practice CNF"
    return str_comments

#construct p as p + type + #variable + #clauses
def pline():
    str_pline = "p cnf "
    str_pline += str(number_of_vars()) + " "
    str_pline += str(number_of_clauses()) + "\n"
    return str_pline

def edges_clauses():
    edge_clause = ""
    for edge in edges:
        variable_count = c
        map = {a:c+1,b:c+2,c:c+3}
        for key in map.keys():
            for k in map.keys():
                if k != key:
                    edge_clause += "-" str(k)
                else
        