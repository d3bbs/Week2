import os
choice=0
path= ''
while(choice!=2):
    print("----->MENU<-----\n1) Run Program \n 2) Exit Program")
    choice = int(input("Enter an option \n"))
    if choice<=0 or choice>=3:
        print("Choice is invalid. Please try again")
    if choice==1:
        path=input("Enter Path to program\n")
        os.system(path)
    if choice==2:
        quit()
    
        
      
