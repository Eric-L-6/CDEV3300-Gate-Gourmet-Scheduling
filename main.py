from tkinter import ttk, messagebox
from controller import Controller
import tkinter as tk
import os
from constants import MONTHLY_ROSTERS_PATH, WEEKLY_TEMPLATES_PATH

##################################################################
########################## Helpers ###############################

def validWeeklyTemplateDir(weekly_template_dir: str) -> bool:
    if not weekly_template_dir:
        messagebox.showwarning("Selection Error", "Please select a weekly template from the dropdown.")
        return False

    return True

def validMonthlyRoster(monthly_roster: str) -> bool:
    if not monthly_roster:
        messagebox.showwarning("Selection Error", "Please select a monthly roster from the dropdown.")
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
        controller = Controller(monthly_roster, weekly_template_dir)
        
        # close program if successfull
        if controller.process():
            root.destroy()

    # Create the main application window
    root = tk.Tk()
    root.title("Shift Scheduler")
    root.geometry("400x200")

    # File selection label and Combobox
    file_label = tk.Label(root, text="Select the monthly roster:")
    file_label.pack(pady=10)

    # Create a Combobox to display xlsx file names
    file_combobox = ttk.Combobox(root, width=38, state="readonly")

    # Check if the path exists and populate the Combobox with xlsx files
    if os.path.exists(MONTHLY_ROSTERS_PATH) and os.path.isdir(MONTHLY_ROSTERS_PATH):
        files = [f for f in os.listdir(MONTHLY_ROSTERS_PATH) if f.endswith('.xlsx')]
        file_combobox['values'] = files
    else:
        file_combobox['values'] = ["No rosters found"]
    file_combobox.pack(pady=5)

    # Folder selection label and Combobox
    folder_label = tk.Label(root, text="Please select the weekly template:")
    folder_label.pack(pady=10)

    # Create a Combobox to display folder names
    folder_combobox = ttk.Combobox(root, width=38, state="readonly")

    # Check if the path exists and populate the Combobox with folders
    if os.path.exists(WEEKLY_TEMPLATES_PATH) and os.path.isdir(WEEKLY_TEMPLATES_PATH):
        folders = [f for f in os.listdir(WEEKLY_TEMPLATES_PATH) if os.path.isdir(os.path.join(WEEKLY_TEMPLATES_PATH, f))]
        folder_combobox['values'] = folders
    else:
        folder_combobox['values'] = ["No templates found"]
    folder_combobox.pack(pady=5)

    # Button to confirm selection
    confirm_button = tk.Button(root, text="Confirm Selection", command=onSubmit)
    confirm_button.pack(pady=20)

    # Start the main event loop
    root.mainloop()