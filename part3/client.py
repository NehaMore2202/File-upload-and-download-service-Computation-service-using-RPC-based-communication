import rpyc
import random

conn = rpyc.connect("localhost", 34567)

threads = {}  # Keeping track for threads status


def generate_random_id(action):
    return action + "_" + str(random.randint(1, 100))


def accept_user_input_int(msg):

    n = ""
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print("INVALID: Please enter a number")
            continue
        else:
            break
    return n


def find_sum_sync():
    '''
    synchronous addition
    '''
    n1 = accept_user_input_int("Please enter the first number: ")
    n2 = accept_user_input_int("Please enter the second number: ")

    sum = conn.root.find_sum(n1, n2)
    print(f"Sum of two number {n1} and {n2} is : {sum}")
    input("\nPlease enter any key to continue.")


def sort_array_sync():
    '''
    synchronous sort
    '''
    arr_str = input("Please enter values separated by space: ")
    result = conn.root.sort_array(arr_str)
    print(f"Sorted array :  {result}")
    input("\nPlease enter any key to continue.")


def find_sum_async():
    '''
    asynchronous addition
    '''
    n1 = accept_user_input_int("Please enter the first number: ")
    n2 = accept_user_input_int("Please enter the second number: ")

    add_async = rpyc.async_(conn.root.find_sum)
    response = add_async(n1, n2)

    thread_id = generate_random_id("add")
    threads[thread_id] = response

    print(
        f"Add action for {n1} and {n2} has been added to thread with id: " + thread_id)
    input("\nPlease enter any key to continue.")


def sort_array_async():
    '''
    asynchronous sort
    '''
    arr_str = input("Please enter values separated by space: ")

    array_async = rpyc.async_(conn.root.sort_array)
    response = array_async(arr_str)

    thread_id = generate_random_id("arr")
    threads[thread_id] = response

    print("Sort array action has been added to thread with id: " + thread_id)

    input("\nPlease enter any key to continue.")


def check_result():
    '''
    check status of a thread
    '''
    try:
        id = input("Please enter thread id to see the result: ")
        action_obj = threads[id]
        if action_obj.ready == True:
            print(action_obj.value)
        else:
            print(
                "Waiting for server to complete the operation. Please try again later!")
        input("\nPlease enter any key to continue.")
    except:
        print("No such thread id available")
        input("\nPlease enter any key to continue.")


def menu():
    '''
    Menu to display options (for user friendly)
    '''
    print()
    print("==========================================")
    print("[1] Synchronous add two number ")
    print("[2] Synchronous sort an array")
    print("[3] Asynchronous add two number")
    print("[4] Asynchronous sort an array")
    print("[5] Show thread result using a thread id")
    print("[0] Exit the program")
    print("==========================================")


while True:
    menu()
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("INVALID: You need to enter a number 1-6")
        continue

    if option == 1:
        find_sum_sync()

    elif option == 2:
        sort_array_sync()

    elif option == 3:
        find_sum_async()

    elif option == 4:
        sort_array_async()

    elif option == 5:
        check_result()

    elif option == 0:
        print("Exiting client service...")
        exit()

    else:
        print("Invalid option! Please choose option from 1 to 5.")
