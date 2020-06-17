#import io 

#read in the string
xystring = input("Input the stringification:")
#xystring = "3,5,(1,1),(1,5),(2,4)"
#xystring = "2,2,(1,1)"

#remove the parenthesis, useless things
xystring = xystring.replace("(","")
xystring = xystring.replace(")","")

#split what remains
#Think of the whole list as pairs in a single list,
#where the first pair is the size of the rectangle
# and the following pairs are coordinates of blocks
xygrid = xystring.split(",")

#as is
height = int(xygrid[0])
width = int(xygrid[1])
size =  height * width

#a list to hold the blocks as tuples
blocks = []

#a variable to hold the number of clause lines
int_clause = 0

#dict to map coord to their index pairs
index_map = {}
count_in_grid = 0
for i in range (height):
    for j in range (width):
        x = 0 #holder if blocked
        if ((str(i+1),str(j+1)) not in blocks) : #if the coord is not blocked
            count_in_grid +=1 #count the coord
            x = count_in_grid #change holder
        index_map[(i+1,j+1)]=x #add the index counts to the map

#Put the blocks in the list
xholder = ""
for i in range(2,len(xygrid)):
    #hang on to even entries
    if i%2==0:
        xholder = xygrid[i]
    else:
        blocks.append((xholder,xygrid[i])) # pair even entries with odds as tuples

#helpful visualizer
def grid_as_string():
    grid_string = ""
    for i in range(1,height+1):
        for j in range(1,width+1):
            if ((str(i),str(j)) in blocks): #if it's a block, make a block
                grid_string += "█"
            else:
                grid_string+="+" #empties are +
        grid_string += "\r\n"

    return grid_string

#Variable for each square that is not a block
def number_of_vars():
    n = (size-len(blocks))
    return n

#2 clauses for each row
def number_of_clauses():
    n = ((width + height)*2)
    return n

#compile cnf piece by piece
def create_cnf():
    str_cnf = ""
    str_cnf += comments()
    str_cnf += pline()
    str_cnf += "c Row Clauses \n"
    str_cnf += row_clauses()
    str_cnf += "c Col Clauses \n"
    str_cnf += col_clauses()
    return str_cnf

def comments():
    str_comments = "\
c =========Grid of XY in every Row/Colum CNF========= \n\
c There is a variable for each open space, x_i, where i \n\
c begins at 0,0 and increase left to right, top to bottom.\n\
c There are two clauses for every row and column such \n\
c that there must be at least one true and one false x_i. \n"
    return str_comments

#construct p as p + type + #variable + #clauses
def pline():
    str_pline = "p cnf "
    str_pline += str(number_of_vars()) + " "
    str_pline += str(number_of_clauses()) + "\n"
    return str_pline

#create the clause line given the count & clause
def clause_line(str_clause):
    global int_clause
    int_clause += 1 # increase clause count
    str_full_clause =""
    #uncomment this line if you're using a non-heretical sat solver that uses line numbers
    #str_full_clause = str(int_clause) # begin the line with the number 
    str_full_clause += str_clause #add clause
    str_full_clause += " 0 \n" # close the line with 0 and newline
    return str_full_clause

def row_clauses():
    global index_map
    str_rows=""
    for i in range(height): #for each row
        row_string_1 = "" #hold the True clause
        row_string_0 = "" #hold the False clause
        for j in range(width): #for each index in the row
            var = index_map[(i+1,j+1)] #var is saved in the map
            if(var!=0): #if it's not blocked, add the clauses
                row_string_1 += " " + str(var)
                row_string_0 += " -" + str(var)
        #add the row data as clause line
        str_rows += clause_line(row_string_1) 
        str_rows += clause_line(row_string_0)
    return str_rows

def col_clauses():
    str_col = ""
    for i in range(width): #for each column
        #strings to hold column variables
        col_string_1 = ""
        col_string_0 = ""
        for j in range(height): #for each index in column
            var = index_map[(j+1,i+1)] #get the var from the map
            if(var!=(0,0)): #if not blocked
                #add indexes to their string
                col_string_1 += " " + str(var)
                col_string_0 += " -" + str(var)
        #convert to clause lines and add
        str_col += clause_line(col_string_1)
        str_col += clause_line(col_string_0)

    return str_col

def print_solution(s):
    big_s = s.split(" ") #split into variables
    position = 0 #hold position
    grid_string = "" 
    for i in range(1,height+1):
        for j in range(1,width+1):
            #walk through the whole grid
            #not only the first half of the list
            #infer that the positions are Y if not X
            if ((str(i),str(j)) in blocks):
                #if it's a block, add block
                grid_string += "█"
            else:
                if(int(big_s[position])<0):#if negative, add Y
                    grid_string += "Y"
                else:
                    grid_string += "X" #if positive, add X
                position+=1 #increment position
        grid_string += "\r\n" #return the string
    return grid_string

print(create_cnf())
print(grid_as_string())

solved = input("Enter solve (Vars only) or 'UNSAT':")

if solved != "UNSAT":
    print(print_solution(solved))
else:
    print("Unsatisfiable... but you knew that.")