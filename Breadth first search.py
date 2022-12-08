import ast
file_reader = open( r'D:\\DATA\\AI\\Python\\TASK 4\\BFS.txt', 'r' )
temp_data   = ast.literal_eval( file_reader.read( ) )
print (temp_data)
print ("Data type of object is:  {}".format(type(temp_data)))
visited = [] 
queue = []
def bfs(visited, temp_data, node): 
    visited.append(node)
    queue.append(node)
    while queue: 
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in temp_data[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, temp_data, '5') 