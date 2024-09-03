from datetime import datetime, timedelta
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


# outputs
# {shiftId: driverId}
# all_employees = {1, 2, 3, 4}
# available_employees = [1, 4]
# shifts = [s1, s2, s3]
# output = {s1.id: e1.id, s2: e4.id, s3.id: [e2.id, e3.id]}


class MaxBipartiteGraphSolver:
    def __init__(self, all_employees: dict, available_employees: list, shifts: list):
        self.shifts = shifts
        self.available_employees = available_employees
        self.all_employees = all_employees
        self.off_employees = self.getOffEmployees()
        self.graph = self.createBipartiteGraph(available_employees, shifts)
        self.csr_graph = csr_matrix(self.graph)

    def solve(self):
        max_matching = maximum_bipartite_matching(self.csr_graph, perm_type='row') # match by shift

        result = {}
        for s_index, e_index in enumerate(max_matching):
            if e_index == -1:
                match = self.findElegibleOffEmployees(self.shifts[s_index])
            else:
                match = self.available_employees[e_index]

            result[self.shifts[s_index].id] = match
        return result
    
    def createBipartiteGraph(self, employees, shifts):
        graph = [[0 for _ in range(len(shifts))] for _ in range(len(employees))] 

        for e_index, e_id in enumerate(employees):
            for s_index, shift in enumerate(shifts):
                if self.elegible(e_id, shift):
                    graph[e_index][s_index] = 1

        return graph
    
    def elegible(self, e_id: int, shift: Shift):
        employee = self.all_employees[e_id]

        # employee last worked within 12 hours
        if employee.last_work_time is not None:
            if employee.last_work_time - timedelta(hours=12) <= shift.start_time:
                return False

        # employee lacks required skills for shift
        for task in shift.tasks:
            if task not in employee.skill_set:
                return False
    
        return True

    def findElegibleOffEmployees(self, shift):
        # TODO future sort output based on least amount of overtime
        return [e_id for e_id in self.off_employees if self.elegible(e_id, shift)]

    def getOffEmployees(self):
        return set(self.all_employees.keys()) - set(self.available_employees)

    def print_graph(self):
        for row in self.graph:
            print(row)

if __name__ == '__main__':

    class Driver:
        def __init__(self, id: int, skill_set: set, last_work_time: datetime = None):
            self.id = id
            self.skill_set = skill_set
            self.last_work_time = last_work_time

    class Shift:
        def __init__(self, id: int, tasks: set, start_time: datetime = None):
            self.id = id
            self.tasks = tasks
            self.start_time = start_time

    e1 = Driver(1, {'a', 'b'})
    e2 = Driver(2, {'a'})
    e3 = Driver(3, {'b'})
    e4 = Driver(4, {'a', 'b', 'c'})

    s1 = Shift(1, {'a'})
    s2 = Shift(2, {'a', 'b'})
    s3 = Shift(3, {'a', 'c'})

    # inputs
    all_employees = {1: e1, 2: e2, 3: e3, 4: e4} # e_id: driver
    available_employees = [2, 3]
    shifts = [s1, s2, s3]

    bg = MaxBipartiteGraphSolver(all_employees, available_employees, shifts)
    bg.print_graph()
    print("max matching")
    print(bg.solve())
