from constants import *
from datetime import datetime, timedelta
from tkinter import messagebox
from Parser.parserController import ParserController
from Helpers.matchingAlgorithm import MaxBipartiteGraphSolver


class Controller:
    def __init__(self, monthly_roster: str, weekly_template_dir: str):
        self.monthly_roster = monthly_roster
        self.weekly_template_dir = weekly_template_dir

    def process(self):
        pc = ParserController(self.monthly_roster, self.weekly_template_dir)

        # read skillsmatrix -> get all_employees + skillsets
        all_employees = pc.getAllEmployees()
        createdDailyRosters = []

        # main loop - iterate through monthly roster day by day
        for idx, date in enumerate(pc.getMonthlyDateRange()):
            day = date.strftime("%A")

            # check if the day / column has already been processed
            if pc.dayHasBeenProcessed(date):
                continue
            
            # read monthly roster -> get daily availabilities
            available_employees = pc.getDailyAvailability(date)

            # read weekly template -> get daily roster
            required_shifts = pc.getShiftsFromWeeklyTemplate(day)

            # run algorithm
            solver = MaxBipartiteGraphSolver(all_employees, available_employees, required_shifts)
            success, results = solver.solve()

            # write to new daily schedule and monthly roster
            daily_schedule_filename = f"{day} {date.strftime("%d-%m-%Y")}.xlsx"
            path = os.path.splitext(self.monthly_roster)[0]

            pc.writeToNewDailySchedule(results, path, daily_schedule_filename)
            pc.writeToExistingMonthlyRoster(results)

            createdDailyRosters.append(daily_schedule_filename)
            
            # pause if conflict occurs
            if not success or idx == 0:
                break
        
        # showinfo
        if success:
            pass

        # showwarning
        else :
            pass
            print(date, day)
        
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