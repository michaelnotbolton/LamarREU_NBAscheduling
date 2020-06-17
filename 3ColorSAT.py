#read in string
#graphstring = input("Input:")
graphstring = "{0: [1, 2], 1: [0, 2], 2: [0, 1]}"

graph = exec(graphstring)

print(graph)
keys = graph.keys()

keyparents = {key:0 for k in keys}
for k in keys:
    for child in graphstring[k]:
        keyparents[k] = child


#def number_of_vars():
    #number of edges

print(keyparents)
