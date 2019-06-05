import sys
import copy
import random
import numpy as np
import actions
sys.setrecursionlimit(100000)

root = [['0','0','0','0'],['0','0','0','0'],['0','0','0','0'],['A','B','C',':)']]

def goal(node):
    if ((node.state[1][1] == 'A') and (node.state[2][1] == 'B') and (node.state[3][1] == 'C')):
        return True
    return False

class node_astar(): 
    def __init__(self, state,parent,depth,hcost,gcost):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.fcost = hcost + gcost
        
def score_calc(state):
    ay, ax = np.where(np.array(state)=='A')
    by, bx = np.where(np.array(state)=='B')
    cy, cx = np.where(np.array(state)=='C')
    return manhattan(ay, ax, by, bx, cy, cx, 4, 1)
        
def children_astar(state):
    addchild = []
    add_hscore = []
    y, x = actions.position(state,':)') #row,col
            
    first_child = actions.up(state,y,x) #UP
    if first_child:
        h_score = score_calc(first_child)        
        add_hscore.append(h_score)
        addchild.append(first_child)
    sec_child = actions.left(state,y,x) #LEFT 
    if sec_child:       
        h_score = score_calc(sec_child)        
        add_hscore.append(h_score)
        addchild.append(sec_child)
    third_child = actions.down(state,y,x) #DOWN 
    if third_child:
        h_score = score_calc(third_child)        
        add_hscore.append(h_score)
        addchild.append(third_child)
    fourth_child = actions.right(state,y,x) #RIGHT 
    if fourth_child:
        h_score = score_calc(fourth_child)
        add_hscore.append(h_score)
        addchild.append(fourth_child) 
    
    # [UP,LEFT,DOWN,RIGHT]
    return (addchild,add_hscore)

def manhattan(ay, ax, by, bx, cy, cx, dy, dx):
    ay_tr,ax_tr = 1,1;
    by_tr,bx_tr = 2,1;
    cy_tr,cx_tr = 3,1;
    
    distance = abs(ay - ay_tr) + abs(ax - ax_tr) + abs(by - by_tr) + abs(bx - bx_tr) + \
                abs(cy - cy_tr) + abs(cx - cx_tr)

    return int(distance)

def recursive_astar(root):
    fringe = [] #A LIFO queue with the unexplored nodes
    visited = [] #A list with the visited nodes
    No_states = 0 #the number of past states w/o the root.
    time_complex = [0]
    space_complex = [0]
    all_depth_list = []
    
    Root = node_astar(root,None,0,5,0)
    fringe.insert(0,Root)

    message, time, space, depth_list, path = a_star(fringe,No_states,time_complex,space_complex, all_depth_list,visited)
    return (message, time, space, depth_list, path)
    
def a_star(fringe,No_states,time_complex,space_complex,all_depth_list,visited):
    cur_state = fringe.pop()
    No_states = No_states + 1
    #visited.append(cur_state.state) #comment for tree, uncomment for graph
    
    #print('Depth: ',cur_state.depth) #Prints current node. (Mute it unless you want to verify corectness).
    #print('Cost: ',cur_state.fcost)
    #print('Current node: No.',No_states,'\n',cur_state.state[0],'\n',cur_state.state[1],'\n',cur_state.state[2],'\n',cur_state.state[3])
        
    if goal(cur_state):
        time_complex.append(No_states)
        space_complex.append(len(fringe)+len(visited))
        all_depth_list.append(cur_state.depth)
        final = cur_state
        path = []
        path.insert(0,final.state)
        while(final.parent != None):
            path.insert(0,final.parent.state)
            final = final.parent
        return ('success', time_complex, space_complex, all_depth_list,path)
        
    successors, succ_hscores = children_astar(cur_state.state)
    if (successors == []):
        return ('failure', time_complex, space_complex, all_depth_list, path)
    for i,e in enumerate(successors):
        if e not in visited:
            child = node_astar(e,cur_state,cur_state.depth+1,succ_hscores[i],cur_state.depth+1)
            fringe.append(child)
            
    fringe = sorted(fringe, key=lambda x: x.fcost, reverse=True)
    fringe = list(fringe);
    
    time_complex.append(No_states)
    space_complex.append(len(fringe)+len(visited))
    all_depth_list.append(cur_state.depth)
    message, time, space, depth_list, path = a_star(fringe,No_states,time_complex,space_complex, all_depth_list,visited)
    return message, time, space, depth_list, path
 


message_astar, time_astar, space_astar, depth_list_astar, path_astar = recursive_astar(root)
import plot
plot.plot_astar(depth_list_astar, time_astar, space_astar)