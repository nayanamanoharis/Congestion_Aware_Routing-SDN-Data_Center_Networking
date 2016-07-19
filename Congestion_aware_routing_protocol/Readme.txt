1. Did you use code from anywhere for your project? If not, say so. If so, say what
functions and where they are from. (Also identify this with a comment in the
source code.)

Ans: Yes i have used code for some part of my project from sources mentioned in Piazza.
The links are as follows.

TCP socket programming in python for host-controller communication. Basically, I have written a python code for the client thread in Controller which communicates with the host thread for flow information. I am using the below link for TCP communication in python.
https://wiki.python.org/moin/TcpCommunication

TCP socket communication in C programming. TCP sockets for Sender and Receiver in the host is implemented in C-programming. Also a thread is implemented in c programming to communicate with controller to send the flow info I have used Beejs tutorial and rutgers tutorials for the C-programming in TCP sockets.
http://beej.us/guide/bgnet/
http://pk.org/417/notes/sockets/index.html

Select sample program(Links from Piazza)
I have used Select function In the receiver to switch between ports and receive only in the ports in which the data is coming. This is implemented in the receiver. 
 
http://www.gnu.org/software/libc/manual/html_node/Byte-Stream-Example.html#Byte-Stream-Example
http://www.gnu.org/software/libc/manual/html_node/Server-Example.html#Server-Example 

To get the IP addresses for a particular interface in C-programming.
I have used the below link to find out the IP address of the interface to implement sender -receiver and host-controller thread.
http://stackoverflow.com/questions/4139405/how-can-i-get-to-know-the-ip-address-for-interfaces-in-c


2. Describe how you implement the sender and receiver at hosts

Sender:
    I have written two functions in sender.
    1) Command_parser()
      This function is used to read the trace files in traffic folder, which gives the flow information. This function parses the information. IP address and PORT information specified in the trace file to send the flows specified in the trace file. This function uses TCP sockets for communication.

I have read the file using a file pointer, and parsed the information using tokens, used this information to create TCP sockets. 

These sockets are used to send and receive data to and from the receiver in the other hosts.
 
Sender Receiver communication is done on 10.0.0.x IP address, where x ranges from 1 to 16 with two ports 5000 and 5001.

TCP sockets send and receive message in infinite loop.


    2) Get_flow_state()
      This function is used for host controller communication. It is use to send flow information in every host to the controller. This function uses TCP sockets for communication.

TCP sockets are created to listen on port 5000 to accept connections from the client thread in controller.
As and when client thread in the controller requests for information, this function provides the flow state. (For Project B only reachability from host to controller and vice versa is implemented.)

Host-controller communication is done on 20.0.0.x IP address, where x ranges from 1 to 16 with port 5000.

I have used few functions to get the IP address of a host by its interface for effective communication between sender-receiver and host-controller.
TCP sockets send and receive message in infinite loop.


These two functions are implemented in two different threads for parallelism. 


3. Describe the algorithm you use at the controller.

I have used ECMP (Equal Cost MultiPath) Routing in the controller.  
Equal-cost multi-path routing (ECMP) is a routing strategy where next-hop packet forwarding to a single destination can occur over multiple "best paths" which tie for top place in routing metric calculations.

Algorithm for the Controller.
Controller code is implementer with the help of Multithreading and and Inheritance. 

1) flows from hosts is sent to its particular edge switch in the same pod with a comparatively lesser priority.

2) flows from edge switch is sent to the aggregate switch in the same pod with the same priority as mentioned above.

3)flows from the aggregate switch is sent to the core switches.
flows from two aggregate switches in the same pod is sent to all the core switches. Priority same as above

4) Every core switch is connected to every pod, this makes 4 paths from every host to every other host. With a relatively higher priority.flows from every core switch is sent to their respective destination pod. i.e to the aggregate switch.

5) flows from every aggregate switch is sent to to the respective edge switch and flows from every edge switch is sent to their respective destination. This is done with a comparatively higher priority. 