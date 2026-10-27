import sqlite3

def connection_db():
    connection = sqlite3.connect("maintenance.db")
    return connection

def create_table():
    connection = connection_db()
    cursor = connection.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS machines( 
    SrNo int PRIMARY KEY AUTOINCREMENT,
    Mach_name VARCHAR(100),
    Mach_id VARCHAR(20));
    """)

def add_machines():
    connection = connection_db()
    cursor = connection.cursor()

    '''no_of_mach = int(input("How many machines are to be added\n"))
    
    for i in range(no_of_mach):
    SrNo = int(input("Sr. No: "))'''
    Mach_name = input("Machine Name: ")
    Mach_id = input("Machine Id: ")
    cursor.execute("""INSERT INTO machines
        (Mach_name, Mach_id)
        VALUES(?, ?, ?)""",
            (Mach_name, Mach_id))

    connection.commit()
    connection.close()

def view_log():
    connection = connection_db()
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM machines""")
    machines = cursor.fetchall()
    connection.close()

    for x in machines:
        print(x)
        
    print("Database displayed successfully!")

def update_machine():
    connection = connection_db()
    cursor = connection.cursor()

    a = input()
    
    cursor.execute("""UPDATE machines
        SET Mach_name = ?
        WHERE Mach_id = ?""",
        ("a", "Mach_id"))







