# After parsing: Will have:
# A skills matrix for all employees
# A list of available employees
# A list of shifts and required 
from collections import deque
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


class Driver:
    def __init__(self, id):
        self.id = id

class Shift:
    def __init__(self, id):
        self.id = id

e1 = Driver(1)
e2 = Driver(2)
e3 = Driver(3)
e4 = Driver(4)

s1 = Shift(1)
s2 = Shift(2)
s3 = Shift(3)

# inputs
employees = {1: e1, 2: e2, 3: e3, 4: e4}
available_employees = [1, 4]
shifts = [s1, s2, s3]

# outputs
# {shiftId: driverId}
result = {s1.id: e1.id, s2: e4.id, s3.id: [e2.id, e3.id]}



# potentially: Precalculate the priority of each shift???
# based on how many employees can perform the shift
# OR based on how many available employees cna perform the shift?????????????????????

def getPriority(tasks):
    return len(tasks)

def elegible(employee, tasks):
    for task in tasks:
        if not employee.skill_set[task]:
            return False
    
    return True

class BipartiteGraph:
    def __init__(self, available_employees, shifts):
        self.graph = self.createBipartiteGraph(available_employees, shifts)
        self.source = len(available_employees)


        

    def createBipartiteGraph(available_employees, shifts):
        graph = [[0 for _ in range(len(shifts))] for _ in range(len(available_employees))] 
        graph[SOURCE] = 
        graph[SINK] = {}

        for e_id in available_employees:
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