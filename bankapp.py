import random
import time 


def generate_acc (n):
    otp = "0"
    for i in range (n):
        otp+=str(random.choice(range(n)))
    return otp

print(generate_acc(9))

data = {}
data2 = {}
print ("*" *31)
print( "Welcome to Listin Bank!")
print ("*" *31)

while True:
    print("What would you like to do ?\n1. Login \n2. Create account \n3. Quit ")
    user_input = input("::-")

    if user_input == "2":
        print ("Enter your first name")
        first_name = input("::-")
        print ("Enter your last name")
        last_name = input("::-")
        print ("Enter your login pin")
        login_pin = input("::-")
        print ("Enter your transaction pin")
        transaction_pin = int(input("::-"))
        acc_number = generate_acc(9)

        data = {"first_name":first_name, "last_name":last_name, "login_pin":login_pin,
        "transaction_pin":transaction_pin, "balance":0}
        data2[acc_number] = data
    
        print("Creating account....")
        time.sleep(1)
        print("Completing setup....")
        time.sleep(1)
        print(f"\n Welcome {first_name} , your account has been created successfully \n your account number is {generate_acc(9)} ")

    elif user_input == "1":
        print(f"{first_name}")
        print ("Enter your account number")
        acc_number = input("::-")
        print ("Enter your login pin")
        user_pin = input("::-")
        user_acc_number = data2.get(acc_number, False)
        while True:#user_acc_number and user_pin == data["login_pin"]:
        #while acc_number and user_pin == data["login_pin"]:
            # print ("Verifying your account...")
            time.sleep(2)
            print(f"Welcome {first_name}, select \n1. Deposit \n2. Withdraw \n3. Transfer \n4. Check balance \n5 Exit ")

            user_choice = input("::-")
            if user_choice == "1":
                print("Enter deposit amount")
                amount = int (input("::-"))
                data["balance"]= data["balance"] + amount
                print ("*" *31)
                print(f"You have successfully deposited {amount}")
                print(f'Your new balance is {data["balance"]}')
                print ("*" *31)
            
            elif user_choice == "2":
                print("Enter withdrawal amount")
                amount= int(input("::-"))
                if amount >= data["balance"]:
                    print("Insufficient Funds")
                    
                else:
                    print ("*" *31) 
                    data["balance"] = data["balance"]-amount
                    print(f"You have successfully withdrawn {amount}")
                    print(f'Your new balance is {data["balance"]}')
                    print ("*" *31)

            elif user_choice == "3":
                print ("Enter receipients account number")
                acc_number = int (input("::-"))
                print ("Enter transfer amount")
                amount = int (input("::-"))
                print("Enter your transaction pin")
                pin = int(input("::-"))
                if pin ==data["transaction_pin"]:
                    data["balance"] = data["balance"]-amount
                    print ("*" *31)
                    print(f"You have successfully transferred {amount}")
                    print(f'Transfer Successful your balance is {data["balance"]}')
                    print ("*" *31)

                    if amount >= data["balance"]:
                        print ("Insufficient Funds")
                    # else: 
                        # print ("*" *31)
                        # data["balance"] = data["balance"]-amount
                        # print("You have successfully transferred{amount}")
                        # print(f'Transfer Successful your balance is {data["balance"]}')
                        # print ("*" *31)
                        
                else:
                    print ("Wrong transaction pin")

            elif user_choice == "4":
                print(f'Your balance is {data["balance"]}')
            
            elif user_choice == "5":
                break
            else:
                print ("Invalid input")
    
        #print("\nInvalid account number or login pin.")
    
    elif user_input == "3":
        break


        # while True:

    









