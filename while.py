import os
import time
choice=0
root=0
path= ''
username="root"
password="Pa$$w0rd"
inputuser=''
inputpass=''
loginchance=0
while(choice!=2):
    print("----->MENU<-----\n1) Run Program \n 2) Exit Program")
    choice = int(input("Enter an option \n"))
    if choice==1:
        while(root==0 or root>=3):         
            root=int(input("Do you want to run the program in Root Rights: \n 1: Yes \n 2. No \n"))
            while(loginchance<3):
                if root==1:
                    inputuser=input("Enter sudo user for login: \n")
                    inputpass=input("Enter sudo user password: \n")
                    if inputuser==username and inputpass==password:
                        print("Login Successfull proceeding....")
                        time.sleep(2)
                        path=input("Enter Path to program\n")
                        os.system("sudo "+path)
                        os.system("clear")
                        break
                        
                    else:
                        loginchance+=1
                        print("Incorrect Credentials Please Try Again!")
                if loginchance>=3:
                    print("Login limit exceeded....Back to main menu")
                    time.sleep(5)
                    root=0
                elif root==2:
                    path=input("Enter Path to program\n")
                    os.system(path)
                    os.system("clear")
                    break
                else:
                    print("Choice regarding permissions is invalid. Please try again")
                    root=0   
                    break
                           
    elif choice==2:
        quit()
    else:
        print("Choice is invalid. Please try again")

        
      
