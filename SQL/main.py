import sqlite3

conn = sqlite3.connect('employee_2022')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS employees(firstname TEXT, secondname TEXT, paycheck REAL)')
def data_entry():
    c.execute("INSERT INTO employees VALUES('Nemwel', 'Chris', 56000)")
    conn.commit()
    conn.close()
create_table()
data_entry()
