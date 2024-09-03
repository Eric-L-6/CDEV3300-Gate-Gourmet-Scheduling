import os
import pandas as pd
from Helpers.drivers import Driver

num_skill = 19
offset = 2
index_column_table = []

class DriverParser():
    def driverInitialise(file_path: str):
        drivers = []

        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
        else:
            df = pd.ExcelFile(file_path).parse('Team member list') 
            for i in range(0, len(df.columns)):
                index_column_table.append((df.columns[i]))
            skill_set = df.columns[offset: offset + num_skill].tolist()
            for i in range(0, len(df)):
                # skip if the first column is empty
                if pd.isnull(df.iloc[i, 0]):
                    continue
                # break if the first column is not a number or is empty
                if not isinstance(df.iloc[i, 0], int):
                    break
                # create a driver if the first column is not empty
                if not pd.isnull(df.iloc[i, 0]):
                    driver = Driver(df.iloc[i].tolist(), skill_set, index_column_table)
                    drivers.append(driver)

        return drivers

if __name__ == "__main__":
    drivers = DriverParser.driverInitialise(os.path.join(os.getcwd(), "Input Data", "skill_M.xlsx"))
    for driver in drivers:
        print(driver)