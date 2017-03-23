import time


def timer():
    run_again = ""
    while run_again != "n":
        # Spacebar would be more ideal, but this is easier than adding a key listener for now
        print("Press enter to start timing", end="")
        input()
        starting_time = time.time()

        print("Press enter to stop timing", end="")
        input()
        ending_time = time.time()

        solve_time = ending_time - starting_time
        print("Solve time: %.3f seconds" % solve_time)

        print("Record another time (y/n): ", end="")
        run_again = input()

        print()

if __name__ == "__main__":
    menu_option = ""
    while menu_option != "0":
        print("PuzzleTimer Menu \n0 - quit \n1 - Timer \nChoice: ", end="")
        menu_option = input()

        if menu_option == "1":
            print()
            timer()

