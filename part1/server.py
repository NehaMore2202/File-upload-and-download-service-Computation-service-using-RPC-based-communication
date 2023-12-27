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
    def file_upload(self, binary_data, name):
        try:
            # Create folder if it does not exist
            if not os.path.exists(SERVER_FOLDER):
                os.mkdir(SERVER_FOLDER)

            file_path = SERVER_FOLDER + "/" + name
            with open(file_path, 'wb') as f:
                f.write(binary_data)

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

    # Rename file on the server
    @rpyc.exposed
    def file_rename(self, name, new_name):
        try:
            old_file_path = SERVER_FOLDER + "/" + name
            new_file_path = SERVER_FOLDER + "/" + new_name

            if os.path.exists(old_file_path):
                os.rename(old_file_path, new_file_path)
            else:
                return "The file does not exist"
            return "Renamed file successfully"
        except:
            return "Unable to rename please try again"

    # Send file to client for download
    @rpyc.exposed
    def download(self, name):
        try:
            path = SERVER_FOLDER + "/" + name
            if os.path.exists(path):
                bin_data = open(path, 'rb').read()
                return {"data": bin_data, "error": None}
            else:
                return {"error": "File not found", "data": None}
        except:
            return {"error": "Unable to download", "data": None}

    # List file on the server
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


# Execution starts
if __name__ == "__main__":
    server = ThreadedServer(FileServer, port=12345)
    print("Server Started")
    server.start()
