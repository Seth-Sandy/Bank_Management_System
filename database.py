import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="14092003",
    database="bank"
)

cursor = mydb.cursor()

def createCustomerTable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers
            (username VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            name VARCHAR(20) NOT NULL,
            age INTEGER NOT NULL,
            city VARCHAR(20) NOT NULL,
            account_number INTEGER NOT NULL,
            balance INTEGER NOT NULL,
            status BOOLEAN NOT NULL)
    ''')

mydb.commit()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

if __name__ == '__main__':
    createCustomerTable()