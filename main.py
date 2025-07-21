#ATM MANAGEMENT SYSTEM
#aim
#This project is mainly for beginners
#topics:
# 1.Conditional statements
# 2.Bulit in functions
# 3.Operators

username='kiran'
password='kiran1235'

c_name=input("Enter your name:")
c_pass=str(input("Enter your password:"))

if c_name==username and c_pass==password:
    print('''
    1.Deposite
    2.withdraw
    3.ministatement
    4.exit
    ''')
    amount=50000
    option=int(input("Select your option:"))
    if option==1:
        deposite=int(input("Enter your deposited amount:"))
        amount+=deposite
        print("Total deposited amount: ",amount)
    elif option==2:
        withdraw=int(input("Enter your withdrawal amount:"))
        amount-=withdraw
        print("Total withdrawal amount: ",amount)
    elif option==3:
        print("========ATM=======")
        print("username:",username)
        print("Total amount:",amount)
        print("Thank you for visiting")
        print("==========")
    elif option==4:
        exit()
    else:
        print("please enter a correct logins")

