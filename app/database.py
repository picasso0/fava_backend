import pyodbc
import os

def get_db_connection():
    return pyodbc.connect(
        "Driver={SQL Server};"
        "Server=localhost;"
        "Database=ActoDB;"
        "Trusted_Connection=yes;"
    )
