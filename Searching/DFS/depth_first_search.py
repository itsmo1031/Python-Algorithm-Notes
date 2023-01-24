example = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

''' Depth-First Search (DFS) '''


def dfs(graph, start, visited):
    print(start, end=' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False] * 9

dfs(example, 1, visited)

'''
[Output Example]
1 2 7 6 8 3 4 5
'''
