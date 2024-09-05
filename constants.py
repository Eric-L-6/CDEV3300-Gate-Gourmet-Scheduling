import os
import sys

# Determine if running as a bundled executable or as a script
if getattr(sys, 'frozen', False):
    # Path to the folder where the executable is located
    base_path = os.path.dirname(sys.executable)
else:
    # Path to the folder where the script is located
    base_path = os.path.dirname(os.path.abspath(__file__))

INPUT_PATH = os.path.join(base_path, "Inputs")
MONTHLY_ROSTERS_PATH = os.path.join(INPUT_PATH, "MonthlyRosters")
WEEKLY_TEMPLATES_PATH = os.path.join(INPUT_PATH, "WeeklyTemplates")
SKILLS_MATRIX_PATH = os.path.join(INPUT_PATH, "SkillMatrix", "skill_M.xlsx")
OUTPUT_PATH = os.path.join(base_path, "Outputs")