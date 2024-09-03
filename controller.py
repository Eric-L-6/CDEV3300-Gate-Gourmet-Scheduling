from constants import *
from tkinter import messagebox

class Controller:
    def __init__(self, monthly_roster: str, weekly_template_dir: str):
        self.monthly_roster = monthly_roster
        self.weekly_template_dir = weekly_template_dir

    def process(self):
        print("Processing")
    
    # need to: 
    # read monthly roster -> get daily availabilities 
    # weekly_template_dir -> read daily shift schedule -> get shifts + required tasks
    # read skillsmatrix -> get all_employees + skillsets
    
    # read skills matrix
    # iterate through monthly roster day by day
    # if the column / day has already been processed before, continue
    # if the column has not been processed:
    #   read daily availabilities -> available_employees
    #   read daily shift schedule for that day -> shifts
    #   run algorithm(all_employees, available_employees, shifts)
    # if success is false, ie not enough employees, break at that point 
    # if success if true:
    #   TODO generate filled daily schedules
    #   TODO fill in row for monthly schedule

    # end of loop:
    # use messagebox to show message:
    # list of created daily schedules
    # updated monthly schedule file
    # if conflict occured: showwarning -> caution display day that conflict occured and show message to ask manager to manually resolve conflict
    # if no conflict occured: showinfo -> success

