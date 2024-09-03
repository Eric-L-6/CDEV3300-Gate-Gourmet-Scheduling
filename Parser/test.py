from drivers import DriverMaker
from shifts import ShiftMaker

def test_driverInitialise():
    DriverMaker.driverInitialise("skill_M.xlsx")
    print("Test passed")

def test_shiftInitialise():
    ShiftMaker.shiftInitialise("daily_M.xlsx")
    print("Test passed")

if __name__ == "__main__":
    test_driverInitialise()
    test_shiftInitialise()