#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv)==2:
        target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
        print("Invalid amount of arguments.")
        print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 58)
print("Scanning target: " +target)
print("Time started: " +str(datetime.now()))
print("-" * 58)

try:
        for port in range(50, 85):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #gathering ipv4 and port connecting to
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target, port))#error indicator is the s.connect_ex
                if result == 0:
                        print (f"Port {port} is open.")
                        s.close()
       
except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

except socket.error:
        print("Could not connect to server.")
        sys.exit()
       
