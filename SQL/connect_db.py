import sqlite3
import pandas as pd


conn = sqlite3.connect('employee_2022')
c = conn.cursor()
c.execute('''
    SELECT * FROM employees
    '''   
)

df  = pd.DataFrame(c.fetchall(),columns=['firstname','secondname','payroll'])
print(df)