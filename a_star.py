
import heapq
WALL = '\033[91m█\033[0m'  # Red color
OPEN_SPACE = '\033[94m◌\033[0m'  # Blue color
START = '\033[92mS\033[0m'  # Green color
END = '\033[92mE\033[0m'  # Green color
PATH = '\033[92m◍\033[0m'  # Green color

def find_path_astar(maze, start_row, start_col, end_row, end_col, size):
    # Heuristic function for Manhattan distance
    def heuristic(row, col):
        return abs(row - end_row) + abs(col - end_col)

    open_set = [(0, heuristic(start_row, start_col), start_row, start_col)]  # Priority queue
    came_from = {}  # Store predecessors for path reconstruction
    g_score = {(start_row, start_col): 0}  # Cost from start to current cell
    f_score = {(start_row, start_col): heuristic(start_row, start_col)}  # Total estimated cost

    while open_set:
        current_f_score, _, current_row, current_col = heapq.heappop(open_set)

        if (current_row, current_col) == (end_row, end_col):
            # Reconstruct the path
            path = []
            while (current_row, current_col) in came_from:
                path.append((current_row, current_col))
                current_row, current_col = came_from[(current_row, current_col)]
            path.reverse()  # Start from the beginning
            return path

        for neighbor_row, neighbor_col in [(current_row - 1, current_col), (current_row + 1, current_col),
                                           (current_row, current_col - 1), (current_row, current_col + 1)]:
            if 0 <= neighbor_row < size and 0 <= neighbor_col < size and maze[neighbor_row][neighbor_col] != WALL and (neighbor_row, neighbor_col) not in came_from:
                tentative_g_score = g_score[(current_row, current_col)] + 1
                if (neighbor_row, neighbor_col) not in g_score or tentative_g_score < g_score[(neighbor_row, neighbor_col)]:
                    came_from[(neighbor_row, neighbor_col)] = (current_row, current_col)
                    g_score[(neighbor_row, neighbor_col)] = tentative_g_score
                    f_score[(neighbor_row, neighbor_col)] = tentative_g_score + heuristic(neighbor_row, neighbor_col)
                    heapq.heappush(open_set, (f_score[(neighbor_row, neighbor_col)], heuristic(neighbor_row, neighbor_col), neighbor_row, neighbor_col))

    return None  # No path found

