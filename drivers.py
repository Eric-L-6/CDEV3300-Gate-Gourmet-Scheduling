import os
import pandas as pd

num_skill = 19
offset = 2
index_column_table = []

 # Driver Class
class Driver:
    # id: int
    # name: string
    # skill_set: set of string
    # responsible_task: string
    # last_work_time: datetime

    def __init__(self, driver_info:list, skill_set:list):
        self.driverSetUp(driver_info, skill_set)

    def __str__(self):
        return f"Driver: {self.name}\nID: {self.id}\nSkill set: {self.skill_set}\nResponsible task: {self.responsible_task}\n"
    
    # driver_info: list of driver information(row)
    # skill_matrix: list of existing skills(column)
    def driverSetUp(self, driver_info:list , skill_matrix:list):
        self.id = driver_info[0]
        self.name = driver_info[1]
        self.skill_set = self.skillSetUp(driver_info[2:], skill_matrix)
        self.responsible_task = self.responsibleSetUp(driver_info);
        self.last_work_time = None

    # skill_info: list of skill information(row)
    def skillSetUp(self, skill_info:list, skill_matrix:list):
        skill_set = set()
        for i in range(len(skill_matrix)):
            # if skill = 〇
            if skill_info[i] == "〇":
                skill_set.add(skill_matrix[i])
        return skill_set
    
    def responsibleSetUp(self, driver_info:list):
        index = index_column_table.index("Responsible task")
        if index in range(len(driver_info)):
            return driver_info[index]
        else:
            return None

class DriverMaker:
    def driverInitialise(filename:str):
        # Check if the file exists in the current directory
        file_path = os.path.join(os.getcwd(), "Input Data",filename)
        drivers = []

        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
        else:
            df = pd.ExcelFile(file_path).parse('Team member list') 
            for i in range(0, len(df.columns)):
                index_column_table.append((df.columns[i]))
            skill_set = df.columns[offset: offset + num_skill].tolist()
            for i in range(1, len(df)):
                # skip if the first column is empty
                if pd.isnull(df.iloc[i, 0]):
                    continue
                # break if the first column is not a number or is empty
                if not isinstance(df.iloc[i, 0], int):
                    break
                # create a driver if the first column is not empty
                if not pd.isnull(df.iloc[i, 0]):
                    driver = Driver(df.iloc[i].tolist(), skill_set)
                    drivers.append(driver)

        return drivers

if __name__ == "__main__":
    drivers = DriverMaker.driverInitialise("skill_M.xlsx")
    for driver in drivers:
        print(driver)