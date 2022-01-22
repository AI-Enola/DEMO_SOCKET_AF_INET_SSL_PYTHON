# Created by LA - 12 november 2021
# Modified by LA - 22 january 2022
# V1
# OLD COMMENTS VALIDED - 2022-01-05 by LA

import logging
import logging.handlers


class Log():
    """
    Description : Log data to display on console and save them into log file if needed.
    Function parameters : log_in_file=bool, log_in_console=bool, encoding=str, filename=str, filemode=str, logger_name=str, format=str -> None
    Note when not using file for saving log : If log_in_file is False, encoding, filename and filemode can be set to None
    
    Example : 
        # Init logger
        log = Log(log_in_file=True, log_in_console=bool, encoding='utf-8', filename='log.txt', filemode='a', logger_name='LOG TEST', format='%(name)s - %(asctime)s - %(levelname)s: %(message)s')
        self.logger = log.get_logger()
        
        # Use like this :
        self.logger.info("This is a test")
    """
    
    def __init__(self, log_in_file=bool, log_in_console=bool, encoding=str, filename=str, filemode=str , logger_name=str, format=str) -> None :

        # set format
        self.formatter = logging.Formatter(format)
        
        # Set logger name and logger level
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        
        if (log_in_file) :
            self.set_log_file(encoding=encoding, filename=filename, filemode=filemode)
            
        if (log_in_console) :
            self.set_log_console()
        

    
    def set_log_file(self, encoding=str, filename=str, filemode=str) -> None:
        """
        Description : Log data into file
        Function parameters : encoding=str, filename=str, filemode=str, logger_name=str -> None
        Note : log_in_file need to be set as True to use this function
        """
        # set file to get log
        handler = logging.handlers.WatchedFileHandler(encoding=encoding,filename=filename, mode=filemode)
        # create formatter for file log
        handler.setFormatter(self.formatter)
        # add file to logger to send log to it
        self.logger.addHandler(handler)
    


    def set_log_console(self) -> None:
        """
        Description : Show log data into console
        Function parameters : self
        """
        # create console handler and set level to info
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # create formatter for console
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
    


    def get_logger(self) -> object:
        """
        Description : Return logger to use in own code
        Function parameters : self
        Return : logger as object
        """
        return self.logger