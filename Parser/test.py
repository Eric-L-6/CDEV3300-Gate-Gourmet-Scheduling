import drivers
import shifts

def test_driverInitialise():
    drivers.driverInitialise("skill_M.xlsx")
    print("Test passed")

def test_shiftInitialise():
    shifts.shiftInitialise("daily_M.xlsx")
    print("Test passed")

if __name__ == "__main__":
    test_driverInitialise()
    test_shiftInitialise()