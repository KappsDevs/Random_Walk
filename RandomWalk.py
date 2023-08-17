import matplotlib.pyplot as plt
import random



# E = EXIT 
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 'E', 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]  


def possible_directions(x,y):
    
    directions = []

    if maze[x+1][y] != 1:
        directions.append((1,0))
    
    if maze[x-1][y] != 1:
        directions.append((-1,0))
    
    if maze[x][y + 1] != 1:
        directions.append((0,1))

    if maze[x][y - 1] != 1:
        directions.append((0,-1))

    return directions


#THE RANDOM WALK FUNCTION
def random_walk():
    x = 1
    y = 1


              # in N steps
    for paces in range(1000):   

        possible_ways = possible_directions(x,y)

        dx,dy = random.choice(possible_ways)

        x = x + dx          # dx, dy -> variation of movement 
        y = y + dy

        if maze[x][y] == 'E':
            print(f"Completed in {paces} steps")
            print("Exit")
            return
        
        
        
    print("Unable to find the exit.")
        

        
random_walk()



