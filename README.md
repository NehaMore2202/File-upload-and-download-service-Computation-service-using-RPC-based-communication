**# File-upload-and-download-service-Computation-service-using-RPC-based-communication
File upload and download service &amp; Computation service using remote procedure call (RPC) based communication**

**Introduction**
This project is implemented on Python language. We have used ` RPyC` (Remote Python Call) - a
python library for remote procedure calls (RPC). The RPyC library uses object proxying, which is
a technique to reference a remote object transparently. RPyC allows both client and the server
to serve requests because the connection is symmetric. This library also allows for synchronous
and asynchronous operations.

**Part 1**

**Implementation:**

**- server.py**
  
o Implemented a “FileServer” class which exposes file_upload, file_delete,
file_rename, file_download and show_files methods using “rpyc” method.

o FileServer class is then served using “ThereadedServer” from “rpyc” library.

**- client.py**
  
o Client uses rpyc.connect method to connect to server.

o Client provides a menu to choose an option to perform a specific task. Each task
calls a remote method asynchronously.

o We generate random id for each asynchronous call and store them, which can
later be used to check if the server has completed the task or not.

o Client will provide all the acknowledgement on terminal.

**What we learned:**

- Using Python language.
  
- How to implement RPC using RPyC library.
  
- How a client and server communicate with each other using RPC.
  
- How to create a menu driven application.
  
**What issues we faced:**

- Since this was our first attempt to implement a RPC server and client, it took us a lot of
time researching and building prototypes before we could get a working server and
client. 

**Screnshots:**

**File Upload**

![image](https://github.com/NehaMore2202/File-upload-and-download-service-Computation-service-using-RPC-based-communication/assets/154467395/a318dcb3-7e6d-4827-b005-43ef99af1982)

**File rename**

![image](https://github.com/NehaMore2202/File-upload-and-download-service-Computation-service-using-RPC-based-communication/assets/154467395/1a81595f-67e5-4af7-8331-96e1cc47dcc4)

**File download**

![image](https://github.com/NehaMore2202/File-upload-and-download-service-Computation-service-using-RPC-based-communication/assets/154467395/f0c21e0c-6c97-4481-8322-ca989e189d3f)

**File delete**

![image](https://github.com/NehaMore2202/File-upload-and-download-service-Computation-service-using-RPC-based-communication/assets/154467395/c3910037-4f15-46ce-9277-2b69c81f2d13)

**Part 2**

**Implementation:**

- In this part we added a function to monitor changes on client files every 10 second.
 
- On every loop the functions compare files from client and server and determines all the  
files that are added to client and all the files that are deleted from the client.

- All the added files are uploaded to server and all the deleted files are removed for
server.

- To check updated files, we compare last modified time of the file with last monitor time.
  
If the last modified time is later than the last monitor time, we update the file on the
server.

**What we learned:**

- How to sleep a process/thread.
  
- How to monitor a folder for changes.
  
- How to check if a file has been modified.\
  
**What issues we faced:**

- When creating a new file on client, our code was uploading the file to server and then it
was also updating the file again. To resolve it we had to add a condition to ignore
updating if the file is new.

**Screenshots:**

![image](https://github.com/NehaMore2202/File-upload-and-download-service-Computation-service-using-RPC-based-communication/assets/154467395/c44e836e-5db9-4de6-8c50-2e59d19113d0)

**Part 3**

**Implementation:**

- Created sync functions for add and sort_array operation.
  
- Created async functions for add and sort_array operation.
  
- Client provides a menu to perform different operations.
  
- To track async functions we generate random id for each of them and store them, which
is later be used to check if the server has completed the task or not.

**What we learned:**

- Sorted function in Python.
  
- Difference between asynchronous and synchronous calls.
  
**What issues we faced:**
  
- For adding two numbers, we were getting exceptions when user was providing non
integer values. To handle it we wrapped the input method in a try catch block.

- There were few limitations for using RPyC library which we didn’t knew when we started
the project. We had to find an alternate solution for resolving them.

**Screenshots:**
  
**Synchronous add**

![image](https://github.com/NehaMore2202/File-upload-and-download-service-Computation-service-using-RPC-based-communication/assets/154467395/da00abde-85cb-4a8d-8fc4-a9b97a6442f4)

**Synchronous array sort**

![image](https://github.com/NehaMore2202/File-upload-and-download-service-Computation-service-using-RPC-based-communication/assets/154467395/89313320-6359-417d-8fef-37d4757c0015)

**Asynchronous add**

![image](https://github.com/NehaMore2202/File-upload-and-download-service-Computation-service-using-RPC-based-communication/assets/154467395/5bbf310f-c06f-44b8-9304-562516732ea8)

**Asynchronous array sort**

![image](https://github.com/NehaMore2202/File-upload-and-download-service-Computation-service-using-RPC-based-communication/assets/154467395/042225ae-b84f-4c41-a3a9-f6b415ea62ee)

**Readme to run the project**

This project uses `rpyc` library to do RPC calls. This project requires python version >= 3.10.

Check if `rpyc` is installed by running the below command

**> pip list | grep rpyc**

If `rpyc` is not installed, please install by running the below command

**> pip install rpyc**

**Part 1:**

    To run server: 
    
    Open a new terminal
    
    > cd part1
    
    > python server.py # or python3 server.py

    **To run client:**
    
    Open a new terminal
    
    > cd part1
    
    > python client.py # or python3 client.py

    Please follow client prompt menu to use the program.

**Part 2:**

  **  To run server: **
    
    Open a new terminal
    
    > cd part2
    
    > python server.py # or python3 server.py

    **To run client:**
    
    Open a new terminal
    
    > cd part2
    
    > python client.py # or python3 client.py

    Add, update or delete files under part2/client_files directory. It will automatically sync changes on part2/server_files directory.

**Part 3:**

   ** To run server: **
   
    Open a new terminal
    
    > cd part3
    
    > python server.py # or python3 server.py

   ** To run client:**
   
    Open a new terminal
    
    > cd part2
    
    > python client.py # or python3 client.py

    Please follow client prompt menu to use the program.


