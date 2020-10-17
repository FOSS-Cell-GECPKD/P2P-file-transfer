import send
import recive

def menu():
    choice=input("""
                S: Send a file
                R: Receive a file
                Please enter your choice (S/R):""")
    if choice=="S" or choice=="s":
        send.send_file()
    elif choice=="R" or choice=="r":
        recive.receive_file()
    else:
        print("You must only select either S or R")
        print("please try again")
        menu()

def main():
    menu()

if __name__ =="__main__":
    main()
