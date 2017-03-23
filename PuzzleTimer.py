import time
import queue


last_ten = queue.Queue(maxsize=10)


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
        add_to_last_ten(solve_time)
        print("Solve time: %.3f seconds" % solve_time)

        print("Record another time? (y/n): ", end="")
        run_again = input()

        print()


def add_to_last_ten(solve_time):
    global last_ten
    if last_ten.full():
        last_ten.get()
    last_ten.put(solve_time)


def print_last_ten_times():
    global last_ten
    print("Last ten solve times:")
    for i in list(last_ten.queue):
        print("%.3f" % i)


def analytics_menu():
    analytics_menu_option = ""
    while analytics_menu_option != "0":
        print("Analytics Menu \n0 - Back to main menu \n1 - Average of last ten solve times")


if __name__ == "__main__":
    main_menu_option = ""
    while main_menu_option != "0":
        print("PuzzleTimer Menu \n0 - Quit \n1 - Timer \n2 - Analytics \nChoice: ", end="")
        main_menu_option = input()

        if main_menu_option == "1":
            print()
            timer()
        elif main_menu_option == "2":
            print()
            analytics_menu()

