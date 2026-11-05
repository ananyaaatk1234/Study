import sqlite3
from werkzeug.security import generate_password_hash

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

    cursor.execute("""CREATE TABLE IF NOT EXISTS admin_log(
        srno INTEGER PRIMARY KEY AUTOINCREMENT,
        Employee_Name TEXT NOT NULL,
        Username INTEGER NOT NULL UNIQUE,
        Password TEXT NOT NULL,
        Role TEXT NOT NULL);
        """)

    connection.commit()
    connection.close()
    

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
        VALUES(?, ?)""",
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

    connection.commit()

    connection.close()

def delete_machine(Mach_id):

    connection = connection_db()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM machines
        WHERE Mach_id = ?
    """, (Mach_id,))

    connection.commit()
    '''if cursor.rowcount > 0:
        print("Machine deleted successfully!")
    else:
        print("Machine ID not found.")'''
    connection.close()


def add_user(name, username, password, role):
    connection = connection_db()
    cursor = connection.cursor()

    role = role.strip().lower()

    if role not in ["employee", "manager", "admin"]:
        connection.close()
        return "Invalid Role"

    try:
        hashed_password = generate_password_hash(password)
        cursor.execute("""INSERT INTO admin_log
            (Employee_Name, Username, Password, Role)
            VALUES (?,?,?,?)""",
            (name, username, hashed_password, role))

        connection.commit()
        return "User Added Successfully"

    except sqlite3.IntegrityError:
        return "Username Exists"

    finally:
        connection.close()
    
def view_user():
    connection = connection_db()
    cursor = connection.cursor()
    
    cursor.execute("""SELECT srno, Employee_Name, Username, Role FROM admin_log""")
    logs = cursor.fetchall()
    connection.close()
    
    return logs
   
    
    
def update_log(role, username):
    connection = connection_db()
    cursor = connection.cursor()
    role = role.strip().lower()

    if role not in ["employee", "manager", "admin"]:
            connection.close()
            return "Invalid "
    
    cursor.execute("""UPDATE admin_log
        SET  role = ?
        WHERE username = ?""",
        (role, username))
    connection.commit()
    connection.close()

def delete_user(username):
    connection = connection_db()
    cursor = connection.cursor()
    username = username
    cursor.execute("""DELETE FROM admin_log WHERE username = ? """, (username,))
    connection.commit()
    connection.close()











