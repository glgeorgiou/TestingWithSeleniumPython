import inspect
import logging


class BaseClass:
    def getLogger(self):
        #A trick to display the testcase that is, the method name instead of __name__
        # Το inspect.stack() αναφέρεται στην σειρά εκτέλεσης του Interpreter στην python ή αλλιώς # σωστά μπορούμε να πούμε της στοίβας του. Με ποια σειρά δηλαδή εκτελούνται οι εντολές και # τα functions που έχουμε.
        loggerName = inspect.stack()[1][3]  #Display 1 of 3
        logger = logging.getLogger(loggerName)
        
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger


