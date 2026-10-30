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

def update_machine(Mach_id, Mach_name = None):

    connection = connection_db()
    cursor = connection.cursor()

        
    cursor.execute("""UPDATE machines
        SET Mach_name = COALESCE(?, Mach_name)
        WHERE Mach_id = ?""",
        (Mach_name, Mach_id))

    print("Database Updated")

def delete_machine(Mach_id):

    connection = connection_db()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM machines
        WHERE Mach_id = ?
    """, (Mach_id,))

    connection.commit()
    connection.close()


def create_table():
    connection = connection_db()
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS admin_log(
    srno int PRIMARY KEY AUTOINCREMENT,
    Employee_Name VARCHAR(100),
    Username int NOT NULL UNIQUE,
    Password TEXT NOT NULL,
    Role TEXT NOT NULL;
    """)



def add_user():
    connection = connection_db()
    cursor = connection.cursor()

    name = input(" ")
    username = int(input(" ")) 
    password = input(" ")
    role = input("")
    cursor.execute("""INSERT INTO admin_log
        (name, username, password, role)
        VALUES (?,?,?,?)""",
        (name, username, password, role))
    
def view_user():
    connection = connection_db()
    cursor = connection.cursor()
    
    cursor.execute("""SELECT * FROM admin_log""")
    logs = cursor.fetchall()
    connection.close()
    
    for x in logs:
        print(x)
            
    print("Database displayed successfully!")
    
def update_log(role, username):
    connection = connection_db()
    cursor = connection.cursor()
    b = role
    usern = username
    cursor.execute("""UPDATE admin_log
        SET  role = ?
        WHERE username = ?""",
        ("b", "usern"))

def delete_user(username):
    connection = connection_db()
    cursor = connection.cursor()
    username = username
    cursor.execute("""DELETE FROM admin_log WHERE username = ? """, ("username"))












