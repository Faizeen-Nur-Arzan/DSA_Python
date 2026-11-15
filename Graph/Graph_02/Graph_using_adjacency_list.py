# Function to add an edge between two vertices
def addEdge(adj, u, v):
    adj[u].append(v)

def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(f"{j} ", end="")
        print()

def main():
    # Create a graph with 3 vertices and 3 edges
    V = 3
    adj = [[] for _ in range(V)]

    # Now add edges one by one
    addEdge(adj, 1, 0)
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 0)

    print("Adjacency List Representation:")
    display_adj_list(adj)

if __name__ == "__main__":
    main()