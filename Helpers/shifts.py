class Shift:
    # id: int
    # start_time: datetime
    # end_time: datetime
    # task_requirement: list of string

    def __init__(self, id, start_time, end_time, task_requirement):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.task_requirement = task_requirement
    
    def __str__(self):
        return f"Shift: {self.id}\nStart time: {self.start_time}\nEnd time: {self.end_time}\nTask requirement: {self.task_requirement}\n"
