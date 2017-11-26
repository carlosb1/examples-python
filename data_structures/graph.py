def find_path(graph, start, end, path= []):
    path = path + [start]
    #is it the path
    if start == end:
        return path
    #no, has more graphs to visit
    if not graph.has_key(start):
        return None

    #has graphs, search adjs
    for node in graph[start]:
        #if it is not included, search there
        if node not in path:
            newpath = find_path(graph,node,end,path)
            if newpath: return newpath
    return None



def bfs(grap, start,end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in graph.get(node,[]):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)




graph = {'A': ['B','C'],
        'B': ['G','C','D'],
         'C': ['D'],
         'D': ['C','E'],
         'E': ['F'],
         'F': ['C'],
         'G': []
         }

result_path = find_path(graph,'A','D')
print str(result_path)

result_path_v2 = bfs(graph,'A','G')
print str(result_path_v2)
