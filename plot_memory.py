import matplotlib.pyplot as plt
#algorithms={'BFS':0.14,'DFS':1.11,'A*':0.72,'MDP_Value':0.56,'MDP_Policy':4.44} #10x10 maze
#algorithms={'BFS':0.08,'DFS':1.98,'A*':0.83,'MDP_Value':0.5,'MDP_Policy':6.52} #20x20 maze
algorithms={'BFS':0.14,'DFS':2.70,'A*':0.86,'MDP_Value':0.61,'MDP_Policy':6.14} #25x25 maze
sorted_algorithms = sorted(algorithms, key=algorithms.get)

# Extract sorted algorithms and times
algorithms_list = list(sorted_algorithms)
memory_list = [algorithms[algorithm] for algorithm in algorithms_list]

plt.figure(figsize=(10, 6))  # Set plot dimensions
plt.plot(algorithms_list, memory_list, marker='o', linestyle='-')  # Plot line with markers
plt.xlabel("Algorithm")
plt.ylabel("Memory (MB)")
plt.title("Memory consumed by Each Algorithm for maze 25x25")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()