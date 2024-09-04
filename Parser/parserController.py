from Parser.driverParser import DriverParser
from Parser.shiftParser import ShiftParser
from Parser.rosterParser import RosterParser
from datetime import datetime
from constants import SKILLS_MATRIX_PATH
from constants import WEEKLY_TEMPLATES_PATH
from constants import MONTHLY_ROSTERS_PATH

import os

class ParserController:
    def __init__(self, monthly_roster_filepath:str, weekly_template_dir:str):
        self.drivers = DriverParser.driverInitialise(SKILLS_MATRIX_PATH)
        self.rp = RosterParser("roster_M.xlsx")
        self.weekly_template_dir = weekly_template_dir

    def getAllEmployees(self):
        employees = {}
        for driver in self.drivers:
            employees[driver.id] = driver
        return employees
    
    def getAvailableEmployees(self, date:datetime):
        return self.rp.getAvailableDrivers(date, self.drivers)
    
    def getShiftsFromWeeklyTemplate(self, day: str):
        file_path = os.path.join(self.weekly_template_dir, day + ".xlsx")
        print(file_path)
        return ShiftParser.shiftInitialise(file_path)
    
    def getMonthlyDateRange(self):
        return self.rp.getMonthlyDateRange()
    
    def dayHasBeenProcessed(self, date: datetime):
        return self.rp.dayHasBeenProcessed(date)
    

if __name__ == "__main__":
    pc = ParserController(MONTHLY_ROSTERS_PATH, WEEKLY_TEMPLATES_PATH + "/2024 First Half")
    # print("All employees:")
    # print(pc.getAllEmployees())

    # for driver in pc.drivers:
    #     print(driver)
    # print("Available employees:")
    # print(pc.getAvailableEmployees(datetime(2024, 10, 1)))
    # for driver in pc.drivers:
    #     print(driver)

    # print("Shifts:")
    # shifts = pc.getShiftsFromWeeklyTemplate("Monday")
    # for shift in shifts:
    #     print(shift)

    # print("Monthly date range:")
    # print(pc.getMonthlyDateRange())

    print("Day has been processed:")
    print(pc.dayHasBeenProcessed(datetime(2024, 10, 1)))
