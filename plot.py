import matplotlib.pyplot as plt
import numpy as np

def plot_astar(depth_list_astar, time_astar, space_astar):
	depth_list_astar.reverse()
	time_astar.reverse()
	space_astar.reverse()
	
	x_astar=[] #depth
	y_astar=[] #time
	z_astar=[] #space
	x_astar.append(depth_list_astar[-1])
	y_astar.append(time_astar[-1])
	z_astar.append(space_astar[-1])
	for i in range(depth_list_astar[0]):
	    x_astar.append(i+1)
	    y_astar.append(time_astar[depth_list_astar.index(i)])
	    z_astar.append(space_astar[depth_list_astar.index(i)])
	    
	print('Depth to goal state: ',depth_list_astar[0], ', Nodes generated until goal state: ', time_astar[0],
	     'Nodes in memory: ',space_astar[0])
	fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(12,4))
	ax.plot(x_astar,y_astar,label='Time')
	ax.plot(x_astar,z_astar,label='Space')
	ax.grid()
	ax.set_title('Time Complexity')
	ax.set_xlabel('Depth')
	ax.set_ylabel('Nodes generated');
	ax.legend();
	plt.show();


def plot_dfs(depth_list_dfs, time_dfs, space_dfs):
	x_dfs=[] #depth
	y_dfs=[] #time
	z_dfs=[] #space
	for i in range(len(depth_list_dfs)-1):
	    if (depth_list_dfs[i] < depth_list_dfs[i+1]):
	        x_dfs.append(depth_list_dfs[i])
	        y_dfs.append(time_dfs[i])
	        z_dfs.append(space_dfs[i])
	        
	print('Depth to goal state: ',depth_list_dfs[-1], ', Nodes generated until goal state: ', time_dfs[-1], 
	      ', Nodes in memory: ', space_dfs[-1])
	fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(12,4))
	ax.plot(np.hstack([x_dfs,x_dfs[-1]+1]),np.hstack([y_dfs,time_dfs[-1]]),label='Time')
	ax.plot(np.hstack([x_dfs,x_dfs[-1]+1]),np.hstack([z_dfs,space_dfs[-1]]),label='Space')
	ax.grid()
	ax.set_title('Complexity')
	ax.set_xlabel('Depth')
	ax.set_ylabel('Nodes');
	ax.legend();
	plt.show();

def plot_bfs(depth_list_bfs, time_bfs, space_bfs):
	x_bfs=[] #depth
	y_bfs=[] #time
	z_bfs=[] #space
	for i in range(len(depth_list_bfs)-1):
	    if (depth_list_bfs[i] < depth_list_bfs[i+1]):
	        x_bfs.append(depth_list_bfs[i])
	        y_bfs.append(time_bfs[i])
	        z_bfs.append(space_bfs[i])
	        
	print('Depth to goal state: ',depth_list_bfs[-1], ', Nodes generated until goal state: ', time_bfs[-1], 
	      ', Nodes in memory: ', space_bfs[-1])
	fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(12,4))
	ax.plot(np.hstack([x_bfs,x_bfs[-1]+1]),np.hstack([y_bfs,time_bfs[-1]]),label='Time')
	ax.plot(np.hstack([x_bfs,x_bfs[-1]+1]),np.hstack([z_bfs,space_bfs[-1]]),label='Space')
	ax.grid()
	ax.set_title('Complexity')
	ax.set_xlabel('Depth')
	ax.set_ylabel('Nodes');
	ax.legend();
	plt.show();

def plot_ids(depth_list_ids, time_ids, space_ids):
	x_ids=[] #depth
	y_ids=[] #time
	z_ids=[] #space
	for i in range(len(depth_list_ids)-1):
	    if (depth_list_ids[i] < depth_list_ids[i+1]):
	        x_ids.append(depth_list_ids[i])
	        y_ids.append(time_ids[i])
	        z_ids.append(space_ids[i])
	        
	print('Depth to solution: ',depth_list_ids[-1], ', Time complexity: ', time_ids[-1],  
	      ', Space complexity: ', space_ids[-1])
	fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(12,4))
	ax.plot(np.hstack([x_ids,x_ids[-1]+1]),np.hstack([y_ids,time_ids[-1]]),label='Time')
	ax.plot(np.hstack([x_ids,x_ids[-1]+1]),np.hstack([z_ids,space_ids[-1]]),label='Space')
	ax.grid()
	ax.set_title('Complexity')
	ax.set_xlabel('limit')
	ax.set_ylabel('Past nodes');
	ax.legend();
	plt.show()

