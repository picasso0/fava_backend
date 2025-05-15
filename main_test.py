import pyodbc

def get_db_connection():
    return pyodbc.connect(
        "Driver={SQL Server};"
        "Server=localhost;"
        "Database=ActoDB;"
        "Trusted_Connection=yes;"
    )

def get_all_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    #cursor.execute("SELECT * FROM sys.tables")
    cursor.execute("SELECT * FROM Opr.Comp ")
    tables = cursor.fetchall()
    cursor.close()
    conn.close()
    return tables

if __name__ == "__main__":
    tables = get_all_tables()
    print("Tables in ActoDB:")
    for table in tables:
        print(table)