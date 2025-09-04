# MUADH AEJAZ KHAN
# 2024-06-19
# SQL DATABASE FOR EXPENSE TRACKER APP

from xmlrpc.client import DateTime
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QDateTimeEdit, QTableWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import QDate, QDateTime, Qt
from PyQt6.QtSql import QSqlQuery
from database import fetch_expenses, add_expense, delete_expense

# IMPORT MATPLOTLIB FOR GRAPH
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ExpenseApp(QWidget):
    # INITIALIZE APP
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        self.apply_styles();
        self.load_table_data()
        self.update_graph();  # DRAW GRAPH WHEN START
    
        # TESTING FOR PROPER SIZE
        def resizeEvent(self, event):
            width = self.width()
            hieght = self.height
            print(f"WINDOW SIZE: {width} x {hieght}")
            super().resizeEvent(event)

    # SET WINDOW CONFIGURATION
    def settings(self):
        self.setGeometry(700, 400, 1440, 780)
        self.setWindowTitle("Expense Tracker App  |  Muadh Aejaz Khan  |  2025")

    # INITIALIZE UI ELEMENTS
    def initUI(self):
        # DATE PICKER
        self.date_box = QDateTimeEdit()
        self.date_box.setDateTime(QDateTime.currentDateTime())
        self.date_box.setDisplayFormat("yyyy-MM-dd hh:mm AP");  # SHOW 12HR TIME

        # INPUT FIELDS
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        # BUTTONS
        self.btn_add = QPushButton("Add Expense")
        self.btn_delete = QPushButton("Delete Expense")
        self.btn_view = QPushButton("View All Expenses")

        # TABLE
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(("ID", "Date", "Category", "Amount",
        "Description"))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.setup_layout()

    # SETUP LAYOUT
    def setup_layout(self):
        # MASTER LAYOUT HORIZONTAL TO HAVE GRAPH ON SIDE
        master = QHBoxLayout()
        left_layout = QVBoxLayout()  # LEFT SIDE WITH TABLE AND INPUTS
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        # TODAY BUTTON
        self.btn_today = QPushButton("Today")
        row1.addWidget(QLabel("Date:"))
        row1.addWidget(self.date_box)
        row1.addWidget(self.btn_today)
        row1.addWidget(QLabel("Category:"))
        row1.addWidget(self.dropdown)

        # AMOUNT AND DESCRIPTION ROW
        row2.addWidget(QLabel("Amount:"))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel("Description:"))
        row2.addWidget(self.description)

        # BUTTONS ROW
        row3.addWidget(self.btn_add)
        row3.addWidget(self.btn_delete)

        # ADD ROWS TO LEFT LAYOUT
        left_layout.addLayout(row1)
        left_layout.addLayout(row2)
        left_layout.addLayout(row3)
        left_layout.addWidget(self.table)

        # POPULATE DROPDOWN
        self.populate_dropdown()

        # CONNECT BUTTONS
        self.btn_add.clicked.connect(self.add_expense)
        self.btn_today.clicked.connect(self.set_today_date);
        self.btn_delete.clicked.connect(self.delete_expense_item)

        # CREATE GRAPH CANVAS
        self.graph_canvas = FigureCanvas(Figure(figsize=(4, 6)))
        self.ax = self.graph_canvas.figure.add_subplot(111)
        self.ax.set_facecolor("#0d1117")
        self.graph_canvas.figure.tight_layout()

        # ADD LEFT AND GRAPH TO MASTER
        master.addLayout(left_layout, 3)
        master.addWidget(self.graph_canvas, 1)

        self.setLayout(master)

    # APPLY STYLES
    def apply_styles(self):
        # CSS BUILT INTO PYTHON FILE
        self.setStyleSheet("""
        QWidget {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: "Segoe UI", sans-serif;
            font-size: 14px;
        }

        QLabel {
            color: #c9d1d9;
        }

        QLineEdit, QComboBox, QDateEdit {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 6px;
            padding: 6px;
            color: #c9d1d9;
        }
        QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
            border: 1px solid #58a6ff;
            outline: none;
        }

        QPushButton {
            background-color: #21262d;
            border: 1px solid #30363d;
            border-radius: 6px;
            padding: 8px 14px;
            color: #c9d1d9;
            font-weight: 500;
        }
        QPushButton:hover {
            background-color: #30363d;
            border: 1px solid #58a6ff;
            color: #ffffff;
        }
        QPushButton:pressed {
            background-color: #161b22;
            border: 1px solid #58a6ff;
            padding-top: 10px;
            padding-left: 15px;
        }

        QTableWidget {
            background-color: #161b22;
            gridline-color: #30363d;
            border: 1px solid #30363d;
            border-radius: 6px;
        }
        QHeaderView::section {
            background-color: #21262d;
            color: #c9d1d9;
            border: 1px solid #30363d;
            padding: 6px;
        }
        """)

    # POPULATE DROPDOWN MENU
    def populate_dropdown(self):
        categories = ["Food", "Transport", "Entertainment", "Utilities", "Rent", "Other"]
        self.dropdown.addItems(categories)

    # LOAD DATA TO TABLE
    def load_table_data(self):
        expenses = fetch_expenses()
        self.table.setRowCount(0)
        for row_idx, expense in enumerate(expenses):
            self.table.insertRow(row_idx)
            for col_idx, data in enumerate(expense):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    # SET DATE TO TODAY (CURRENTDATETIME)
    def set_today_date(self):
        self.date_box.setDateTime(QDateTime.currentDateTime())

    # CLEAR INPUTS
    def clear_inputs(self):
        self.date_box.setDateTime(QDateTime.currentDateTime())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear();
        self.description.clear();

    # GRAPHINV UPDATE
    def update_graph(self):
        expenses = fetch_expenses()
        categories = [e[2] for e in expenses]
        amounts = [float(e[3]) for e in expenses]

        self.ax.clear()
        self.ax.set_facecolor("#0d1117")
        self.ax.figure.set_facecolor("#0d1117")
        self.ax.tick_params(colors="#c9d1d9", which="both")
        self.ax.spines["top"].set_color("#c9d1d9")
        self.ax.spines["right"].set_color("#c9d1d9")
        self.ax.spines["bottom"].set_color("#c9d1d9")
        self.ax.spines["left"].set_color("#c9d1d9")
        self.ax.yaxis.label.set_color("#c9d1d9")
        self.ax.xaxis.label.set_color("#c9d1d9")

        if expenses:
            category_sums = {}
            for cat, amt in zip(categories, amounts):
                category_sums[cat] = category_sums.get(cat, 0) + amt
            cats = list(category_sums.keys())
            vals = list(category_sums.values())

            # BAR COLORS
            bar_colors = ["#58a6ff", "#ffa657", "#79c0ff", "#ff7b72", "#d2a8ff", "#ffdf5d"]
            colors = [bar_colors[i % len(bar_colors)] for i in range(len(cats))]
            self.ax.bar(cats, vals, color=colors)

        self.ax.set_ylabel("Amount", color="#c9d1d9")
        self.ax.set_xlabel("Category", color="#c9d1d9")
        self.ax.set_title("Expenses by Category", color="#c9d1d9")
        self.ax.tick_params(axis="x", rotation=30)
        self.graph_canvas.draw();

    # ADD EXPENSE
    def add_expense(self):
        date = self.date_box.dateTime().toString("yyyy-MM-dd hh:mm AP")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        check = QSqlQuery("SELECT COUNT(*) FROM expenses")
        if check.next():
            print("Cardinality of data :", check.value(0));

        if not amount or not description:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.");
            return
        if add_expense(date, category, float(amount), description):
            self.load_table_data()
            self.clear_inputs()
            self.update_graph();
        else:
            QMessageBox.critical(self, "Database Error", "Failed to add expense.");

    # DELETE EXPENSE
    def delete_expense_item(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Selection Error", "Select item to delete.");
            return

        expense_id = int(self.table.item(row, 0).text())

        # CONFIRM DELETE
        confirm = QMessageBox.question(
            self,
            "Confirm Delete",
            "Are you sure you want to delete this expense?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        );

        if confirm == QMessageBox.StandardButton.Yes and delete_expense(expense_id):
            self.load_table_data();
            self.update_graph();  # UPDATE GRAPH AFTER DELETE

# APP END