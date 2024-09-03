from Parser.driverParser import DriverParser
from Parser.shiftParser import ShiftParser
from Parser.roasterParser import RoasterParser
from datetime import datetime

class ParserController:
    def __init__(self):
        self.drivers = DriverParser.driverInitialise("skill_M.xlsx")
        self.shifts = ShiftParser.shiftInitialise("daily_M.xlsx")

    def getAllEmployees(self):
        employees = {}
        for driver in self.drivers:
            employees[driver.id] = driver
        return employees
    
    def getAvailableEmployees(self, date:datetime):
        rp = RoasterParser("roaster_M.xlsx")
        return rp.getAvailableDrivers(date, self.drivers)
    
    def getShifts(self):
        return self.shifts
    

if __name__ == "__main__":
    pc = ParserController()
    # print("All employees:")
    # print(pc.getAllEmployees())
    print("Available employees:")
    print(pc.getAvailableEmployees(datetime(2024, 10, 6)))
    # print("Shifts:")
    # print(pc.getShifts())