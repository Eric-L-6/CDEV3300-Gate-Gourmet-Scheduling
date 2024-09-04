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
        self.rp = RosterParser(os.path.join(MONTHLY_ROSTERS_PATH, monthly_roster_filepath))
        self.weekly_template_dir = os.path.join(WEEKLY_TEMPLATES_PATH, weekly_template_dir)
        self.employees = {}
        self.shifts = {}

    #########################################################################
    #######################    Reader Functions     #########################
    #########################################################################

    def getAllEmployees(self):
        employees = {}
        for driver in self.drivers:
            employees[driver.id] = driver

        self.employees = employees
        return self.employees
    
    def getAvailableEmployees(self, date:datetime):
        return self.rp.getAvailableDrivers(date, self.drivers)
    
    def getShiftsFromWeeklyTemplate(self, day: str):
        file_path = os.path.join(self.weekly_template_dir, day + ".xlsx")
        shift_list = ShiftParser.shiftInitialise(file_path)
        for shift in shift_list:
            self.shifts[shift.id] = shift
        return shift_list
    
    def getMonthlyDateRange(self):
        return self.rp.getMonthlyDateRange()
    
    def dayHasBeenProcessed(self, date: datetime):
        return self.rp.dayHasBeenProcessed(date)
    
    def getRosterSheetList(self):
        return self.rp.getRosterSheetList()
    
    def setRosterSheet(self, sheet_name:str):
        self.rp.setSheet(sheet_name)
    
    #########################################################################
    #######################    Writer Functions     #########################
    #########################################################################

    def writeToNewDailySchedule(self, result:list, path:str, daily_schedule_filename:str):
        ShiftParser.writeToNewDailySchedule(result, path, daily_schedule_filename)

    def writeToMonthlyRoster(self, result:list): 
        self.rp.writeToMonthlyRoster(result, self.employees, self.shifts)
    

if __name__ == "__main__":
    pc = ParserController("Roster.xlsx", "2024 First Half")

    print(pc.getRosterSheetList())
    
    # print("All employees:")
    # print(pc.getAllEmployees())

    # # for driver in pc.drivers:
    # #     print(driver)
    # print("Available employees:")
    # driver_id_list = pc.getAvailableEmployees(datetime(2024, 10, 1))
    # # for driver in pc.drivers:
    # #     print(driver)

    # print("Shifts:")
    # shifts = pc.getShiftsFromWeeklyTemplate("Monday")
    # # for shift in shifts:
    # #     print(shift)

    # print("Monthly date range:")
    # print(pc.getMonthlyDateRange())

    # print("Day has been processed:")
    # print(pc.dayHasBeenProcessed(datetime(2024, 9, 30)))

    # shift_id_list = [shifts[0].id]
    # result = {}
    # i = 0
    # for shift_id in shift_id_list:
    #     result[shift_id] = driver_id_list[i]
    #     i += 1
    # print("Result:")
    # pc.writeToMonthlyRoster(result)

