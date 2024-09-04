from Parser.driverParser import DriverParser
from Parser.shiftParser import ShiftParser
from Parser.rosterParser import RosterParser
from datetime import datetime

def test_driverInitialise():
    DriverParser.driverInitialise("skill_M.xlsx")
    print("Test passed")

def test_shiftInitialise():
    ShiftParser.shiftInitialise("daily_M.xlsx")
    print("Test passed")

def test_getAvailableDrivers():
    drivers = DriverParser.driverInitialise("skill_M.xlsx")
    rp = RosterParser()
    print(rp.getAvailableDrivers(datetime(2024, 9, 30), drivers))
    # print("Test passed")

if __name__ == "__main__":
    test_driverInitialise()
    test_shiftInitialise()
    # test_getAvailableDrivers()