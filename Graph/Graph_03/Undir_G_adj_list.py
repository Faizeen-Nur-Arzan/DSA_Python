def addEdge(adj, u, v, w):
    adj[u].append((v, w))
    adj[v].append((u, w))

def displayAdjList(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(f"{({j[0]}, {j[1]})} ", end="")
        print()

def main():
    V = 3
    adj = [[] for i in range(V)]

    # Now add edges one by one
    addEdge(adj, 1, 0, 4)
    addEdge(adj, 1, 2, 3)
    addEdge(adj, 2, 0, 1)

    print("Adjacency List Representation:")
    displayAdjList(adj)

    print("0.", "0" * 67, "67", sep="")

if __name__ == "__main__":
    main()