import SP3

header = """
    ################################
       #### S2 - More FFMPEG ####
    ################################
     ## Made by Víctor Zaldívar ##"""

main_options = """
What do you want to do?
    1.- Convert Video codecs of BBB video
    2.- Video codecs comparasion
    3.- 
    4.- 
    0.- Exit"""

def show_menu():

    print(header)
    a=0

    exit_game = False
    while not exit_game:
        print(main_options)

        selected_option = input()
        if selected_option == "0":
            exit_game = True

        elif selected_option == "1":
            SP3.SP3.convertVideoContainer(a)

        elif selected_option == "2":
            SP3.SP3.twoVideoComparasion(a)

        elif selected_option == "3":
            print("no solution:(")

        elif selected_option == "4":
            print("no solution:(")

        else:
            print("This is not a valid option! Let's try again...")


if __name__ == '__main__':
    show_menu()