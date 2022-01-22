"""
Author : LA
Title : Demo of Python Socket - Client session

Description : Thread session for each client. Message reception and transmission as Rx_Tx class

Version : 3.0 (Public Version of code from PYKE NPPE V3)
OS : Linux & macOS
Updated : 2022-01-22

WARNING : THIS PROGRAM IS ONLY A DEMO - DOES NOT REPRESENT PROGRAM FOR PRODUCTION OR PYKE NPPE V3
"""

# Python Library
from _thread import *


class Rx_Tx:
    """
        Init Rx_Tx class:
            client_socket as class variable using self
            logger as class object using self

            Setting MAX BYTES SIZE
            
        Sending message to client
        Receiving message from client
    """
    
    
    def __init__(self, client_socket=list, logger=object) -> None:
        """
            client_socket as class variable using self
            logger as class object using self

            Setting MAX BYTES SIZE
            
            Return: None
                
        """
        self.logger = logger
        self.logger.info("[SERVER SESSION] - Init Rx-Tx...")
        
        self.client = client_socket # Client socket info
        self.MAX_SIZE = int(8192) # Bytes size
        
        self.logger.info("[SERVER SESSION] - Rx-Tx ready.")
    
    
    def send_to_client(self, data_out=str) -> None:
        """
            Getting message as function parameter
            Send message to client using client socket info
            Exception raised when sending message failed
            
            Return: None
                
        """
        self.logger.info(f"[SERVER SESSION] - Sending message to client...\n Message : {data_out}")
        try:
            self.client.send(str.encode(str(data_out)))
            
        except:
            self.logger.error("[SERVER SESSION] - Sending message to client FAILED!")
            raise
        
        self.logger.info("[SERVER SESSION] - Message sended to client.")
    
    
    def receive_from_client(self) -> str:
        """
            Receiving message from client using client socket info
            Exception raised when receiving message failed
            
            Return: message (data_in) from client as type str
                
        """
        data_received_len = int(0)
        
        self.logger.info("[SERVER SESSION] - Receiving message from client...")
        
        try: data_in = self.client.recv(self.MAX_SIZE).decode('utf-8')
        
        except: 
            self.logger.error("[SERVER SESSION] - Receiving message from client FAILED!")
            raise
        
        data_received_len += len(data_in)

        self.logger.info(f"[SERVER SESSION] - Message received from client: {self.client}\nMessage: {data_in}\nMessage size: {data_received_len} Bytes.")
        return data_in
        
        

class Client_Session:
    """
        Init Client_Session class:
            client_socket as class variable using self
            logger as class object using self
            Init Rx_tx class
            Start tread for client session
    """
    
    
    def __init__(self, client_socket=list, logger=object) -> None:
        """
            client_socket as class variable using self
            logger as class object using self
            Init Rx_tx class
            Start tread for client session
             
        """
        
        self.logger = logger
        self.logger.info("[SERVER SESSION] - Starting Rx_Tx init...")
        
        self.rx_tx = Rx_Tx(client_socket=client_socket, logger=logger) #Init Rx_Tx to send and receive data
        
        self.client_socket = client_socket
        
        self.logger.info("[SERVER SESSION] - Starting thread for client...")
        start_new_thread(self.threaded_client, ())
        

    
    def threaded_client(self) -> None:
        """
            Get native ID of thread
            Keep session running using while(1)
            
            Call function to receive message from client and send message to client
            If received message is empty then exit session
            
            Return : None
        """
        self.user_session = get_native_id()
        self.logger.info(f"[SERVER SESSION] - Client thread ID: {self.user_session}")

        while True:
            
            response = str("")
            data_from_client = str("")
            
            data_from_client = self.rx_tx.receive_from_client()
            
            if data_from_client != "":
                
                response = f"Hello ! Client : {self.client_socket} \n- This is your message : {data_from_client}"
                
                self.rx_tx.send_to_client(data_out=response)
                
            else : self.exit_session()
             
             
    def exit_session(self) -> None:
        self.logger.info(f"[SERVER SESSION] - Exiting client on thread ID: {self.user_session}")
        exit()