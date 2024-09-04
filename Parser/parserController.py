from Parser.driverParser import DriverParser
from Parser.shiftParser import ShiftParser
from Parser.rosterParser import RosterParser
from datetime import datetime

class ParserController:
    def __init__(self):
        self.drivers = DriverParser.driverInitialise("skill_M.xlsx")
        self.shifts = ShiftParser.shiftInitialise("2024 first half.xlsx")
        self.rp = RosterParser("roster_M.xlsx")

    def getAllEmployees(self):
        employees = {}
        for driver in self.drivers:
            employees[driver.id] = driver
        return employees
    
    def getAvailableEmployees(self, date:datetime):
        return self.rp.getAvailableDrivers(date, self.drivers)
    
    def getShifts(self):
        return self.shifts
    
    def getMonthlyDateRange(self):
        return self.rp.getMonthlyDateRange()
    

if __name__ == "__main__":
    pc = ParserController()
    # print("All employees:")
    # print(pc.getAllEmployees())
    # print("Available employees:")
    # print(pc.getAvailableEmployees(datetime(2024, 10, 1)))
    # print("Shifts:")
    # print(pc.getShifts())

    print("Monthly date range:")
    print(pc.getMonthlyDateRange())