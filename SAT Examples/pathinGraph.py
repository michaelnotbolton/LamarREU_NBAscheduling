#read in graph as string

g = {0: [1, 2, 3, 4, 5, 6], 1: [0, 2, 3, 4, 5, 6], 2: [0, 1], 3: [0, 1], 4: [0, 1], 5: [0, 1], 6: [0, 1]}
#max k is 5

#g = {0: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], 1: [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], 2: [0, 1], 3: [0, 1], 4: [0, 1], 5: [0, 1], 6: [0, 1], 7: [0, 1], 8: [0, 1], 9: [0, 1], 10: [0, 1], 11: [0, 1], 12: [0, 1], 13: [0, 1], 14: [0, 1], 15: [0, 1], 16: [0, 1], 17: [0, 1], 18: [0, 1], 19: [0, 1], 20: [0, 1], 21: [0, 1], 22: [0, 1], 23: [0, 1], 24: [0, 1], 25: [0, 1], 26: [0, 1], 27: [0, 1], 28: [0, 1], 29: [0, 1], 30: [0, 1], 31: [0, 1]}
#max k i s 5

#g = {0: [1, 2, 3, 4, 5, 6, 7], 1: [0, 2, 3, 4, 5, 6, 7], 2: [3, 4, 0, 1], 3: [2, 4, 0, 1], 4: [2, 3, 0, 1], 5: [6, 7, 0, 1], 6: [5, 7, 0, 1], 7: [5, 6, 0, 1]}
#max k is 8

#g = {0: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], 1: [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], 2: [3, 4, 0, 1], 3: [2, 4, 0, 1], 4: [2, 3, 0, 1], 5: [6, 7, 0, 1], 6: [5, 7, 0, 1], 7: [5, 6, 0, 1], 8: [9, 10, 0, 1], 9: [8, 10, 0, 1], 10: [8, 9, 0, 1], 11: [12, 13, 0, 1], 12: [11, 13, 0, 1], 13: [11, 12, 0, 1], 14: [15, 16, 0, 1], 15: [14, 16, 0, 1], 16: [14, 15, 0, 1], 17: [18, 19, 0, 1], 18: [17, 19, 0, 1], 19: [17, 18, 0, 1], 20: [21, 22, 0, 1], 21: [20, 22, 0, 1], 22: [20, 21, 0, 1], 23: [24, 25, 0, 1], 24: [23, 25, 0, 1], 25: [23, 24, 0, 1], 26: [27, 28, 0, 1], 27: [26, 28, 0, 1], 28: [26, 27, 0, 1], 29: [30, 31, 0, 1], 30: [29, 31, 0, 1], 31: [29, 30, 0, 1], 32: [33, 34, 0, 1], 33: [32, 34, 0, 1], 34: [32, 33, 0, 1], 35: [36, 37, 0, 1], 36: [35, 37, 0, 1], 37: [35, 36, 0, 1]}
#max k is 11

#k = input("k many edges:")

v_to_e_map = {}
edges = {}
edge_counter = 0
for key in g.keys():
    for v in g[key]:
        if (not (((key,v) in edges) or ((v,key) in edges))):
            edge_counter +=1
            edges.update({(key,v):str(edge_counter)})

print(edges)
        
    