import copy

def position(state, agent):
    for i,sub_list in enumerate(state):
        if agent in sub_list:
            return(i,sub_list.index(agent))              
def up(state,y,x):
    if not((y-1) < 0):
        go_up = copy.deepcopy(state)
        go_up[y-1][x], go_up[y][x] = go_up[y][x], go_up[y-1][x]
        return go_up      
def left(state,y,x):
    if not((x-1) < 0):
        go_left = copy.deepcopy(state)
        go_left[y][x-1], go_left[y][x] = go_left[y][x], go_left[y][x-1]
        return go_left      
def down(state,y,x):
    if not((y+1) > len(state)-1):
        go_down = copy.deepcopy(state)
        go_down[y+1][x], go_down[y][x] = go_down[y][x], go_down[y+1][x]
        return go_down        
def right(state,y,x):
    if not((x+1) > len(state)-1):
        go_right = copy.deepcopy(state)
        go_right[y][x+1], go_right[y][x] = go_right[y][x], go_right[y][x+1]
        return go_right

def children(state):
    addchild = []
    y, x = position(state,':)') #row,col
            
    first_child = up(state,y,x) #UP
    if first_child:
        addchild.insert(0,first_child)
    sec_child = left(state,y,x) #LEFT 
    if sec_child:
        addchild.insert(0,sec_child)
    third_child = down(state,y,x) #DOWN 
    if third_child:
        addchild.insert(0,third_child)
    fourth_child = right(state,y,x) #RIGHT  
    if fourth_child:
        addchild.insert(0,fourth_child) 
    
    addchild.reverse()       # [UP,LEFT,DOWN,RIGHT]
    #random.shuffle(addchild) # Comment for specific action order
    return addchild