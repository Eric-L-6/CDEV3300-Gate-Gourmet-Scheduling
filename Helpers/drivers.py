class Driver:
    # id: int
    # name: string
    # skill_set: set of string
    # responsible_task: string
    # last_work_time: datetime

    def __init__(self, driver_info:list, skill_set:list, index_column_table:list):
        self.driverSetUp(driver_info, skill_set, index_column_table)

    def __str__(self):
        return f"Driver: {self.name}\nID: {self.id}\nSkill set: {self.skill_set}\nResponsible task: {self.responsible_task}\n"
    
    # driver_info: list of driver information(row)
    # skill_matrix: list of existing skills(column)
    def driverSetUp(self, driver_info:list , skill_matrix:list, index_column_table:list):
        self.id = driver_info[0]
        self.name = driver_info[1]
        self.skill_set = self.skillSetUp(driver_info[2:], skill_matrix)
        self.responsible_task = self.responsibleSetUp(driver_info, index_column_table);
        self.last_work_time = None

    # skill_info: list of skill information(row)
    def skillSetUp(self, skill_info:list, skill_matrix:list):
        skill_set = set()
        for i in range(len(skill_matrix)):
            # if skill = 〇
            if skill_info[i] == "〇":
                skill_set.add(skill_matrix[i])
        return skill_set
    
    def responsibleSetUp(self, driver_info:list, index_column_table:list):
        index = index_column_table.index("Responsible task")
        if index in range(len(driver_info)):
            return driver_info[index]
        else:
            return None