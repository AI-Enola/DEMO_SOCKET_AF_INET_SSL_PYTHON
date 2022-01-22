"""
Author : LA
Title : Demo of Python Socket - Client main
Description : Client send message to server and server reply message back
Version : 1.0 (Public Version of code from PYKE NPPE V3)
OS : Linux & macOS
Updated : 2022-01-22

WARNING : THIS PROGRAM IS ONLY A DEMO - DOES NOT REPRESENT PROGRAM FOR PRODUCTION OR PYKE NPPE V3
"""

# Custom library
from client_socket import Client_Socket
from log import Log


class Rx_Tx:
    """
        Init Rx_Tx class:
            client_socket as class variable using self
            logger as class object using self

            Setting MAX BYTES SIZE
            
        Sending message to server
        Receiving message from server
    """
    
    
    def __init__(self, server_socket=list, logger=object) -> None:
        """
            client_socket as class variable using self
            logger as class object using self

            Setting MAX BYTES SIZE
            
            Return: None
                
        """
        self.logger = logger
        self.logger.info("[CLIENT] - Init Rx-Tx...")
        
        self.server_socket = server_socket # Client socket info
        self.MAX_SIZE = int(8192) # Bytes size
        
        self.logger.info("[CLIENT] - Rx-Tx ready.")
    
    
    def send_to_server(self, data_out=str) -> None:
        """
            Getting message as function parameter
            Send message to server using server socket info
            Exception raised when sending message failed
            
            Return: None
                
        """
        self.logger.info(f"[CLIENT] - Sending message to server...")
        try:
            self.server_socket.send(str.encode(str(data_out)))
            
        except:
            self.logger.error("[CLIENT] - Sending message to server FAILED!")
            raise
        
        self.logger.info("[CLIENT] - Message sended to server.")
    

    def receive_from_server(self) -> str:
        """
            Receiving message from server using server socket info
            Exception raised when receiving message failed
            
            Return: message (data_in) from server as type str if str is empty then return empty str
                
        """
        data_received_len = int(0)
        data_in = ""
        
        self.logger.info("[CLIENT] - Receiving message from server...")
        
        try: data_in = self.server_socket.recv(self.MAX_SIZE).decode('utf-8')
        
        except: 
            self.logger.error("[CLIENT] - Receiving message from server FAILED!")
            raise
        
        data_received_len += len(data_in)
        
        if data_in != "" :

            self.logger.info(f"[CLIENT] - Message received from server.")
        
        else : 
            self.logger.error("[CLIENT] - Receiving message from server FAILED! Exiting demo...")
            exit()
        
        return data_in



class Client:
    
    
    def __init__(self) -> None:
        """
        Init Client class:
            client_socket as class variable using self
            logger as class object using self
            Init Rx_tx class
             
        """
        
        # Init logger
        log = Log(log_in_file=True, log_in_console=True, encoding='utf-8', filename='./log.txt', filemode='a', logger_name='DEMO SOCKET PYTHON', format='%(name)s - %(asctime)s - %(levelname)s: %(message)s')
        self.logger = log.get_logger() # Get logger object
        
        self.logger.info("[CLIENT] - Starting Init socket...")
        server_socket = Client_Socket(logger=self.logger)
        self.server_socket = server_socket.connect_to_server()
        
        
        self.logger.info("[CLIENT] - Starting Init Rx_Tx...")
        self.rx_tx = Rx_Tx(server_socket=self.server_socket, logger=self.logger) #Init Rx_Tx to send and receive data
        
        self.logger.info("[CLIENT] - Starting Init done.")


    def main(self) -> None:
        """
            Keep DEMO running
            Wait for user input to send to server
            Get message from server
            
            Return: None
                
        """
        while(1) : # Keep DEMO running
            
            message_from_server = str("")
            message = input("(Press 0 to quit demo) \nYour message: ")
            
            if message == "0": # Stop demo
                break
            
            elif message != "" :
            
                self.rx_tx.send_to_server(data_out=message)
                
                message_from_server = self.rx_tx.receive_from_server()
                
                if message_from_server != "":
                
                    self.logger.info(f"[CLIENT] - Message from server: {message_from_server}")

        
  
        
if __name__ == '__main__':
      
    do = Client()
    do.main()