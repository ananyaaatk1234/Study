import prac

prac.create_table()

ex = True

while ex:


    x = int(input("To Add Machines: Press 1\n To View Database: Print 2\n To Update the Status: Press 3\n To Exit: Press 4\n"))

    if x == 1:
        mach_count = int(input("No. of Machines to be Added: \n"))
        for i in range(mach_count):
            prac.add_machines()

    elif x == 2:
        prac.view_log()

    elif x == 3:
        print("N/A")

    elif x == 4:
        ex = False

    else:
        print("Invalid Input")

