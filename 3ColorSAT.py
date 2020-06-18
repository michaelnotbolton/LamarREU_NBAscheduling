#read in string
#graphstring = input("Input:")
#graphstring = "{0: [1, 2], 1: [0, 2], 2: [0, 1]}" #Y
#graphstring = "{0: [1, 2, 3, 4, 5, 6, 7], 1: [0, 2, 3, 4, 5, 6, 7], 2: [0, 1, 3, 4, 5, 6, 7], 3: [0, 1, 2, 4, 5, 6, 7], 4: [0, 1, 2, 3, 5, 6, 7], 5: [0, 1, 2, 3, 4, 6, 7], 6: [0, 1, 2, 3, 4, 5, 7], 7: [0, 1, 2, 3, 4, 5, 6]}" #N
graphstring = "{0: [1, 2, 3, 4, 5, 6], 1: [0, 2, 3, 4, 5, 6], 2: [0, 1, 3, 4, 5, 6], 3: [0, 1, 2, 4, 5, 6], 4: [0, 1, 2, 3, 5, 6], 5: [0, 1, 2, 3, 4, 6], 6: [0, 1, 2, 3, 4, 5]}" #Y

graph = eval(graphstring)

#print(graph)
keys = graph.keys()

edges = []
for key in keys:
    for child in graph[key]:
        if not(((key,child) in edges) or ((child,key) in edges)):
            edges.append((key,child))
edge_map = {edge:[] for edge in edges}
print(edges)

def number_of_vars():
    #number of edges
    n = len(edges)
    return n

clause_count = number_of_vars()*4
def number_of_clauses():
    global clause_count
    return clause_count

VARIABLE_COUNT = 0
#compile CNF piece by piece
def create_cnf():
    str_cnf = ""
    str_cnf += comments()
    str_cnf += "c Edge Clauses \n"
    str_cnf += edges_clauses()
    str_cnf += "c Vertex Clauses \n"
    str_cnf += vertex_clauses()
    str_cnf += pline()
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
            edge_clause += key_clause + " 0 \n"
            final_key_clause += " " + map[key]
        VARIABLE_COUNT+=3
        edge_clause += final_key_clause + " 0 \n"
    return edge_clause

def vertex_clauses():
    global clause_count
    global variable_count
    vertex_clause = ""
    for key in keys:
        incidents = []
        for n in range(0,len(edges)):
            if (edges[n][0] == key or edges[n][1] == key):
                incidents.append(n)
        if len(incidents) > 2:
            for j in range(0,len(incidents)):
                for k in range(j+1,len(incidents)):
                    for l in range(k+1,len(incidents)):
                        vertex_clause += "-" + str((3*(j+1))+0) + " -" + str((3*(k+1))+0) + " -" + str((3*(l+1))+0) + " 0 \n"
                        vertex_clause += "-" + str((3*(j+1))+1) + " -" + str((3*(k+1))+1) + " -" + str((3*(l+1))+1) + " 0 \n"
                        vertex_clause += "-" + str((3*(j+1))+2) + " -" + str((3*(k+1))+2) + " -" + str((3*(l+1))+2) + " 0 \n"
                        clause_count += 3
    return vertex_clause

print(create_cnf())