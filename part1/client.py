import rpyc
import random

conn = rpyc.connect("localhost", 12345)

# Global variable
CLIENT_FOLDER = "./client_files"
threads = {}  # Keeping track for threads status


def generate_random_id(action):
    return action + "_" + str(random.randint(1, 100))


def file_upload():
    '''
    Upload a file to server
    '''
    try:
        name = input("Please enter file name to upload: ")
        file_path = CLIENT_FOLDER + "/" + name

        bin_data = open(file_path, 'rb').read()  # Read file as binary
        # make remote function as asynchronous
        file_upload_async = rpyc.async_(conn.root.file_upload)
        response = file_upload_async(bin_data, name)

        thread_id = generate_random_id("file_upload")
        threads[thread_id] = response
        print("File upload action has been added to thread with id: " + thread_id)
        input("\nPlease enter any key to continue.")
    except Exception as e:
        print(e)
        input("\nPlease enter any key to continue.")


def file_rename():
    '''
    Rename file in server
    '''
    old_name = input("Please enter the file name to rename: ")
    new_name = input("Please enter new file name: ")

    rename_file_async = rpyc.async_(conn.root.file_rename)
    response = rename_file_async(old_name, new_name)

    thread_id = generate_random_id("file_rename")
    threads[thread_id] = response
    print("File rename action has been added to thread with id: " + thread_id)
    input("\nPlease enter any key to continue.")


def file_download():
    '''
    Download file from server
    '''
    name = input("Please enter the file name to download: ")
    response = conn.root.download(name)

    if (response["error"] is not None):
        print(response["error"])
    else:
        file_path = CLIENT_FOLDER + "/" + name
        with open(file_path, 'wb') as f:
            f.write(response["data"])

        print("File download successfully")
    input("\nPlease enter any key to continue.")


def file_delete():
    '''
    Delete file from server
    '''
    name = input("Please enter the file name to delete: ")
    delete_file_async = rpyc.async_(conn.root.file_delete)
    response = delete_file_async(name)

    thread_id = generate_random_id("file_delete")
    threads[thread_id] = response
    print("File delete action has been added to thread with id: " + thread_id)
    input("\nPlease enter any key to continue.")


def show_files():
    '''
    List all files on the server
    '''
    files = conn.root.show_files()
    if len(files) == 0:
        print("No files found on the server!")
    else:
        print("Files on the server")
        for file in files:
            print(f"-- {file}")
    input("\nPlease enter any key to continue.")


def check_result():
    '''
    Check status of a thread
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
    print("[1] Upload a file from client to server")
    print("[2] Rename a file on the server")
    print("[3] Download a file from server")
    print("[4] Delete a file from server")
    print("[5] Show all uploaded file")
    print("[6] Show thread result using a thread id")
    print("[0] Exit the program")
    print("==========================================")


while True:
    menu()
    try:
        option = int(input("Enter your option: "))

    except ValueError:
        print("INVALID: Please enter a number 1-6")
        continue

    if option == 1:
        file_upload()

    elif option == 2:
        file_rename()

    elif option == 3:
        file_download()

    elif option == 4:
        file_delete()

    elif option == 5:
        show_files()

    elif option == 6:
        check_result()

    elif option == 0:
        print("Exiting client service...")
        exit()

    else:
        print("INVALID: Please enter a number 1-6")
