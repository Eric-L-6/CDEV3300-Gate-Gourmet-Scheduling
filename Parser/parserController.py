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
        available_employees = []
        rp = RoasterParser()
        return rp.getAvailableDrivers(datetime(2024, 9, 30), self.drivers)
    
    def getShifts(self):
        return self.shifts
    

if __name__ == "__main__":
    pc = ParserController()
    print("All employees:")
    print(pc.getAllEmployees())
    print("Available employees:")
    print(pc.getAvailableEmployees(datetime(2024, 9, 30)))
    print("Shifts:")
    print(pc.getShifts())