print("please insert your ATM")
print("Welcome to SBI")
balance=50000
pin=1234
# pin_code=int(input("enter the pin"))
# if pin_code==pin:
#     print("select your choice")
# else:
#     print("wrong pin,try again")
def ATM(**choice):
    print("1=cash_withdrawal")
    print("2=balance_enquiry")
    print("3=deposite")
    print("4=pin_generation")
    print("5=exit")
    choice=int(input("enter the number"))
    if choice==1:
        withdrawal=int(input("enter the ammount"))
        if withdrawal<=balance:
            print("collect your cash",withdrawal)
            print("remaining balance",balance-withdrawal)
        else:
            print("not enough cash in your account")
    elif choice==2:
        print("your balance",balance)
    elif choice==3:
        deposit=int(input("enter the amount to deposit"))
        print("total_ammount",balance+deposit)
        print("deposit successful")
    elif choice==4:
        pin_generation=int(input("enter new pin"))
        print("new pin=",pin_generation)
    elif choice==5:
        print("Thank you for visiting")
def fun():
    pin_code=int(input("enter the pin"))
    if pin_code==pin:
        print("select your choice")
        ATM()
    else:
        print("wrong pin,try again")
fun()
# ATM()
