import random
from string import ascii_uppercase

def prima(W, city_labels = None):

    _ = float('inf')
    cities_count = len(W)

    for weights in W:
        assert len(weights) == cities_count

    if not city_labels:
        city_labels = [ascii_uppercase[x] for x in range(cities_count)]

    assert cities_count <= len(city_labels)

    free_vertexes = list(range(0, len(city_labels)))

    starting_vertex = random.choice(free_vertexes)
    tied = [starting_vertex]
    free_vertexes.remove(starting_vertex)

    print('Started with %s' % city_labels[starting_vertex])

    road_length = 0

    while free_vertexes:
        min_link = None  
        overall_min_path = _    

        for current_vertex in tied:
            weights = W[current_vertex]  

            min_path = _
            free_vertex_min = current_vertex

            for vertex in range(cities_count):
                vertex_path = weights[vertex]
                if vertex_path == 0:
                    continue

                if vertex in free_vertexes and vertex_path < min_path:
                    free_vertex_min = vertex
                    min_path = vertex_path

            if free_vertex_min != current_vertex:
                if overall_min_path > min_path:
                    min_link = (current_vertex, free_vertex_min)
                    overall_min_path = min_path
        try:
            path_length = W[min_link[0]][min_link[1]]
        except TypeError:
            print('Unable to find path')
            return

        print('Connecting %s to %s [%s]' % (city_labels[min_link[0]], city_labels[min_link[1]], path_length))

        road_length += path_length
        free_vertexes.remove(min_link[1])
        tied.append(min_link[1])

    print('Road length: %s' % road_length)


if __name__ == '__main__':

    _ = float('inf')

    W = [
     
        [_, 4, _, 3, _, _, _, _], 
        [4, _, 3, 1, 8, 5, _, _], 
        [_, 3, _, _, 7, 6, _, _], 
        [3, 1, _, _, 3, 3, 6, _], 
        [_, 8, 7, 3, _, 2, 5, _], 
        [_, 5, 6, 3, 2, _, 3, 4], 
        [_, _, _, 6, 5, 3, _, 7],
        [_, _, _, _, _, 4, 7, _],
    ]

    prima(W)