from unittest import result
import rpyc
import os
from rpyc.utils.server import ThreadedServer

# Global variable
SERVER_FOLDER = "./server_files"


@rpyc.service
class FileServer(rpyc.Service):
    # Client upload file to server
    @rpyc.exposed
    def file_upload(self, binary_data, name, update=False):
        try:
            if not os.path.exists(SERVER_FOLDER):
                os.mkdir(SERVER_FOLDER)

            file_path = SERVER_FOLDER + "/" + name
            with open(file_path, 'wb') as f:
                f.write(binary_data)

            if update == True:
                return "File updated successfully"
            else:
                return "File uploaded successfully"
        except:
            return "Unable to upload file please try again"

    # Delete file from server
    @rpyc.exposed
    def file_delete(self, name):
        try:
            file_path = SERVER_FOLDER + "/" + name
            if os.path.exists(file_path):
                os.remove(file_path)
                return "File Deleted successfully"
            else:
                return "The file does not exist"
        except:
            return "Unable to delete file please try again"

    @rpyc.exposed
    def show_files(self):
        try:
            if not os.path.exists(SERVER_FOLDER):
                return []
            else:
                files = os.listdir(SERVER_FOLDER)
                return files
        except:
            return []


# Execution start
if __name__ == "__main__":
    server = ThreadedServer(FileServer, port=23456)
    print("Server Started")
    server.start()
