import numpy as np

graph_list = [[0, 4, 0, 3, 0, 0, 0, 0],
              [4, 0, 3, 1, 8, 5, 0, 0],
              [0, 3, 0, 0, 7, 6, 0, 0],
              [3, 1, 0, 0, 3, 3, 6, 0],
              [0, 8, 7, 3, 0, 2, 5, 0],
              [0, 5, 6, 3, 2, 0, 3, 4],
              [0, 0, 0, 6, 5, 3, 0, 7],
              [0, 0, 0, 0, 0, 4, 7, 0]]


def dijkstra(graph, src):
    # init
    visited = []
    distance = {src: 0}
    node = list(range(len(graph[0])))
    if src in node:
        node.remove(src)
        visited.append(src)
    else:
        return None
    for i in node:
        distance[i] = graph[src][i]
    prefer = src
    while node:
        _distance = float('inf')
        for i in visited:
            for j in node:
                if graph[i][j] > 0:
                    if _distance > distance[i] + graph[i][j]:
                        _distance = distance[j] = distance[i] + graph[i][j]
                        prefer = j
        visited.append(prefer)
        node.remove(prefer)
    return distance


if __name__ == '__main__':
    distance = dijkstra(graph_list, 0)
    print(distance)