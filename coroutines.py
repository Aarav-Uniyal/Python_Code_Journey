from time import sleep


# Coroutines are used to continue the process after doing a task.
# The next time the coroutine is called, it will skip the process.


def opener():
    # This will run only once.
    f = open("Coroutines.txt")
    sleep(4)
    read = f.read()

    # This will always run after running the first phase.
    while True:
        # The coroutine begins from here
        # This next line is necessary.
        text = (yield)
        if text in read:
            print("Your text is in the file.")

        else:
            print("Your text is not in the file.")


search = opener()
print("Opening the file now.")
next(search)  # This will tell the coroutine to go to the next phase.
print("Opened.")
search.send("Generators")  # Way to send an argument to a coroutine.
search.send("Aarav")
search.send("blah blah blah")
# If we close a coroutine, we have to open it again to send arguments.
search.close()
# This will throw an error as coroutine has been closed.
# search.send("Kuch bhi daal do isme")
