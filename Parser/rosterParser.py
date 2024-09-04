from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from datetime import datetime, timedelta
import os
class RosterParser():

    unavailable_slot = "FFFF0000"
    driver_id_map = {}
    date_index_map = {}
    ws = None

    def __init__(self, workbook_path):
        # Load the workbook and select the active sheet
        self.workbook_path = os.path.join(os.getcwd(),"Input Data", workbook_path)
        self.wb = load_workbook(self.workbook_path)
        self.ws = self.wb.active
        self.driver_id_map = self.initDriverIdMap()
        self.date_index_map = self.initDateIndexMap()
        print(self.date_index_map)
    
    def initDriverIdMap(self):
        driver_id_map = {}
        for row in range(2, self.ws.max_row + 1):
            driver_id = self.ws.cell(row=row, column=1).value
            if driver_id is not None:
                driver_id_map[self.ws.cell(row=row, column=1).value] = row
        return driver_id_map
    
    def initDateIndexMap(self):
        date_index_map = {}
        for col in range(2, self.ws.max_column + 1):
            date = self.ws.cell(row=2, column=col).value
            # date is a datetime object
            if date is not None and type(date) == datetime:
                date_index_map[date] = col
        return date_index_map
    
    def getKeyFromValue(self, d, value):
        for key, val in d.items():
            if val == value:
                return key
        return None


    def getDateRange(self):
        # get the date range from the excel file 
        return

    # Function to access a cell based on row and column
    def getCellInfo(self, row, col):

        # Get the cell based on the row and column
        cell = self.ws.cell(row=row, column=col)
        cell_info = {
            "value": cell.value,
            "fill_color": None
        }

        # Check if the cell has a fill and access its color
        if cell.fill and cell.fill.fgColor.type == "rgb":
                cell_info["fill_color"] = cell.fill.fgColor.rgb

        return cell_info
    
    # write a specific format of cell into the excel file
    # all cell in the given range if not filled with red color will be filled with that specific format
    def writing(self, row, col, value=None):
        cell = self.ws.cell(row=row, column=col)
        
        # Write a value to the cell if provided
        # color of the value will be black
        if value is not None:
            cell.value = value
            cell.font = cell.font.copy(color="FF000000")
        
        # Change the fill color of the cell
        cell.fill = PatternFill(start_color="FFFFC000", end_color="FFFFC000", fill_type="solid")
        print(f"Writing to cell ({row}, {col}): value={value}, fill_color=FFFFC000")

        cell = self.ws.cell(row=row+1, column=col)

        # fill with empty color and empty value
        cell.fill = PatternFill(start_color="FFFFFFFF", end_color="FFFFFFFF", fill_type="solid")
        cell.value = None
    
        return cell

    # Precondition: 
    # - date is a datetime object
    # - drivers is a list of driver class objects
    # Postcondition:
    # - Returns a list of available drivers based on the date
    def getAvailableDrivers(self, date:datetime, drivers:list):
        # Get the column index based on the date
        date_col = None
        for col in range(1, self.ws.max_column + 1):
            print(self.ws.cell(row=2, column=col).value)
            if self.ws.cell(row=2, column=col).value == date:
                date_col = col
                break
        if date_col is None:
            return []
        # print(f"Date column index: {date_col}")

        # Check if the driver is available on the date
        available_drivers = []

        for driver in drivers:
            print(driver.id)
            if driver.id in self.driver_id_map:
                row = self.driver_id_map[driver.id]
                cell_info = self.getCellInfo(row, date_col)
                # print(f'Before {driver.id} + {cell_info}')
                if cell_info["fill_color"] != self.unavailable_slot:
                    # self.writing(row, date_col, value="欠")
                    # update the last working time of the driver
                    self.updateLastWorkingTime(row, date_col, driver)
                    available_drivers.append(driver.id)

                # print(f'After {driver.id} + {cell_info}')

        self.wb.save(self.workbook_path)  # Save the workbook to persist changes
        print(f"Workbook saved to {self.workbook_path}")
        # return a list of available drivers ids
        return available_drivers
    
    def updateLastWorkingTime(self, row, date_col, driver):
        # get date from date_col
        date = self.getKeyFromValue(self.date_index_map, date_col)
        # find the previous date
        prev_date = date - timedelta(days=1)
        print(f"Previous date: {prev_date}")
        # find the previous date column index
        prev_date_col = self.date_index_map[prev_date]
        if prev_date_col is None:
            driver.last_work_time = None
            return
        # get the previous cell info
        prev_cell_info = self.getCellInfo(row, prev_date_col)
        # check if the previous cell is filled with red color
        if prev_cell_info["fill_color"] == self.unavailable_slot:
            # if so, update the last working time to None
            driver.last_work_time = None
        else:
            print(f'Have yesterday work record: {prev_cell_info}')

    

if __name__ == "__main__":
     # Example usage
    parser = RosterParser()
    # date = datetime(2023, 10, 1)  # Example date
    # drivers = []  # Example list of driver objects
    # available_drivers = parser.getAvailableDrivers(date, drivers)
    # print(available_drivers)

    # Example of writing to a cell
    workbook_path = os.path.join(os.getcwd(), "Input Data/roaster_M.xlsx")
    wb = load_workbook(workbook_path)
    ws = wb.active
    parser.writing(4, 4, ws, value="Test Value")
    wb.save(workbook_path)  # Save the workbook to persist changes
