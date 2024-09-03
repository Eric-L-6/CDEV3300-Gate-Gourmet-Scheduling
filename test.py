from drivers import DriverMaker
from shifts import ShiftMaker
from Parser.roasterParser import RoasterParser
from datetime import datetime

def test_driverInitialise():
    DriverMaker.driverInitialise("skill_M.xlsx")
    print("Test passed")

def test_shiftInitialise():
    ShiftMaker.shiftInitialise("daily_M.xlsx")
    print("Test passed")

def test_getAvailableDrivers():
    drivers = DriverMaker.driverInitialise("skill_M.xlsx")
    rp = RoasterParser()
    print(rp.getAvailableDrivers(datetime(2024, 9, 30), drivers))
    # print("Test passed")

if __name__ == "__main__":
    # test_driverInitialise()
    # test_shiftInitialise()
    test_getAvailableDrivers()