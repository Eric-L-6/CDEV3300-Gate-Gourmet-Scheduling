from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from datetime import datetime
import os
class RosterParser():

    unavailable_slot = "FFFF0000"

    # Function to access a cell based on row and column
    def getCellInfo(self, row, col):
        # Load the workbook and select the active sheet
        workbook_path = os.path.join(os.getcwd(), "Input Data/roster_v2.xlsx" ) # Replace with your Excel file path
        wb = load_workbook(workbook_path)
        ws = wb.active

        # Get the cell based on the row and column
        cell = ws.cell(row=row, column=col)
        cell_info = {
            "value": cell.value,
            "fill_color": None
        }

        # Check if the cell has a fill and access its color
        if cell.fill and cell.fill.fgColor.type == "rgb":
                cell_info["fill_color"] = cell.fill.fgColor.rgb

        return cell_info

    # Precondition: 
    # - date is a datetime object
    # - drivers is a list of driver class objects
    # Postcondition:
    # - Returns a list of available drivers based on the date
    def getAvailableDrivers(self, date:datetime, drivers:list):
        # Load the workbook and select the active sheet
        workbook_path = os.path.join(os.getcwd(),"Input Data/roster_v2.xlsx")
        wb = load_workbook(workbook_path)
        ws = wb.active

        # Get the column index based on the date
        date_col = None
        for col in range(1, ws.max_column + 1):
            if ws.cell(row=1, column=col).value == date:
                date_col = col
                break

        if date_col is None:
            return []
        
        # Get the row index mapping to the driver id
        driver_id_map = {}
        for row in range(2, ws.max_row + 1):
            driver_id_map[ws.cell(row=row, column=1).value] = row
        # print(driver_id_map)

        # Check if the driver is available on the date
        available_drivers = []
        for driver in drivers:
            if driver.id in driver_id_map:
                row = driver_id_map[driver.id]
                cell_info = self.getCellInfo(row, date_col)
                if cell_info["fill_color"] != self.unavailable_slot:
                    # print(f"Driver {driver.id} is available on {date}")
                    available_drivers.append(driver.id)

        # return a list of available drivers ids
        return available_drivers

    if __name__ == "__main__":
        # Example usage
        row, col = 2, 3  # Change this to the desired row and column
        cell_info = getCellInfo(row, col)

        if cell_info:
            print(f"Cell ({row}, {col}) info:")
            print(f"Value: {cell_info['value']}")
            print(f"Fill Color: {cell_info['fill_color']}")
        else:
            print(f"Cell ({row}, {col}) does not exist.")
        print(getAvailableDrivers(datetime(2024, 9, 30)))
