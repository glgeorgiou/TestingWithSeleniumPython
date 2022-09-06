import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__) #get the object for logg everything. __name__ = test case name

    filehandler = logging.filehandler('logfile.log')
   
    #Printing format. name is the test case name. The s is string format %s.
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)  #filehandler object

    #Θέτει το επίπεδο λάθους που θα δείξει. Ε΄άν θέσουμε warning, θα δείξει τα λάθη από το warning και κάτω.
    logger.setLevel(logging.CRITICAL)
    
    logger.debug("A debug statement is executed") #Prints a message to the file
    logger.info("Information statement") #Prints the type of the error: info
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode") #Prints the type of the error: warning
    logger.error("A Major error has happend") #Prints the type of the error: Error
    logger.critical("Critical issue") #Prints the type of the error: Critical



