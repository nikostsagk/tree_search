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

def dls(root,limit):    
    fringe = [] #A LIFO queue with the unexplored nodes
    visited = [] #A list with the visited nodes
    No_states = 0 #the number of past states w/o the root.
    
    time_complex = [0]
    space_complex = [0]
    all_depth_list = []
    
    Root = node(root,None,0,0)
    fringe.insert(0,Root)
    cutoff_occurred = False
    message, time, space, all_depth_list, limit,path,flag = recursive_dls(fringe,limit,visited,No_states,
                                                time_complex,space_complex,all_depth_list,cutoff_occurred)
    return message, time, space, all_depth_list, limit, path

def recursive_dls(fringe,limit,visited,No_states,time_complex,space_complex,all_depth_list,cutoff_occurred):
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
        return ('success', time_complex, space_complex, all_depth_list, limit, path,cutoff_occurred)
    elif (limit == 0):
        path = 0
        return ('cutoff', time_complex, space_complex, all_depth_list, limit, path,cutoff_occurred)
    else:
        if cutoff_occurred == False:
            explore = actions.children(cur_state.state)
            explore.reverse()
            for e in explore:
                if (e not in (visited or fringe)): # GRAPH
                #if (True == True): # TREE
                    child = node(e,cur_state,cur_state.depth+1,cur_state.cost+1)
                    fringe.append(child)
            
            time_complex.append(No_states)
            space_complex.append(len(fringe) + len(visited))
            all_depth_list.append(cur_state.depth)
            message, time, space, all_depth_list, limit, path,cutoff_occurred = recursive_dls(fringe,limit-1,
                                visited,No_states,time_complex,space_complex,all_depth_list,cutoff_occurred)
        if (message == 'cutoff'):
            path = 0
            cutoff_occurred = True
        elif (message == 'success'):
            return ('success', time_complex, space_complex, all_depth_list, limit, path,cutoff_occurred)
        if cutoff_occurred:
            return ('cutoff', time_complex, space_complex, all_depth_list, limit, path,cutoff_occurred)
        else:
            path = 0
            return ('failure', time_complex, space_complex, all_depth_list, limit, path,cutoff_occurred)
            
def ids(root):
    import sys
    nodes_generated = []
    nodes_memory = []
    for d in range(sys.maxsize):
        message, time, space, all_depth_list, limit, path = dls(root,d)
        if message == ('success' or 'failure'):
            #print('cutoff Limit: ',d)
            nodes_generated.append(time[-1]+nodes_generated[-1])
            return message, nodes_generated, space, all_depth_list, limit, path
        else:
            if d==0:
                nodes_generated.append(time[-1])
                nodes_memory.append(space[-1])
            else:
                nodes_generated.append(time[-1]+nodes_generated[-1])
                nodes_memory.append(space[-1])
            #print(message,'Limit: ',d)
message_ids, time_ids, space_ids, depth_list_ids, limit_4, path_ids = ids(root)

import plot
plot.plot_ids(depth_list_ids, time_ids, space_ids)
        