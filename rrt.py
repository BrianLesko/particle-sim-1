# Brian Lesko
# 1/17/2024
# RRT Class

import numpy as np 

class RRT:
    def __init__(self, start, goal):
        self.n = len(start) # n is the dimension of the space
        self.start = start
        self.goal = goal
        self.nodes = [self.start]  # Use list for dynamic appending
        self.node_x = [start[0]]
        self.node_y = [start[1]]
        self.edges = []  # Store edges as tuples (parent, child)

    def get_x_sample(self):
        self.x_sample = 6*np.random.uniform(-1, 1, self.n)
        return self.x_sample
    
    def get_nearest_node(self, x_sample):
        distances = np.linalg.norm(self.nodes - x_sample, axis=1)
        nearest_index = np.argmin(distances)
        return nearest_index
    
    def get_x_new(self, x_nearest, x_sample, max_step = .888):
        vector = x_sample - x_nearest
        distance = np.linalg.norm(vector)
        step_size = min(max_step, distance)*np.random.normal(.777, (0.9 - 0.5) / (2 * 0.675))
        step = step_size * vector / distance
        self.x_new = x_nearest + step
        return self.x_new
    
    def check_collision(self, x_new):
        self.nodes.append(self.x_new)
        self.node_x.append(self.x_new[0])
        self.node_y.append(self.x_new[1])
        #self.paths.append(self.x_new_path)
        return False
    
    def halton(index, base):
        fraction = 1
        result = 0
        while index > 0:
            fraction /= base
            result += fraction * (index % base)
            index //= base  # floor division
        return result
    


        