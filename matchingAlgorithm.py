# After parsing: Will have:
# A skills matrix for all employees
# A list of available employees
# A list of roles and required 

SOURCE = 'SOURCE_NODE';
SINK = 'SINK_NODE';

taskTypes = ['one', 'two']
skillsMatrix = {'a': {'one': True, 'two': False}, 'b': {'one': False, 'two': False}, 'c': {'one': False, 'two': True}}
availableEmplyees = ['a', 'b', 'c']
unavailableEmployees = []
dailyRoles = {1: ['one'], 2: ['two'], 3: ['one', 'two']}

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

    for role, _ in dailyRoles:
        graph[role] = {}
        graph[role][SINK] = 1
    
    for employee in availableEmplyees:
        for role, tasks in dailyRoles:
            if elegible(employee, tasks):
                graph[employee][role] = 1 * getPriority(tasks)
                graph[role][employee] = 0

    return graph

for employeeCapability in createBipartiteGraph():
    print(employeeCapability)