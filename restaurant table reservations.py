available_tables=[1,2,3,4,5]
requested_table=int(input("Enter the table number you want to reserve:"))
if requested_table in available_tables:
    print("The table is available for reservation")
else:
    print("The table is already reserved")