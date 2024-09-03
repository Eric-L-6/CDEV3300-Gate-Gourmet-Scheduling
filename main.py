from tkinter import ttk, messagebox
from datetime import datetime
import tkinter as tk
import os

##################################################################
########################## Helpers ###############################

def isValidDate(date_string):
    try:
        # Try to parse the date string in DD-MM-YYYY format
        datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        # If parsing fails, it's not in the correct format or an invalid date
        return False

def validateDateEntry(date_entry: str) -> bool:
    if not date_entry:
        messagebox.showwarning("Input Error", "Please enter a date.")
        return False
    
    if not isValidDate(date_entry):
        messagebox.showwarning("Input Error", "Please enter the date in (DD-MM-YYYY) format")
        return False
    
    # if date not found - invalid date entry

    return True

##################################################################
########################### Main #################################

if __name__ == '__main__':
    
    # Function to handle onSubmit
    def onSubmit():
        daily_schedule_folder = folder_combobox.get()
        date_input = date_entry.get()
        
        # Validate date input format (simple example, more validation may be needed)
        validateDateEntry(date_input)

        if not isValidDate(date_input):
            messagebox.showwarning("Input Error", "Please enter a date.")
            return
        if not daily_schedule_folder:
            messagebox.showwarning("Selection Error", "Please select a folder from the dropdown.")
            return
        
        # Show the selected date and folder
        messagebox.showinfo("Selection", f"Selected Date: {date_input}\nSelected Folder: {selected_folder}")

    # Create the main application window
    root = tk.Tk()
    root.title("Shift Scheduler")
    root.geometry("400x200")

    # Date input label and entry
    date_label = tk.Label(root, text="Enter Date to schedule (DD-MM-YYYY):")
    date_label.pack(pady=10)
    date_entry = tk.Entry(root, width=20)
    date_entry.pack(pady=5)

    # Folder selection label and Combobox
    folder_label = tk.Label(root, text="Please select :")
    folder_label.pack(pady=10)

    # Define the relative path to search for folders
    relative_path = 'Inputs\\DailyScheduleTemplates'  # Change this to your desired relative path

    # Get the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Get the absolute path from the relative path
    absolute_path = os.path.join(script_directory, relative_path)

    # Create a Combobox to display folder names
    folder_combobox = ttk.Combobox(root, width=38, state="readonly")

    # Check if the path exists and populate the Combobox with folders
    if os.path.exists(absolute_path) and os.path.isdir(absolute_path):
        folders = [f for f in os.listdir(absolute_path) if os.path.isdir(os.path.join(absolute_path, f))]
        folder_combobox['values'] = folders
    else:
        folder_combobox['values'] = ["No folders found"]
    folder_combobox.pack(pady=5)

    # Button to confirm selection
    confirm_button = tk.Button(root, text="Confirm Selection", command=onSubmit)
    confirm_button.pack(pady=20)

    # Start the main event loop
    root.mainloop()