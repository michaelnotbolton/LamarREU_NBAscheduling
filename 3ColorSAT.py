#read in string
#graphstring = input("Input:")
graphstring = "{0: [1, 2], 1: [0, 2], 2: [0, 1]}"

graph = eval(graphstring)

#print(graph)
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
    n = 4*number_of_vars()
    # how many clauses for each vertex?

    return n
    
variable_count = 0
#compile CNF piece by piece
def create_cnf():
    str_cnf = ""
    str_cnf += comments()
    str_cnf += pline()
    str_cnf += "c Edge Clauses \n"
    str_cnf += edges_clauses()
    str_cnf += "c Vertex Clauses \n"
    str_cnf += vertex_clauses()
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
    global variable_count
    edge_clause = ""
    for edge in edges:
        map = {"a":str(variable_count+1),"b":str(variable_count+2),"c":str(variable_count+3)}
        final_key_clause = ""
        for key in map.keys():
            key_clause = ""
            for k in map.keys():
                if k!=key:
                    key_clause += " -" + map[k]
                else:
                    key_clause += " " + map[k]
            edge_clause += key_clause + "\n"
            final_key_clause += " " + map[key]
        variable_count+=3
        edge_clause += final_key_clause + "\n"
    return edge_clause

def vertex_clauses():
    return ""


print(create_cnf())