from tkinter import ttk, messagebox
from datetime import datetime
import tkinter as tk
import os

##################################################################
########################## Helpers ###############################

def validWeeklyTemplateDir(daily_schedule_folder: str) -> bool:
    if not daily_schedule_folder:
        messagebox.showwarning("Selection Error", "Please select a folder from the dropdown.")
        return False

    return True

def validMonthlyRoster(monthly_roster: str) -> bool:
    if not monthly_roster:
        messagebox.showwarning("Selection Error", "Please select a file from the dropdown.")
        return False
    
    return True

##################################################################
########################### Main #################################

if __name__ == '__main__':
    
    # Function to handle onSubmit
    def onSubmit():
        
        monthly_roster = file_combobox.get()
        weekly_template_dir = folder_combobox.get()
        
        if not validWeeklyTemplateDir(weekly_template_dir):
            return
        
        if not validMonthlyRoster(monthly_roster):
            return

        # TODO process the selection
        messagebox.showinfo("Selection", f"Selected roster: {monthly_roster}\nSelected template: {weekly_template_dir}")

    # Create the main application window
    root = tk.Tk()
    root.title("Shift Scheduler")
    root.geometry("400x200")

    # Get the absolute input path
    inputs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Inputs")

    # File selection label and Combobox
    file_label = tk.Label(root, text="Select the monthly roster:")
    file_label.pack(pady=10)

    # Create a Combobox to display xlsx file names
    file_combobox = ttk.Combobox(root, width=38, state="readonly")

    # relative path for monthly roster
    monthlyRosterPath = os.path.join(inputs_path, "MonthlyRosters")

    # Check if the path exists and populate the Combobox with xlsx files
    if os.path.exists(monthlyRosterPath) and os.path.isdir(monthlyRosterPath):
        files = [f for f in os.listdir(monthlyRosterPath) if f.endswith('.xlsx')]
        file_combobox['values'] = files
    else:
        file_combobox['values'] = ["No rosters found"]
    file_combobox.pack(pady=5)

    # Folder selection label and Combobox
    folder_label = tk.Label(root, text="Please select the weekly template:")
    folder_label.pack(pady=10)

    # Create a Combobox to display folder names
    folder_combobox = ttk.Combobox(root, width=38, state="readonly")

    weeklyTemplatesPath = os.path.join(inputs_path, "WeeklyTemplates")

    # Check if the path exists and populate the Combobox with folders
    if os.path.exists(weeklyTemplatesPath) and os.path.isdir(weeklyTemplatesPath):
        folders = [f for f in os.listdir(weeklyTemplatesPath) if os.path.isdir(os.path.join(weeklyTemplatesPath, f))]
        folder_combobox['values'] = folders
    else:
        folder_combobox['values'] = ["No templates found"]
    folder_combobox.pack(pady=5)

    # Button to confirm selection
    confirm_button = tk.Button(root, text="Confirm Selection", command=onSubmit)
    confirm_button.pack(pady=20)

    # Start the main event loop
    root.mainloop()