import numpy as np
WALL = '\033[91m█\033[0m'  # Red color
OPEN_SPACE = '\033[94m◌\033[0m'  # Blue color
START = '\033[92mS\033[0m'  # Green color
END = '\033[92mE\033[0m'  # Green color
PATH = '\033[92m◍\033[0m'  # Green color

def find_path_policy_iteration(maze, size):
    # Define MDP components
    states = [(row, col) for row in range(size) for col in range(size)]
    actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, right, down, left
    rewards = np.zeros((size, size))
    rewards[size - 1, size - 1] = 1  # Reward at the goal state
    discount_factor = 0.9

    # Define transition probabilities (adjust for walls and boundaries)
    transition_probabilities = np.zeros((size, size, len(actions), size, size))
    for row in range(size):
        for col in range(size):
            for action_index, action in enumerate(actions):
                new_row = min(size - 1, max(0, row + action[0]))
                new_col = min(size - 1, max(0, col + action[1]))

                if maze[new_row][new_col] != WALL:
                    transition_probabilities[row, col, action_index, new_row, new_col] = 1

    # Initialize policy (random actions)
    policy = np.random.choice(len(actions), size * size).reshape(size, size)

    # Policy iteration loop
    while True:
        # Policy evaluation
        value_function = np.zeros((size, size))
        policy_stable = True

        while True:
            new_value_function = np.zeros((size, size))
            for row in range(size):
                for col in range(size):
                    action_index = policy[row, col]
                    for new_row in range(size):
                        for new_col in range(size):
                            transition_prob = transition_probabilities[row, col, action_index, new_row, new_col]
                            new_value_function[row, col] += transition_prob * (rewards[new_row, new_col] + discount_factor * value_function[new_row, new_col])

            if np.allclose(value_function, new_value_function):
                break

            value_function = new_value_function

        # Policy improvement
        policy_stable = True
        for row in range(size):
            for col in range(size):
                best_action_index = None
                best_action_value = float('-inf')
                for action_index in range(len(actions)):
                    action_value = 0
                    for new_row in range(size):
                        for new_col in range(size):
                            transition_prob = transition_probabilities[row, col, action_index, new_row, new_col]
                            action_value += transition_prob * (rewards[new_row, new_col] + discount_factor * value_function[new_row, new_col])

                    if action_value > best_action_value:
                        best_action_index = action_index
                        best_action_value = action_value

                if policy[row, col] != best_action_index:
                    policy_stable = False
                    policy[row, col] = best_action_index

        if policy_stable:
            break

    # Extract path from policy
    path = []
    row, col = 0, 0
    while (row, col) != (size - 1, size - 1):
        path.append((row, col))
        action = actions[policy[row, col]]
        row += action[0]
        col += action[1]

    return path
