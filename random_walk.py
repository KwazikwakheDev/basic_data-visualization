from random import choice
class RandomWalk:
     #This is a class to generate random walks

     def __init__(self, num_points = 5000):
          
          self.num_points = num_points

          self.x_values = [0]
          self.y_values = [0]

def fill_walk(self):
     while len(self.x_values) < self.num_points:
          x_direction = choice(1, -1)

          x_distance = choice(0, 1, 2, 3, 4)
          x_step = x_direction * x_distance

