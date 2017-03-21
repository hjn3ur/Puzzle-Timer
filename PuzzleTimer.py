import time


class PuzzleTimer:
    if __name__ == "__main__":
        # Spacebar would be more ideal, but this is easier than adding a key listener for now
        print("Press enter to start timing", end="")
        input()
        starting_time = time.time()

        print("Press enter to stop timing", end="")
        input()
        ending_time = time.time()

        print(ending_time - starting_time)
