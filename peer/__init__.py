import receive
import send


def main():
    while True:
        def choice():
            ans = input("\tC: Create network\n\tJ: Join network\n\tE:Exit\nPlease enter your choice (C/J/E):")
            if ans == "C" or ans == "c":
                send.create_network()
            elif ans == "J" or ans == "j":
               receive.join_network()
            elif ans == "E" or ans == "e":
               exit()
            else:
                print("You must only select either S or R")
                print("please try again")
        choice()

if __name__ == "__main__":
    main()
