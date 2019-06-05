import sys
import copy
import random
import numpy as np
sys.setrecursionlimit(100000)
import actions
root = [['0','0','0','0'],['0','0','0','0'],['0','0','0','0'],['A','B','C',':)']]


class node(): 
    def __init__(self, state,parent,depth,cost):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost

def goal(node):
    if ((node.state[1][1] == 'A') and (node.state[2][1] == 'B') and (node.state[3][1] == 'C')):
        return True
    return False

def dfs(root):
    fringe = [] #A LIFO queue with the unexplored nodes
    visited = [] #A list with the visited nodes
    No_states = 0 #the number of past states w/o the root.
    
    time_complex = [0]
    space_complex = [0]
    all_depths_list = []
    
    Root = node(root,None,0,0)
    fringe.insert(0,Root)
    
    while fringe:
        cur_state = fringe.pop()
        No_states = No_states + 1
        visited.append(cur_state.state) #comment for tree, uncomment for graph
        
        #print('Depth: ',cur_state.depth) #Prints current node. (Mute it unless you want to verify corectness).
        #print('Current node: No.',No_states,'\n',cur_state.state[0],'\n',cur_state.state[1], \
        #         '\n',cur_state.state[2],'\n',cur_state.state[3])
        
        
        if goal(cur_state):
            final = cur_state
            path = []
            path.insert(0,final.state)
            while(final.parent != None):
                path.insert(0,final.parent.state)
                final = final.parent
            return ('success', time_complex, space_complex, all_depths_list,path)
        
        explore = actions.children(cur_state.state)  # returns unexpanded children
        explore.reverse()
        for e in explore:
            if (e not in (visited or fringe)): # GRAPH
            #if (True == True): # TREE
                child = node(e,cur_state,cur_state.depth+1,cur_state.cost+1)
                fringe.append(child)
                
        time_complex.append(No_states)
        space_complex.append(len(fringe) + len(visited))
        all_depths_list.append(cur_state.depth)
    return ('failure', time_complex, space_complex, all_depths_list,path)

message_dfs, time_dfs, space_dfs, depth_list_dfs, path_dfs = dfs(root)

import plot
plot.plot_dfs(depth_list_dfs, time_dfs, space_dfs)
