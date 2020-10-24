import send
import recive


def menu():
    choice = input("""
                C: Create network
                J: Join network
                Please enter your choice (C/J):""")
    if choice == "C" or choice == "c":
        send.create_network()
    elif choice == "J" or choice == "j":
        recive.join_network()
    else:
        print("You must only select either S or R")
        print("please try again")
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()
