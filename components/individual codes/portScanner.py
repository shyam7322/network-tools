import socket, threading
from datetime import datetime

def PortScanner(host_ip = '172.217.1.164'):

        connections = []        # To run connections at the same time
        result = {}         # all
        OpenPorts = []

        # translate hostname to IPv4 
        ip = socket.gethostbyname(host_ip) 

        #prints status block of target and when the scan starts
        print("-" * 50) 
        print("Scanning: " + ip) 
        print("Scanning began at: " + str(datetime.now()).split('.')[0])
        print("**approximate runtime is 1 minute 30 seconds**") 
        print("-" * 50) 
        
        # Spawning threads to scan ports
        for a in range(65535):
                t = threading.Thread(target=TCP_connect, args=(ip, a, result))
                connections.append(t)

        # Starting threads
        for b in range(65535):
                connections[b].start()

        # wait until all threads complete
        for c in range(65535):
                connections[c].join()

        # Printing open ports
        for d in range(65535):
                if result[d] == 'open':
                    print("Port",d,'is',result[d])
                    OpenPorts.append(d)
        
        #print open ports in a list
        print("\nThe Open Ports are:",OpenPorts)
        
        #prints finish time
        print("\nScanning has finished at ",str(datetime.now()).split('.')[0])

def TCP_connect(ip, port, result):
        TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        TCPsock.settimeout(1)
        try:
                TCPsock.connect((ip, port))
                result[port] = 'open'
        except:
                result[port] = ''

host_ip = input("Enter host IP: ")
PortScanner(host_ip)
