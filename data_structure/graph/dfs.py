from collections import deque 

''' The DFS recursive ,
#Time  compelxity O(V+E) 
# Space complecity O(V) Depth of call stack '''

def dfs_recursive(undirected_graph,start,seen):

    ''' if start not in seen:
        raise ValueError("Vertex not found")'''

    seen.append(start)
    neighbors = undirected_graph[start]

    for nei  in neighbors:
        if nei not in seen:
            dfs_recursive(undirected_graph,nei,seen)
    #print(seen)
    return seen


def iterative_dfs(ug,start):

    visited =[]
    stack =[start]
    #stack.append(start)

    while stack :
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            neighbors = ug[node]
            print(neighbors)
            for nei in neighbors:
                if nei not in visited :
                    stack.append(nei)
    return visited



if __name__ == '__main__':
    # ref: Sedgewick Algorithms 4th edition, page 532
    ug = {
        0: [2, 1, 5],
        1: [0, 2],
        2: [0, 1, 3, 4],
        3: [5, 4, 2],
        4: [3, 2],
        5: [3, 0]
    }

    start = 0
    result_visited_nodes = []
    print(f"dfs traversal recursive: ")
    #print(dfs_recursive(ug, start, result_visited_nodes))  # output: [0, 2, 1, 3, 5, 4]


    print("")
    print(f"dfs traversal iterative: ")
    print(iterative_dfs(ug, start))