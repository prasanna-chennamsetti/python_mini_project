from datetime import datetime
#def register()
print("WELCOME TO VOTING REGISTRATION SYSTEM")
def register(n):
    #n = int(input("Enter your age : "))
    if n<18:
        print("You are not eligible for Voting Registration")
    else:
        print("Enter your first name: ")
        fname=input()
        print("Enter yout lastname : ")
        lname=input()
        #print("Enter your Date Of Birth : ")
        #dobstr=input()
        #dob=datetime.strptime(dobstr,"%d-%m-%y")
        print("Enter your gender : ")
        gender=input()
        print("Enter your aadhar number : ")
        aadhar=int(input())
        print("Enter your village : ")
        village=input()
        print("Enter your state : ")
        state=input()
        print("Enter your pincode : ")
        pin=int(input())
        print("THANK YOU FOR REGISTERING")
        file = open("Voters.txt", "r")
        Counter = 0

        # Reading from file
        Content = file.read()
        CoList = Content.split("\n")

        for i in CoList:
            if i:
                Counter += 1

        print("The number of people registered for voting are : ", Counter)

register(int(input("Enter your age : ")))


