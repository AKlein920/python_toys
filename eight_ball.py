import time
import random

responses = ['yes', 'no', 'maybe', 'definitely', 'absolutely']
in_progress_msg = 'Thinking...'
timeout = 5


def activate_ball():
    input('Ask a question: ')
    for second in range(0, timeout):
        print(in_progress_msg)
        time.sleep(1)

        if (second == timeout-1):
            randomInt = random.randint(0, len(responses))
            print(responses[randomInt])
            ask_to_continue()


def ask_to_continue():
    continue_response = input("Would you like to ask another question? y/n: ")
    if continue_response == "y":
        activate_ball()
    else:
        print("Thanks for asking.")


activate_ball()
