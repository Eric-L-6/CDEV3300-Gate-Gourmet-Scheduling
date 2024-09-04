from constants import *
from datetime import datetime, timedelta
from tkinter import messagebox
from Parser.parserController import ParserController
from Helpers.matchingAlgorithm import MaxBipartiteGraphSolver


class Controller:
    def __init__(self, monthly_roster: str, roster_sheet: str, weekly_template_dir: str):
        self.monthly_roster = monthly_roster
        self.roster_sheet = roster_sheet
        self.weekly_template_dir = weekly_template_dir

    def process(self, pause_first_day: bool) -> bool:
        pc = ParserController(self.monthly_roster, self.roster_sheet, self.weekly_template_dir)

        # read skillsmatrix -> get all_employees + skillsets
        all_employees = pc.getAllEmployees()
        created_daily_rosters = []

        # main loop - iterate through monthly roster day by day
        for idx, date in enumerate(pc.getMonthlyDateRange()):
            day = date.strftime("%A")

            # check if the day / column has already been processed
            if pc.dayHasBeenProcessed(date):
                continue
            
            # read monthly roster -> get daily availabilities
            available_employees = pc.getAvailableEmployees(date)

            # read weekly template -> get daily roster
            required_shifts = pc.getShiftsFromWeeklyTemplate(day)

            # run algorithm
            solver = MaxBipartiteGraphSolver(all_employees, available_employees, required_shifts)
            success, results = solver.solve()

            # write to new daily schedule and monthly roster
            daily_schedule_filename = f"{day} {date.strftime("%d-%m-%Y")}.xlsx"
            monthly_roster_dir = f"{os.path.splitext(self.monthly_roster)[0]} {self.roster_sheet}"
            
            # check if monthly roster dir exists
            # if not exists: create dir
            # copy daily template for the day to dir named as daily_schedule_filename
            #   overwrite if exists
            # do same thing as writetomonthlyroster
            #   if a list - write list to the cell and change cell backgroun colour to eg yellow

            pc.writeToNewDailySchedule(results, monthly_roster_dir, daily_schedule_filename)
            pc.writeToMonthlyRoster(results, success)

            created_daily_rosters.append(daily_schedule_filename)
            
            # pause if conflict occurs
            if not success or idx == 0 and pause_first_day:
                break
        
        daily_roster_str = "\n".join([f"\t{daily_roster}" for daily_roster in created_daily_rosters])
        title = "Info"
        message = f"""
Updated '{self.monthly_roster} > {self.roster_sheet}'.
Created the following daily rosters in 'Outputs/{monthly_roster_dir}':
{daily_roster_str}
"""
        messagebox.showinfo(title, message)

        # showinfo
        if success:
            title = "Success"
            message = f"Successfully allocated all drivers for {self.monthly_roster}"
            messagebox.showinfo(title, message)

        # showwarning
        elif idx == 0 and pause_first_day:
            success = False
            title = "Caution"
            message = f"Please check if the allocation for the first day of the month '{created_daily_rosters[-1]}' is valid before running the program again.\n\nCheck if the rostered drivers have at least 12 hours between shifts in the previous month.\n\nIf there are conflicts, please manually resolve and update both {created_daily_rosters[-1]} and {self.monthly_roster}"
            messagebox.showwarning(title, message)
        
        else:
            title = "Warning"
            message = f"Conflict occured in '{created_daily_rosters[-1]}'. Please manually resolve this issue.\nUpdate the Monthly Roster '{self.monthly_roster}' before running the program again."
            messagebox.showerror(title, message)

        return success


    
    # need to: 
    

    # read skills matrix // DONE MOSTLY
    # iterate through monthly roster day by day
    # if the column / day has already been processed before, continue
    # if the column has not been processed:
    #   read daily availabilities -> available_employees // KINDA
    #   read daily shift schedule for that day -> shifts // DONE mostly, 
    #   run algorithm(all_employees, available_employees, shifts) // DONE
    # if success if true OR false:
    #   TODO generate filled daily schedules // 
    #   TODO fill in row for monthly schedule
    # if success if false: break
    # if success is true: continue

#   a  function that parses the monthly schedule and returns the range of dates
#   a function that reads the monthly schedule day by day
#   one that reads if the day has been processed or not
#   one that reads the daily availabilites

# a function that writes to the monthly schedule based on the day - should also mark that day / column as processed
# a function that writes to the daily schedule template - create a new copy of the template, write to the template, and then save based on a title we provide


    # end of loop:
    # use messagebox to show message:
    # list of created daily schedules
    # updated monthly schedule file
    # if conflict occured: showwarning -> caution display day that conflict occured and show message to ask manager to manually resolve conflict
    # if no conflict occured: showinfo -> success


# first day of the month
# fill out hte first day based on the facst that everyone can work
# pause the program there - generat the first day first
# let the manager manually check if the allocaiton is right
# then proceed