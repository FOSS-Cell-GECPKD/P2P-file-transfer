import server
import client

def menu():
    choice=input("""
                S: Send a file
                R: Receive a file
                Please enter your choice (S/R):""")
    if choice=="S" or choice=="s":
        server.send_file()
    elif choice=="R" or choice=="r":
        client.receive_file()
    else:
        print("You must only select either S or R")
        print("please try again")
        menu()

def main():
    menu()
    ans=input("Do you want to continue [y/n]? ")
    if ans=="Y" or ans=="y":
        main()

main()
