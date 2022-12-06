                                    #Bakery Management System
                                       #Administration Menu
                                         #EMPLOYEE RECORD

#Username: Admin   & Password: 12345

Employee_No = []
Employee_Name = []
Employee_Phonenumber = []
Employee_Address = []

def Add_Employee_Record():
    n = int(input("Enter the number of records you want to print: "))
    for count in range(n):
        Employee_No.append(input("Enter the Employee number: "))
        Employee_Name.append(input("Enter the Employee Name: "))
        Employee_Phonenumber.append(input("Enter the Employee Phone Number: "))
        Employee_Address.append(input("Enter the Employees Address: "))
    return()

def View_Employee_Record():
    print("Employee No. \t\t Employee Name \t\t Employee Phone number \t\t Employee Address")
    for count in range(0 , len(Employee_No)):
        print("\t", Employee_No[count], "\t\t", Employee_Name[count], "\t\t", Employee_Phonenumber[count], "\t\t", Employee_Address[count])

def search_Employee_Record():
    Search_Flag = 0
    search = input("\nSearch Employee No or Employee Name: ")
    count = 0
    while count < len(Employee_No):
        if search == Employee_No[count] or search == Employee_Name[count]:
            print("\n")
            print("Employee No. \t\t Employee Name \t\t Employee Phone number \t\t Employee Address")
            print("\t", Employee_No[count], "\t\t", Employee_Name[count], "\t\t", Employee_Phonenumber[count], "\t\t", Employee_Address[count])
            Search_Flag = 1
        count += 1
    if Search_Flag != 1:
        print("\n Record not Found!!")

def Update_Employee_Record():
    Update_Flag = 0
    search = input("Search Employee No or Employee Name: ")
    count = 0
    while count < len(Employee_No):
        if search == Employee_No[count] or search == Employee_Name[count]:
            Employee_No[count] = input("Enter Employee Number: ")
            Employee_Name[count] = input("Enter Employee Name: ")
            Employee_Phonenumber[count] = input("Enter Employee Phone Number: ")
            Employee_Address[count] = input("Enter Employee Address: ")
            print("\n\t\t\t Employee Menu successfully Updated")
            Update_Flag = 1
        count +=1
    if Update_Flag !=1:
        print("Record Not Found!")
    return()

                                                  
Dish_No = []  
Dish_Name = []
Dish_Quantity = []
Dish_Price = []

def Add_Dish_Record(): 
    n = int(input(
        "Enter the number of Dish Records you want to enter: "))
    for count in range(n):  
        Dish_No.append(input("Enter Dish No: ")) 
        Dish_Name.append(input("Enter Dish Name: "))
        Dish_Quantity.append(input("Enter Dish Quantity: "))
        Dish_Price.append(input("Enter Dish Price: "))
    return ()  


def View_Dish_Record():  
    print("Dish No \t\t Dish Name \t\t Dish Quantity \t\t Dish Price")
    for count in range(0, len(Dish_No)):  
        print("\t", Dish_No[count], "\t\t", Dish_Name[count], "\t\t", Dish_Quantity[count], " \t\t", Dish_Price[count])


def Search_Dish_Record(): 
    Search_Flag = 0  
    search = input("\nSearch Dish No or Dish Name: ")  
    count = 0
    while count < len(Dish_No): 
        if search == Dish_No[count] or search == Dish_Name[count]:
            print("\n")  
            print("Dish No \t\t Dish Name \t\t Dish Quantity \t\t Dish Price")
            print("\t", Dish_No[count], "\t\t", Dish_Name[count], "\t\t", Dish_Quantity[count], " \t\t", Dish_Price[count])
            Search_Flag = 1 
        count += 1"hi welcome t
    if Search_Flag != 1: 
        print("\nRecord Not Found!")


def Update_Dish_Record():
    Update_Flag = 0
    search = input("Search Old Dish No or Dish Name: ")  
    count = 0
    while count < len(Dish_No):
        if search == Dish_No[count] or search == Dish_Name[count]:  
            Dish_No[count] = input("Enter New Dish Number: ")
            Dish_Name[count] = input("Enter New Dish Name: ")  
            Dish_Quantity[count] = input("Enter New Dish Quantity: ")
            Dish_Price[count] = input("Enter New Dish Price: ")
            print("\n\t\t\t Dish Menu successfully Updated")
            Update_Flag = 1  
        count += 1
    if Update_Flag != 1:  
        print("Record Not Found!")
    return ()

                           #CUSTOMER RECORD
Customer_Name = []
Customer_CNIC = []
Customer_Table_No = []


def Add_Customer_Record():  
    n = int(input("Enter the number of Customer Records you want to enter: "))  
    for count in range(n):  
        Customer_Name.append(input("Enter Customer Name: "))
        Customer_CNIC.append(input("Enter Customer CNIC: "))  
        Customer_Table_No.append(input("Enter Customer Table No: "))
    return ()


def View_Customer_Record(): 
    print("Customer Name \t\t Customer CNIC \t\t Customer Table No")
    for count in range(len(Customer_Name)):  
        print("\t", Customer_Name[count], "\t\t", Customer_CNIC[count], "\t\t", Customer_Table_No[count])


def Search_Customer_Record():  
    Search_Flag = 0  
    search = input(
        "\nSearch Customer Name or Customer Table No: ")  
    count = 0  
    while count < len(Customer_Name):  
        if search == Customer_Name[count] or search == Customer_Table_No[count]:  
            print("\n")  
            print("Customer Name \t\t Customer CNIC \t\t Customer Table No")  
            print("\t", Customer_Name[count], "\t\t", Customer_CNIC[count], "\t\t", Customer_Table_No[count])
            Search_Flag = 1  
        count += 1
    if Search_Flag != 1:  
        print("\nRecord Not Found!")

                        #ORDERS
Dish_No_Order = [] 
Dish_Name_Order = []
Dish_Quantity_Order = []
Dish_Price_Order = []

Customer_Name_Order = []
Customer_Table_No_Order = []
Customer_CNIC_Order = []


def Dish_Order():  
    Dish_Record_Flag = 0  
    Order_Flag = 0  
    search = input("\nPlace your order by entering Dish No or Dish Name: ")
    count = 0
    while count < len(Dish_Name):  
        if search == Dish_No[count] or search == Dish_Name[count]:  
            print("\n\t\t\t\t", Dish_Name[count], "is available")
            print("\n")
            print("Dish No \t\t Dish Name \t\t Dish Quantity \t\t Dish Price  \t\t Availailbility Status")
            print("\t", Dish_No[count], "\t\t", Dish_Name[count], "\t\t", Dish_Quantity[count], " \t\t", Dish_Price[count],"\t\t\t  Available")
            print("\n")
            check = 0
            check = eval(input("\nPress 1 (YES) to confirm your order or 2 (NO) to cancel: "))
            if check == 1:
                Dish_Name_Order.append(Dish_Name[count])  
                Dish_Quantity_Order = input("\nEnter the quantity of the dish you want to order: ")
                Dish_Price_Order.append(Dish_Price[count])
                print("\nOrder Successfully Placed")
                Order_Flag = 1  
                Dish_Record_Flag = 1  
                
            else:  
                print("Order Cancelled")
                Order_Flag = 1
                break  
        count += 1

    if Order_Flag != 1: 
        count = 0  
        while count < len(Dish_Name):  
            if search != Dish_No[count] or search != Dish_Name[count]:  
                print("\n")  
                print(search, "is not present in the records")
                check = 0  
                check = eval(input("\nPress 1 (YES) to continue and add Dish Record or 2 (NO) to cancel: "))
                if check == 1:  
                    Dish_No.append(input("Enter Dish No: "))  
                    Dish_Name.append(input("Enter Dish Name: "))
                    Dish_Quantity.append(input("Enter Dish Quanity: "))
                    Dish_Price.append(input("Enter Dish Price: "))
                    print("\nDish added to the MAIN DISH MENU successfully")
                    print("\nPress 2 to place your order: ")
                    Order_Flag = 1  
                    break  
                else:  
                    print("Order cancelled")
                    Order_Flag = 1  
                    break  
            count += 1

    if Dish_Record_Flag != 1 and Order_Flag != 1:  
        print("\nYou must add at least 1 Dish record to place your order")
        check = 0  
        check = eval(input("\nDo You Wish to Add Dish Record? \nEnter 1 (YES) to proceed or 2 (NO) to cancel: "))
        if check == 1:  
            Add_Dish_Record()  
            print("\nDish Record added successfully.")
            print("\nPress 2 if you wish to place your order")
        else:  
            print("\nOrder Cancelled")


def Place_Your_Order():  
    Customer_Record_Flag = 0  
    Customer_Flag = 0  
    search = input("\nEnter Your Table No or Name: ")
    count = 0
    while count < len(Customer_Name):  
        if search == Customer_Name[count] or search == Customer_Table_No[count]:
            Customer_Name_Order.append(Customer_Name[count])
            Customer_Table_No_Order.append(Customer_Table_No[count])
            Customer_CNIC_Order.append(Customer_CNIC[count])
            Customer_Flag = 1  
            Customer_Record_Flag = 1  
            Dish_Order()  
            break
        count += 1

    if Customer_Flag != 1:  
        count = 0  
        while count < len(Customer_Name):  
            if search != Customer_Name[count] or search != Customer_Table_No[count]:
                print("\nYour Record is not available")
                check = 0  
                check = eval(input("\nDo you wish to Enter your Record? \n\nEnter 1 (YES) to proceed or 2 (NO) to cancel?: "))
                if check == 1:  
                    Customer_Name.append(input("Enter Your Name Again: "))
                    Customer_Table_No.append(input("Enter Your Table No: "))
                    Customer_CNIC.append(input("Enter Your CNIC: "))
                    print("\nCustomer Record added successfully")
                    Customer_Flag = 1  
                    Customer_Record_Flag = 1  
                    print("\nPress 2 to place your order: ")
                    break
                else:
                    print("\nYou have cancelled your order as customer record is not added")
                    Customer_Flag = 1  
                    break  
            count += 1

    if Customer_Record_Flag != 1 and Customer_Flag != 1:
        print("\nYou must add at least 1 Customer record to place your order")
        check = 0  
        check = eval(input("\nDo You Wish to Add Customer Record? Enter 1 (YES) to proceed or 2 (NO) to cancel: "))
        if check == 1:  
            Add_Customer_Record()  
            print("\nCustomer Record added successfully. \nPress 2 if you wish to place your order")
        else:  
            print("\nOrder Cancelled")


def View_Order_Details():  
    print("Dish Name \t\t Dish Quantity \t\t Dish Price  \t\t Customer Name  \t\t Customer Table No  \t\t Customer CNIC Number")
    count = 0  
    while count < len(Dish_Quantity_Order) and count < len(
            Customer_Name_Order):  
        print(Dish_Name_Order[count], "\t\t", Dish_Quantity_Order[count], "\t\t", Dish_Price_Order[count], "\t\t",
              Customer_Name_Order[count], "\t\t\t", Customer_Table_No_Order[count], "\t\t", Customer_CNIC_Order[count])
        count += 1

                                 #REPORT AND FEEDBACK
Report_No = []
Report = []

def Add_Report():
    n = int(input("Enter the number of reports or feedback you want to submit: "))
    for count in range(n):
        Report_No.append(input("Enter the report or feedback number: "))
        Report.append(input("Submit your report or feedback: "))
    return()

def View_Report():
    print("Report No. \t\t\t\t\t Report & Feedback")
    for count in range(0, len(Report_No)):
        print("\t", Report_No[count], "\t", ":", "\t", Report[count])

def Search_Report():
    Search_Flag = 0
    search = input("\nSearch Reports or Feedback: ")
    count = 0
    while count < len(Report_No):
        if search == Report_No[count]:
            print("\n")
            print("Report No. \t\t\t\t\t Report & Feedback")
            print("\t", Report_No[count], "\t", ":", "\t", Report[count])
            Search_Flag = 1
        count += 1
    if Search_Flag != 1:
        print("\n No Reports or Feedback Found!!")


print("Project By: Haseeb & Noor   Username: Admin, Password: 12345\n")
print("\t\t\t\" BAKERY MANAGEMENT SYSTEM \"\n")



for i in range(4):
    print("\n\t\t\t     ***CHOCO AND TURO***")
    print("\n\t\t\t\t   LOGIN")
    user_name = (input("Username:  "))
    password = (input("Password: "))
    j = 4
    if (user_name == "Admin") and (password == "12345"):
        print("\n\t\t\t     Access Granted!")

        check1 = 0  
        flag = 0  
        Order_Flag = 0  

        while check1 != 6: 
            print("\n\n\t\t\tBAKERY MANAGEMENT SYSTEM")  
            print("\n\t\t\t\tMAIN MENU")
            print("1. Administration \n2. Dish Menu \n3. Customer Record \n4. Order \n5. Reports & Feedback \n6. Exit") 
            check1 = eval(input("Please select one of the above options : "))  

            if check1 == 1:
                print("\n\n\t\t ADMINISTRATION MENU")
                print("\n\t\t\t***LOGIN***")

                user_name = (input("Username:  "))
                password = (input("Password: "))

                if (user_name == "Admin") and (password == "12345"):
                    print("\n\t\t\tAccess Granted!")

                    check = 0
                    while check != 5:
                        print("\n\n**** Employee Record ****")
                        print("1. ADD Employee Record \n2. VIEW Employee Record \n3. SEARCH Employee Record \n4. UPDATE Employee Record \n5. EXIT (Return to Main Menu)")
                        check = eval(input("\nPlease select one of the above options : "))
                        if check == 1:
                            print("\n\t\t\t ADD Employee Record \n")
                            Add_Employee_Record()
                            flag = 1

                        elif check == 2:
                            print("\n\t\t\t VIEW Employee Record \n")
                            if flag == 1:
                                print("\n\n\t\t\t View Employee Record")
                                View_Employee_Record()
                            else:
                                print("Employee Record Not Entered!")

                        elif check == 3:
                            print("\n\t\t\t SEARCH EMPLOYEE RECORD \n")
                            if flag == 1:  
                                search_Employee_Record()
                            else:
                                print("Employee Record Not Entered!")

                        elif check == 4:
                            print("\n\t\t\t UPDATE EMPLOYEE RECORD \n")
                            if flag == 1:
                                Update_Employee_Record()
                            else:
                                print("\nEmployee Record Not Entered!")

                        elif check == 5:
                            print("\t\t\t Employee Record Exited\n")

                        elif check != 5:  
                            print("\t\t\t Please Select one of the given options \n")

                else:
                    print("\n\t\t\tAccess Denied!")
                    print("\n\t\t\tBack to main Menu")


            if check1 == 2:  
                check = 0  
                while check != 5:  
                    print("\n\n\t\t\t Dish Main Menu")
                    print("1. ADD Menu \n2. VIEW Menu \n3. SEARCH Menu \n4. UPDATE Menu \n5. EXIT (Return to Main Menu)")
                    check = eval(input("\nPlease select one of the above options : "))  

                    if check == 1:  
                        print("\n\t\t\t ADD DISH MENU \n")
                        Add_Dish_Record()  
                        flag = 1  

                    elif check == 2:  
                        print("\n\t\t\t VIEW DISH MENU \n")
                        if flag == 1:  
                            print("\n\n\t\t\t View Dish Menu")
                            View_Dish_Record()  
                        else:  
                            print("Dish Menu Not Entered!")

                    elif check == 3:  
                        print("\n\t\t\t SEARCH DISH MENU \n")
                        if flag == 1:  
                            Search_Dish_Record()  
                        else:  
                            print("Dish Menu Not Entered!")


                    elif check == 4:  
                        print("\n\t\t\t UPDATE DISH MENU \n")
                        if flag == 1:
                            Update_Dish_Record()
                        else:  
                            print("\nDish Menu Not Entered!")

                    elif check == 5:  
                        print("\t\t\t Dish Menu Exited\n")
                    elif check != 5:  
                        print("\t\t\t Please Select one of the given options \n")

                        # Customer Record

            if check1 == 3:  
                check = 0  
                while check != 4:  
                    print("\n\n\t\t\t  Customer Records \n")
                    print(
                        "\n1. Add Customer Record \n2. View Customers Record \n3. Search Customer Record \n4. EXIT (Return to Main Menu)")
                    check = eval(input("\nPlease select one of the above options : "))

                    if check == 1:  
                        print("\n\t\t\t Add Customer Record \n")
                        Add_Customer_Record()  
                        flag = 1  

                    elif check == 2:  
                        print("\n\t\t\t View Customer Record \n")
                        if flag == 1:
                            View_Customer_Record()  
                        else:  
                            print("Customers Record Not Entered!")

                    elif check == 3:  
                        print("\n\t\t\t SEARCH Customer Records \n")
                        if flag == 1:
                            Search_Customer_Record()  
                        else:  
                            print("Customer Record Not Entered!")

                    elif check == 4:
                        print("\n\t\t\t\tCustomer Menu Exited")

                    elif check != 4:  
                        print("\t\t\t Please Select one of the given options \n")

                        # Order Records

            if check1 == 4:  
                check = 0  
                while check != 4:  
                    print("\n\t\t\t  Order Menu \n")
                    print("1. View Dish Menu \n2. Place Your Order \n3. View Order \n4. EXIT (Return to Main Menu)")
                    check = eval(input("Please select one of the above options : "))  

                    if check == 1:  
                        print("\n\t\t\t\t VIEW DISH MENU \n")
                        if flag == 1:
                            print("\n\n\t\t\t View Dish Menu")
                            View_Dish_Record()
                        else:  
                            print("Dish Menu Not Entered!")

                    elif check == 2:  
                        print("\n\t\t\t\tPlace Your Order")
                        if flag == 1:  
                            print("\n\n\t\t\t Place Your Order")
                            Place_Your_Order()
                            Order_Flag = 1
                        else:
                            print("\nOrder not placed as no record has been entered")


                    elif check == 3:
                        print("\n\t\t\t\tView Your Order")
                        if Order_Flag == 1:  
                            print("\n\n\t\t\t View Your Order")
                            View_Order_Details()
                        else:  
                            print("\nOrder not placed!")

                    elif check == 4:  
                        print("\n\t\t\t\tOrder Menu Exited")

                    elif check != 4:
                        print("\n\t\t\t Please Select one of the given options \n")

            if check1 == 5:
                print("\n\n\t\t\t REPORTS & FEEDBACKS")
                check = 0
                while check != 4:
                    print("1. ADD REPORT OR FEEDBACK \n2. VIEW REPORT OR FEEDBACK \n3. SEARCH REPORT OR FEEDBACK \n4.EXIT (Return to Main Menu)")
                    check = eval(input("\nPlease select one of the above options : "))
                    if check == 1:
                        print("\n\t\t\t ADD REPORT OR FEEDBACK\n")
                        Add_Report()
                        flag = 1

                    elif check == 2:
                        print("\n\t\t\t VIEW REPORTS & FEEDBACKS\n")
                        if flag == 1:
                            print("\n\n\t\t\t View Report & feedback")
                            View_Report()
                        else:
                            print("No Reports or feedback Entered!")

                    elif check == 3:
                        print("\n\t\t\t SEARCH REPORTS OR FEEDBACKS\n")
                        if flag == 1:
                            Search_Report()
                        else:
                            print("No Report or Feedback Entered!")


                    elif check == 4:
                        print("\t\t\t Report & Feedback Exited\n")
                        break
                    elif check != 4:
                        print("\n\t\t\t Please Select one of the given options \n")

            elif check1 == 6:
                print("\n\t\t\tProgram terminated successfully!\n\n")
                break

    else:
        ans = j-i-1
        print("""
        \t\tIncorrect Password! Try Again!
        \t\t\tChances left""", j-i-1)

        if ans == 0:
            print("\t\t\t\tACCESS DENIED!!")
