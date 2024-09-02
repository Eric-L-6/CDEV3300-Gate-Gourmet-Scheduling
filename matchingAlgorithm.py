# After parsing: Will have:
# A skills matrix for all employees
# A list of available employees
# A list of shifts and required 
from collections import deque

SOURCE = 'SOURCE_NODE';
SINK = 'SINK_NODE';


taskTypes = ['one', 'two']
skillsMatrix = {'a': {'one': True, 'two': False}, 'b': {'one': False, 'two': False}, 'c': {'one': False, 'two': True}}
availableEmplyees = ['a', 'b', 'c']
unavailableEmployees = []

# shift need to 
dailyShift = [start time['one'], ['two'], ['one', 'two']]



# potentially: Precalculate the priority of each shift???
# based on how many employees can perform the shift
# OR based on how many available employees cna perform the shift?????????????????????

def getPriority(tasks):
    return len(tasks)

def elegible(employee, tasks):
    for task in tasks:
        if not skillsMatrix[employee][task]:
            return False
    
    return True

def createBipartiteGraph():
    graph = {}
    graph[SOURCE] = {}
    graph[SINK] = {}

    for employee in availableEmplyees:
        graph[employee] = {}
        graph[SOURCE][employee] = 1

    for shift in range(len(dailyShift)):
        graph[shift] = {}
        graph[shift][SINK] = 1
    
    for employee in availableEmplyees:
        for shift, tasks in enumerate(dailyShift):
            if elegible(employee, tasks):
                graph[employee][shift] = 1 * getPriority(tasks)
                graph[shift][employee] = 0

    return graph

# need the edmonds karp algorithm
def edmonds_karp(graph):
    parent = {}
    shift_match = [None for _ in range(len(dailyShift))]

    def bfs(graph):
        visited = set()
        queue = deque([SOURCE])
        visited.add(SOURCE)

        while queue:
            node = queue.popleft()

            print(f"visiting {node}")

            for neighbhor in graph[node]:
                if neighbhor not in visited and graph[node][neighbhor] > 0: # residual capacity
                    queue.append(neighbhor)

    def bfs_prioritised(graph):
        visited = set()
        queue = deque([SOURCE])

        while queue:
            node = queue.popleft()

            if node in visited:
                continue

            visited.add(node)
            print(f"visiting {node}")

            for neighbhor in sorted(graph[node].items(), key=lambda item: item[1]):
                queue.append(neighbhor)

edmonds_karp(createBipartiteGraph()).bfs()

for employeeCapability in createBipartiteGraph().items():
    print(employeeCapability)