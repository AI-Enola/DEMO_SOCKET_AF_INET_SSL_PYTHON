# DEMO_SOCKET_AF_INET_SSL_PYTHON
Python demo of socket family as AF_INET using TCP with SSL.

Description : 
This is a python demo of socket IP. The server is waiting for message from client. When the client has sended his message the server reply back.

This demo were rebuild based a on parent project (PYKE NPPE). This DEMO is a lite version of the parent project

WARNING : THIS PROGRAM IS ONLY A DEMO - DOES NOT REPRESENT PROGRAM FOR PRODUCTION OR PYKE NPPE V3

Before starting the project :

You will need a dumb SSL certificate to run this demo :

        """ GENERATED SSL CERTIFICATE AND KEY USING THIS COMMAND :
            openssl req -newkey rsa:4096 \
            -x509 \
            -sha256 \
            -days 3650 \
            -nodes \
            -out example.crt \
            -keyout example.key
        """
 
Check line 46 of "server_socket.py" & line 54 "client_socket.py" if you want to change IP and PORT of the server :

    self.SERVER_INFO = [str('127.0.0.1'), int(60004)] # [0] = SERVER IP:127.0.0.1 (LOCALHOST) [1] = SERVER PORT: 60004 - Can be changed
    
To start the server :

    python3 server_socket.py
    
  
  
To start the client : 

    python3 main.py


2022-01-22

Public Version

Version : 3.0 (Public Version of code from PYKE NPPE V3)
  
