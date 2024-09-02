from openpyxl import load_workbook
from openpyxl.styles import PatternFill
import os

# Function to access a cell based on row and column
def get_cell_info(row, col):
    # Load the workbook and select the active sheet
    workbook_path = os.path.join(os.getcwd(), "roaster_v2.xlsx" ) # Replace with your Excel file path
    wb = load_workbook(workbook_path)
    ws = wb.active

    # Get the cell based on the row and column
    cell = ws.cell(row=row, column=col)
    print(cell.fill.fgColor)
    cell_info = {
        "value": cell.value,
        "fill_color": None
    }

    # Check if the cell has a fill and access its color
    if cell.fill and cell.fill.fgColor.type == "rgb":
            cell_info["fill_color"] = cell.fill.fgColor.rgb

    return cell_info


# Example usage
row, col = 2, 3  # Change this to the desired row and column
cell_info = get_cell_info(row, col)

if cell_info:
    print(f"Cell ({row}, {col}) info:")
    print(f"Value: {cell_info['value']}")
    print(f"Fill Color: {cell_info['fill_color']}")
else:
    print(f"Cell ({row}, {col}) does not exist.")