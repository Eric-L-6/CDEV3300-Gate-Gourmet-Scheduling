import os
import pandas as pd

num_skill = 19
offset = 2
index_column_table = []

 # Driver Class
class Driver:
    def __init__(self, driver_info, skill_set):
        self.driverSetUp(driver_info, skill_set)

    def __str__(self):
        return f"Driver: {self.name}\nID: {self.id}\nSkill set: {self.skill_set}\nResponsible task: {self.responsible_task}\n"
    
    def driverSetUp(self, driver_info, skill_set):
        self.id = driver_info[0]
        self.name = driver_info[1]
        self.skill_set = self.skillSetUp(driver_info[2:], skill_set)
        self.responsible_task = self.responsibleSetUp(driver_info);
        self.last_work_time = None

    def skillSetUp(self, skill_info, skill_set):
        skill_dict = {}
        for i in range(len(skill_set)):
            # if skill = 〇
            if skill_info[i] == "〇":
                skill_dict[skill_set[i]] = True
            else:
                skill_dict[skill_set[i]] = False
        return skill_dict
    
    def responsibleSetUp(self, driver_info):
        index = index_column_table.index("Responsible task")
        if index in range(len(driver_info)):
            return driver_info[index]
        else:
            return None
        
    def isAvailable(self, date):
        
        # check if the driver is available on the given date
        return True
    
       


def driverInitialise(filename):
    # Check if the file exists in the current directory
    file_path = os.path.join(os.getcwd(), filename)

    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
    else:
        df = pd.ExcelFile(file_path).parse('Team member list') 
        for i in range(0, len(df.columns)):
            index_column_table.append((df.columns[i]))
        skill_set = df.columns[offset: offset + num_skill].tolist()
        # print(df.columns)
        # print(skill_set)
        drivers = []
        for i in range(1, len(df)):
            # skip if the first column is empty
            if pd.isnull(df.iloc[i, 0]):
                print("Skipping...")
                continue
            # break if the first column is not a number or is empty
            if not isinstance(df.iloc[i, 0], int):
                break
            # create a driver if the first column is not empty
            if not pd.isnull(df.iloc[i, 0]):
                print("Creating driver...")
                print(df.iloc[i].tolist())
                driver = Driver(df.iloc[i].tolist(), skill_set)
                print(driver)
                drivers.append(driver)
        print(f"Number of drivers: {len(drivers)}")
        for driver in drivers:
            print(driver)

def roasterExcelToClass(filename):
    # Check if the file exists in the current directory
    file_path = os.path.join(os.getcwd(), filename)

    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
    else:
        df = pd.ExcelFile(file_path).parse('30SEP')
        print(df.iloc[0])


def main():
    driverInitialise("skill_M.xlsx")
    # roasterExcelToClass("roaster_M.xlsx")



if __name__ == "__main__":
    main()