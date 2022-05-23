# Menu driven DFS BFS Using a Python dictionary to act as an adjacency list
flag = 0
def get_input():
    global flag
    flag = 1
    lst_size = int(input("Enter number of nodes"))
    vertexlst = []
    lst = {}
    for i in range(0,lst_size):
        vertexlst.append(input("Enter "+str(i+1)+" vertex"))
    for i in vertexlst:
        lst[i] = []
    for i in lst:
        inp = input(("Enter adjacent vertices of " + str(i))).split(" ")
        lst[i] = [] if '' in inp else inp
    
    return lst


def dfs(visited, graph, node):
    if node not in visited:
        print(node,end="->")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)



def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        

        
def driver():
    
    
    global graph
    global visited
    global queue
    
    
    
    print("""
    
    ***** Menu *****
    1. Input Graph
    2. Breadth First Search
    3. Depth First Search
    4. Exit
    """)
    
    option = int(input(" > "))
    
    
    
    if option == 1:
        graph = get_input()
        driver()
        
        
    if option == 2:
        if(not flag):
            print("Take Graph input first !!!")
            driver()
        else:
            visited = [] # List to keep track of visited nodes.
            queue = []     #Initialize a queue
            bfs(visited, graph, 'A')
            driver()
            
            
            
    if option == 3:
        if(not flag):
            print("Take Graph input first !!!")
            driver()
        else:
            visited = set() 
            dfs(visited, graph, 'A')
            driver()
            
            
    if option == 4:
        exit()

if _name_ == "_main_":
    graph = visited = queue = None
    driver()
