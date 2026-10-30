import prac

prac.create_table()

ex = True
eb = True

while ex:


    x = int(input("To Add Machines: Press 1\n To View Database: Print 2\n To Update the Status: Press 3\n To Exit: Press 4\n"))

    if x == 1:
        mach_count = int(input("No. of Machines to be Added: \n"))
        for i in range(mach_count):
            prac.add_machines()

    elif x == 2:
        prac.view_log()

    elif x == 3:
        upd_count = int(input("Update Database:\n To Update Entries: Press 1\n To Delete Entries: Press 2\n"))

        if upd_count == 1:
            mach_id = input("Machine Id: ")
            mach_name = input("\nUpdated Name is:\n")

            if mach_name == "":
                mach_name = None
                
            prac.update_machine(mach_id, mach_name)

        elif upd_count == 2:
            mach_id = input("Machine Id: ")
            prac.delete_machine(mach_id)

        else:
            print("Invalid Input")

    elif x == 4:
        ex = False

    else:
        print("Invalid Input")

while eb == True:
    user = int(input("To Add Users: Press 1\n To Update Users: Press 2\n To Delete Users: Press 3\n To View Users: Press 4\n"))

    if user == 1:
        prac.add_user()

    elif user == 2:
        username = ("Search by Username: \n")
        role = input("Enter the Updated Role:\n")
        prac.update_log(role, username)

    elif user == 3:
        usern = int(input(""))
        
        

