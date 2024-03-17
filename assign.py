#Maze generation code
#https://github.com/kunaltyagi760/Terminal_based_Maze_Solver/blob/main/solve_maze.py

import copy
import random
import time
from a_star import find_path_astar
from bfs import find_path_bfs
from dfs import find_path_dfs
from mdp_value import find_path_value_iteration
from mdp_policy import find_path_policy_iteration
import psutil
# Constants for maze ch aracters
WALL = '\033[91m█\033[0m'  # Red color
OPEN_SPACE = '\033[94m◌\033[0m'  # Blue color
START = '\033[92mS\033[0m'  # Green color
END = '\033[92mE\033[0m'  # Green color
PATH = '\033[92m◍\033[0m'  # Green color

def generate_maze(n, wall_percentage=25):
    
    # Generates a random maze of size n x n with walls and open spaces.

    # Parameters:
    #  n: Size of the maze.
    #  wall_percentage: Percentage of walls in the maze.

    # Returns:
    #  The generated maze as a 2D list.
    
    maze = [[OPEN_SPACE] * n for _ in range(n)]

    # Add walls
    num_walls = int((wall_percentage / 100) * (n * n))
    for _ in range(num_walls):
        
        row, col = random.randint(0, n - 1), random.randint(0, n - 1)
        maze[row][col] = WALL

    # Set start and end points
    maze[0][0] = START
    maze[n - 1][n - 1] = END

    return maze

def print_maze(maze):
    
    # Prints the maze in the terminal.

    # Parameters:
    #  maze: The maze to be printed.
    
    for row in maze:

        # colored_str string is printed before and after every row of maze to enhance maze representation in terminal alse maze cell is clearly visible.

        colored_str = (('\033[91m' + "+---" + '\033[0m') * len(maze)) + '\033[91m' + "+" + '\033[0m'
        print(colored_str)
        for cell in row:
            print("|", end=" ")
            print(cell, end=" ")
        print("|", end=" ")
        print()
    print(colored_str)

def main():
        while True:
            try:
                n = int(input("Enter the size of the maze (n x n): "))
                if n <= 1:
                    raise ValueError
                break
            except ValueError:
                print("\nInvalid input, Please enter the size of maze (n x n) > 1")

        maze = generate_maze(n)
        print("\nGenerated Maze:")
        print_maze(maze)
        gen_maze = copy.deepcopy(maze) 

        while True:
            user_choice = input("\n1. Print the BFS path\n2. Print DFS path\n3. Print A*\n4. Print the Value iteration path\n5. Print the Value Policy path\nEnter your choice(1/2/3/4/5): ")

            try:
                path, memory_usage, total_time = find_path_and_measure_memory(user_choice, gen_maze, n)
                if path is None:
                    print(f"\nNo path found for {user_choice}")
                    continue

                if path:
                    mark_path(gen_maze, path, PATH)
                    print(f"\nMaze with {user_choice} Path:")
                    print_maze(gen_maze)
                else:
                    print(f"\nNo path found for {user_choice}")

                print(f"Time taken: {total_time:.4f} seconds")
                print(f"Memory usage: {memory_usage:.2f} MB")
            except Exception as e:  # Catch any unexpected errors
                print(f"An error occurred: {e}")

        # Allow user to continue or exit
            choice = input("\nDo you want to try another algorithm? (y/n): ")
            if choice.lower() != 'y':
                break
def mark_path(maze, path, char):
    for row, col in path:
        maze[row][col] = char

def find_path_and_measure_memory(algo_choice, maze, n):

    process = psutil.Process()
    start_memory = process.memory_info().rss / 1024 / 1024  # Initial memory usage (MB)

    start_time = time.time()
    if algo_choice == '1':
        path = find_path_bfs(maze, 0, 0, n - 1, n - 1)
    elif algo_choice == '2':
        path = find_path_dfs(maze, 0, 0, n - 1, n - 1)
    elif algo_choice == '3':
        path=find_path_astar(maze, 0, 0, n - 1, n - 1,n)
    elif algo_choice == '4':
        path=find_path_value_iteration(maze,n)
    elif algo_choice == '5':
        path=find_path_policy_iteration(maze,n)
    else:
        print(f"Invalid algorithm choice: {algo_choice}")
        return None, None

    end_memory = process.memory_info().rss / 1024 / 1024  # Memory usage after pathfinding
    end_time = time.time()
    total_time = end_time - start_time
    memory_usage = end_memory - start_memory

    return path, memory_usage, total_time
main()
