import receive
import send


def main():
    while True:
        choice = input("\tC: Create network\n\tJ: Join network\n\tE:Exit\nPlease enter your choice (C/J/E):")
        if choice == "C" or choice == "c":
            send.create_network()
        elif choice == "J" or choice == "j":
            receive.join_network()
        elif choice == "E" or choice == "e":
            exit()
        else:
            print("You must only select either S or R")
            print("please try again")


if __name__ == "__main__":
    main()