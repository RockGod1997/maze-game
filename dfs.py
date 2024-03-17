WALL = '\033[91m█\033[0m'  # Red color
OPEN_SPACE = '\033[94m◌\033[0m'  # Blue color
START = '\033[92mS\033[0m'  # Green color
END = '\033[92mE\033[0m'  # Green color
PATH = '\033[92m◍\033[0m'  # Green color

def find_path_dfs(maze, start_row, start_col, end_row, end_col):

    n = len(maze)
    visited = [[False] * n for _ in range(n)]
    stack = [(start_row, start_col, [])]

    while stack:
        cur_row, cur_col, path = stack.pop()

        if cur_row == end_row and cur_col == end_col:
            return path + [(cur_row, cur_col)]

        if visited[cur_row][cur_col]:
            continue

        visited[cur_row][cur_col] = True

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = cur_row + dr, cur_col + dc
            if 0 <= new_row < n and 0 <= new_col < n and maze[new_row][new_col] != WALL:
                stack.append((new_row, new_col, path + [(cur_row, cur_col)]))

    return None  # No path found

