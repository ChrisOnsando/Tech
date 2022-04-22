import sqlite3

conn = sqlite3.connect('employee_db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS employees(firstname TEXT, secondname TEXT, paycheck REAL)')
def data_entry():
    c.execute("INSERT INTO employees VALUES",
    (
        'Nemwel',
        'Onsando', 
        200000
    ),
    (
        'Chris',
        'Onsando',
        202100
    ),
    (
        
        'Chris',
        'Junior',
        1002100
    ))

    conn.commit()
    conn.close()
    create_table()
    data_entry()
