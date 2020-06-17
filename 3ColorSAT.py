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