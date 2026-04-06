import sqlite3

class DatabaseManager:

    def __init__(self):
        self.conn = sqlite3.connect("workforce.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            emp_id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            department TEXT,
            salary REAL,
            performance REAL
        )
        """)
        self.conn.commit()

    def add_employee(self, emp):
        self.cursor.execute("""
        INSERT INTO employees VALUES(?,?,?,?,?,?)
        """,(emp.emp_id, emp.name, emp.age,
             emp.department, emp.salary, emp.performance))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()

    def delete(self, emp_id):
        self.cursor.execute("DELETE FROM employees WHERE emp_id=?",(emp_id,))
        self.conn.commit()

    def update(self, emp_id, salary):
        self.cursor.execute(
            "UPDATE employees SET salary=? WHERE emp_id=?",
            (salary, emp_id)
        )
        self.conn.commit()