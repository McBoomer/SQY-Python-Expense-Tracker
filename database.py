# SQL IMPLEMENTATION FOR DATABASE QUERIES AND STORAGE

from PyQt6.QtSql import QSqlDatabase, QSqlQuery

def init_db(db_name):
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName(db_name)

    if not database.open():
        return False;
    # SQL QUERY IN STRING
    query = QSqlQuery("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
    """)
    return True

def fetch_expenses():
    query = QSqlQuery("SELECT * FROM expenses ORDER BY date DESC")
    expenses = []

    while query.next():
        row = [query.value(i) for i in range(5)]
        expenses.append(row)

    # RETURN LIST AT END
    return expenses

def add_expense(date, category, amount, description):
    query = QSqlQuery()
    # UNKNOWN VALUE INSERTED AS ? PLACHOLER
    query.prepare("""
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    """)
    query.addBindValue(date)
    query.addBindValue(category)
    query.addBindValue(amount)
    query.addBindValue(description)

    # QUERY EXECUTION / CHECK
    if not query.exec():
        print("Insert failed", query.lastError().text())
        return False
    
    print ("Insert success", date, category, amount, description)
    return True

def delete_expense(expense_id):
    query = QSqlQuery()
    query.prepare("DELETE FROM expenses WHERE id = ?")
    query.addBindValue(expense_id);

    return query.exec()

# SQL DATABASING FILE END