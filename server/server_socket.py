"""
Author : LA
Title : Demo of Python Socket - Socket Server
Description : Server socket wait for client message and reply the message back to the client.
Version : 3.0 (Public Version of code from PYKE NPPE V3)
OS : Linux & macOS
Updated : 2022-01-22

WARNING : THIS PROGRAM IS ONLY A DEMO - DOES NOT REPRESENT PROGRAM FOR PRODUCTION OR PYKE NPPE V3
"""


# Python Library
import socket
import ssl

# Custom library
from session import Client_Session
from log import Log


class Server:
    """
        Create the socket with family type, server infos, SSL.
        Bind socket and accept new clients.
        Clients are direct to is own thread in Client_Session class.

    """
    
    
    def __init__(self) -> None:
        
        """
        Init Socket and SSL
        Socket Parameters : INET - IP: 127.0.0.1 - PORT:60004 (CAN BE CHANGED)
        Exception raised when creating socket failed
        Return None
        """
        # Init logger
        log = Log(log_in_file=True, log_in_console=True, encoding='utf-8', filename='./log.txt', filemode='a', logger_name='DEMO SOCKET PYTHON', format='%(name)s - %(asctime)s - %(levelname)s: %(message)s')
        self.logger = log.get_logger() # Get logger object
        
        
        self.logger.info("[SERVER SOCKET] - Init demo socket...")
        
        self.SERVER_INFO = [str('127.0.0.1'), int(60004)] # [0] = SERVER IP  [1] = SERVER PORT - Can be changed
        
        """ GENERATED SSL CERTIFICATE AND KEY USING THIS COMMAND :
            openssl req -newkey rsa:4096 \
            -x509 \
            -sha256 \
            -days 3650 \
            -nodes \
            -out example.crt \
            -keyout example.key
        """
        SSL_CERTIFICATE = 'example.crt'
        SSL_KEY = 'example.key'

        self.logger.info("[SERVER SOCKET] - Creating socket...")
        try :
            # Create Socket as AF_INET= IPV4/6 & SOCK_STREAM = TCP
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
        except socket.error:
            self.logger.error(f"[SERVER SOCKET] - Creating socket FAILED !\n {socket.error}")
            raise
        
        # Implementing SSL
        self.logger.info("[SERVER SOCKET] - Creating SSL context...")
        self.CONTEXT = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        self.CONTEXT.load_cert_chain(SSL_CERTIFICATE, SSL_KEY, password=None) # We generated a non password SSL certificates and key for lab purpose
        
        self.logger.info("[SERVER SOCKET] - Socket init done.")
        
            
    def bind(self) -> None:
        
        """
        Try to bind with server info
        Wraapping socket with SSL context
        Exception raised when binding failed
        
        Return None
        """
        
        self.logger.info("[SERVER SOCKET] - Starting binding...")
        
        try: self.server_socket.bind((self.SERVER_INFO[0], self.SERVER_INFO[1]))
        
        except socket.error:
            
            self.server_socket.close()
            self.logger.error(f"[SERVER SOCKET] - Binding socket FAILED !\n {socket.error}")
            raise
        
        self.server_socket.listen(10)
        

        """
        Function : wrap_socket()
        
        Wrap an existing Python socket sock and return an instance of SSLContext.sslsocket_class (default SSLSocket). 
        The returned SSL socket is tied to the context, its settings and certificates. 
        sock must be a SOCK_STREAM socket; other socket types are unsupported.
        """
        
        self.server_socket = self.CONTEXT.wrap_socket(self.server_socket, server_side=True, do_handshake_on_connect=True, suppress_ragged_eofs=True, server_hostname=None)
        self.logger.info(f"[SERVER SOCKET] - SERVER INFOS: {self.SERVER_INFO}")
        
        
    def new_connection(self) -> None:
        """
        Accept new incoming connection from socket
        Start thread session for client when init Client_Session class
        
        Return None
        Init CLient_Session with client socket info
        """
        
        self.logger.info(f"[SERVER SOCKET] - Waiting for clients...")
        
        while True:
            
            client_info = []
            
            for x in self.server_socket.accept():
                client_info.append(x)
            
            self.logger.info(f"[SERVER SOCKET] - Connected to client: {client_info[0]}\nStarting new thread for this client...")
            
            Client_Session(client_socket= client_info[0], logger=self.logger)



if __name__ == '__main__':
      
    do = Server()
    do.bind()
    do.new_connection()