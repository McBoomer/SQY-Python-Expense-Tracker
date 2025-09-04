# MUADH AEJAZ KHAN
# 2024-06-19

# PYTHON USER INTERFACE THAT INTAKES USER DATA USINV INPUT FIELDS, CONFIRMATION
# THROUGH BUTTONS WITH A GITHUB DARK THEME
# USER INPUT IS STORED IN .DB FILE USING SQL AS A QUERYING SYSTEM, INFO IS THEN DISPLAYED ON TABLE
# SAME DATA IS TAKEN, SORTED TO ITS RESPECTIVE CATEGORY THEN ALLOCATED AS A BAR GRAPH ON THE RIGHT HAND SIDE
# OF THE UI. USERS CAN TRACK THEIR SPENDING USING THE SIMPLE INTERACTIVE TOOL
# THIS PROJECT DISPLAYS KNOWLEDGE IN PYTHON, PYQT6, AX, MATPLOTLIBRARY, CSS AND SQL

# MAIN SCRIPT

import sys
from PyQt6.QtWidgets import QMessageBox, QApplication
from database import init_db;
from app import ExpenseApp

# MAIN FUNCTION
def main():
    app = QApplication(sys.argv)
    # ERROR THROW
    if not init_db("expenses.db"):
        QMessageBox.critical(None, "Database Error", "Could not load database file.")
        sys.exit(1)
    # CREATING WINDOW / SHOWING WINDOW
    window = ExpenseApp()
    window.show()
    # ENSURING PROPER EXECUTION
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

# MAIN END