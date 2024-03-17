import matplotlib.pyplot as plt
#algorithms={'BFS':0.0004,'DFS':0.0002,'A*':0.0003,'MDP_Value':0.0009,'MDP_Policy':0.2636} #5X5 maze
#algorithms={'BFS':0.0008,'DFS':0.0004,'A*':0.0018,'MDP_Value':0.0027,'MDP_Policy':6.219} #10x10 maze
#algorithms={'BFS':0.0007,'DFS':0.0024,'A*':0.0010,'MDP_Value':0.0208,'MDP_Policy':182.7114 } #20x20 maze
algorithms={'BFS':0.0009,'DFS':0.0028,'A*':0.007,'MDP_Value':0.0343,'MDP_Policy':521.1964} #25x25 maze
sorted_algorithms = sorted(algorithms, key=algorithms.get)

# Extract sorted algorithms and times
algorithms_list = list(sorted_algorithms)
times_list = [algorithms[algorithm] for algorithm in algorithms_list]

plt.figure(figsize=(10, 6))  # Set plot dimensions
plt.plot(algorithms_list, times_list, marker='o', linestyle='-')  # Plot line with markers
plt.xlabel("Algorithm")
plt.ylabel("Time (seconds)")
plt.title("Time Taken by Each Algorithm for maze 25x25")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()