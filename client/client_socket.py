"""
Author : LA
Title : Demo of Python Socket - Socket Client
Description : Client socket connect to server socket
Version : 3.0 (Public Version of code from PYKE NPPE V3)
OS : Linux & macOS
Updated : 2022-01-22

WARNING : THIS PROGRAM IS ONLY A DEMO - DOES NOT REPRESENT PROGRAM FOR PRODUCTION OR PYKE NPPE
"""
# Python library
import socket
import ssl


class Client_Socket:
    """
        client_socket as class variable using self
        logger as class object using self
        Set server info IP & PORT
        
        Connect to server
             
    """
    
    
    def __init__(self, logger=object) -> None:
        """
        Init Socket and logger
        Set server info IP & PORT
        
        Return None
        """
        
        self.logger = logger
        
        self.logger.info("[CLIENT SOCKET] - Init socket...")
        self.server_socket = socket.socket()
        self.server_info = [str('127.0.0.1'), int(60004)] # [0] = SERVER IP  [1] = SERVER PORT - Can be changed

    
    def connect_to_server(self) -> object:
        """
        Wrap SSL with Server Socket
        Connect to server
        Exception raised when connect to server failed
        
        Return self.server_socket as object
        """
        
        self.logger.info("[CLIENT SOCKET] - Connecting to server...\nWrapping SSL with server socket")
        self.server_socket = ssl.wrap_socket(self.server_socket, ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        
        try: self.server_socket.connect((self.server_info[0], self.server_info[1]))
        
        except socket.error:
            self.logger.error(f"[CLIENT SOCKET] - Connecting to server FAILED!\n{socket.error}")
            raise
        
        self.logger.info(f"[CLIENT SOCKET] - Connection initiate with Server : {self.server_info[1]}")
        
        return self.server_socket