import send
import recive


def main():
    while 1:
        choice = input("""
                        C: Create network
                        J: Join network
                        E:Exit
                        Please enter your choice (C/J/E):""")
        if choice == "C" or choice == "c":
            send.create_network()
        elif choice == "J" or choice == "j":
            recive.join_network()
        elif choice == "E" or choice == "e":
            exit()
        else:
            print("You must only select either S or R")
            print("please try again")


if __name__ == "__main__":
    main()
