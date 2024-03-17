WALL = '\033[91m█\033[0m'  # Red color
OPEN_SPACE = '\033[94m◌\033[0m'  # Blue color
START = '\033[92mS\033[0m'  # Green color
END = '\033[92mE\033[0m'  # Green color
PATH = '\033[92m◍\033[0m'  # Green color

def find_path_value_iteration(maze, size):
    # Initialize values and state-action pairs
    values = [[0] * size for _ in range(size)]
    actions = [[None] * size for _ in range(size)]
    values[size - 1][size - 1] = 1  # Set end point value to 1

    # Define actions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Value iteration loop
    while True:
        delta = 0
        for row in range(size):
            for col in range(size):
                if maze[row][col] == WALL or (row == size - 1 and col == size - 1):
                    continue  # Skip walls and end point

                current_value = values[row][col]
                best_value = float('-inf')
                best_action = None

                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if 0 <= new_row < size and 0 <= new_col < size and maze[new_row][new_col] != WALL:
                        reward = -1  # Assume a negative step cost for moving
                        new_value = values[new_row][new_col] + reward
                        if new_value > best_value:
                            best_value = new_value
                            best_action = direction

                values[row][col] = best_value
                actions[row][col] = best_action
                delta = max(delta, abs(current_value - values[row][col]))

        if delta < 1e-4:  # Convergence threshold
            break

    # Trace the path from start to end
    path = []

    row, col = 0, 0
    while row != size - 1 or col != size - 1:
        action = actions[row][col]
        maze[row][col] = PATH  # Mark the path
        path.append((row, col))
        row += action[0]
        col += action[1]

    maze[size - 1][size - 1] = END  # Mark the end point
    return path

