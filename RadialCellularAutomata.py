import numpy as np
import matplotlib.pyplot as plt
import math


r = 3		# Radius
grid_width = 64
grid_height = 64
numGP = grid_width * grid_height

live_grid = np.random.randint(2,size=(grid_width,grid_height))
#live_grid = np.ones((grid_width,grid_height))
mask_grid = np.zeros((grid_width,grid_height))

print(live_grid)

num_iters = 50

relative_GP = []

mask_grid[:r,:] = 1
mask_grid[-r:,:] = 1
mask_grid[:,:r] = 1
mask_grid[:,-r:] = 1

inner_origin = (r,r)
d = np.linspace(-r,+r,(2*r)+1,dtype=np.int16)


def rule1(pattern):
	A = pattern[:len(pattern)//2]
	B = pattern[len(pattern)//2:]
	A_sum = np.sum(np.asarray(A, dtype=np.int16))
	B_sum = np.sum(np.asarray(B, dtype=np.int16))
	if A_sum > B_sum:
		return 1
	else:
		return 0


for i in d:
	for j in d:
		dis = math.sqrt((i-0) ** 2 + (j-0) ** 2)
		if dis <= r:
			relative_GP.append([i,j])


for iteration in range(num_iters):
	patterns = []
	for j in range(grid_height):
		for i in range(grid_width):
			pattern = []
			if mask_grid[i][j] == 1: # Do boundary conditional
				for i_sub,j_sub in relative_GP:
					di = i+i_sub
					dj = j+j_sub
					if di >= 0 and di < grid_width and dj >= 0 and dj < grid_height:
						pattern.append(str(live_grid[di,dj]))
					else:
						pattern.append('0')
			else: # slight optimization
				for i_sub,j_sub in relative_GP:
						pattern.append(str(live_grid[i+i_sub,j+j_sub]))
			str_pattern = ''.join(pattern)
			patterns.append(str_pattern)


	new_grid = np.copy(live_grid).flatten()
	for idx,pattern in enumerate(patterns):
		new_val = rule1(pattern)
		new_grid[idx] = new_val

	plt.imshow(live_grid)
	plt.pause(0.5)

	live_grid = np.reshape(new_grid, (grid_width, grid_height))

plt.show()