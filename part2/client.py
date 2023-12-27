import rpyc
import time
import os

conn = rpyc.connect("localhost", 23456)

# Global variable
CLIENT_FOLDER = "./client_files"
LAST_CHECKED_TIME = time.time()


def file_upload(name, update=False):
    '''
    Upload a file to the server
    '''
    try:
        file_path = CLIENT_FOLDER + "/" + name

        bin_data = open(file_path, 'rb').read()
        response = conn.root.file_upload(bin_data, name, update)
        print(response)
    except Exception as e:
        print(e)


def file_delete(name):
    '''
    Delete a file on the server
    '''
    response = conn.root.file_delete(name)
    print(response)


def monitor():
    '''
    Monitor file changes on the client
    '''
    print("checking for changes...")
    global LAST_CHECKED_TIME
    client_files = os.listdir(CLIENT_FOLDER)
    server_files = conn.root.show_files()

    new_files = set(client_files)-set(server_files)
    deleted_files = set(server_files)-set(client_files)

    # upload new files to server
    for file_name in new_files:
        file_upload(file_name)

    # delete files from server
    for file_name in deleted_files:
        file_delete(file_name)

    # update files on the server
    for file_name in client_files:
        if file_name not in new_files:  # if new file then ignore
            file_path = CLIENT_FOLDER + "/" + file_name
            if os.path.getmtime(file_path) > LAST_CHECKED_TIME:
                file_upload(file_name, True)

    LAST_CHECKED_TIME = time.time()


if not os.path.exists(CLIENT_FOLDER):
    os.mkdir(CLIENT_FOLDER)

while True:
    monitor()
    time.sleep(10)
