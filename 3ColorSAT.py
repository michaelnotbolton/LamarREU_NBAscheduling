#read in string
#graphstring = input("Input:")
#graphstring = "{0: [1, 2], 1: [0, 2], 2: [0, 1]}"
graphstring = "{0: [1, 2, 3, 4, 5, 6, 7], 1: [0, 2, 3, 4, 5, 6, 7], 2: [0, 1, 3, 4, 5, 6, 7], 3: [0, 1, 2, 4, 5, 6, 7], 4: [0, 1, 2, 3, 5, 6, 7], 5: [0, 1, 2, 3, 4, 6, 7], 6: [0, 1, 2, 3, 4, 5, 7], 7: [0, 1, 2, 3, 4, 5, 6]}"

graph = eval(graphstring)

#print(graph)
keys = graph.keys()

edges = []
for key in keys:
    for child in graph[key]:
        if not(((key,child) in edges) or ((child,key) in edges)):
            edges.append((key,child))
print(edges)

def number_of_vars():
    #number of edges
    n = len(edges)
    return n

def number_of_clauses():
    #4 clauses for every edge
    n = 4*number_of_vars()
    # how many clauses for each vertex?

    return n

VARIABLE_COUNT = 0
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
    str_comments = "c Practice CNF \n"
    return str_comments

#construct p as p + type + #variable + #clauses
def pline():
    str_pline = "p cnf "
    str_pline += str(number_of_vars()) + " "
    str_pline += str(number_of_clauses()) + "\n"
    return str_pline


def edges_clauses():
    global VARIABLE_COUNT
    edge_clause = ""
    for edge in edges:
        map = {"a":str(VARIABLE_COUNT+1),"b":str(VARIABLE_COUNT+2),"c":str(VARIABLE_COUNT+3)}
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
        VARIABLE_COUNT+=3
        edge_clause += final_key_clause + "\n"
    return edge_clause

def vertex_clauses():
    global VARIABLE_COUNT
    v_clause_str = ""
    for edge in edges:
        #each edge has 3 color variables
        #each color being 3%1, 3%2, 3%3
        VARIABLE_COUNT=3
    return v_clause_str

print(create_cnf())
