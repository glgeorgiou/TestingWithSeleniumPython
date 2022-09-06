import pytest

from pytestsDemo.BaseClass import BaseClass #from projectName.fileName import className


@pytest.mark.usefixtures("dataLoad") #dataload is the method from conftest.py
class TestExample2(BaseClass): #Η TestExample2 class κληρονομεί την BaseClass

    def test_editProfile(self, dataLoad): #Το dataLoad χρειάζεται ως παράμετρος γιατί επιστρέφει κάτι.
        #Log file
        log = self.getLogger()  #Το getLogger το παίρνει από το BaseClass.py return logger.
        log.info(dataLoad[0])   #Prints the type of the error: info
        log.info(dataLoad[2])   #Prints the type of the error: info
        
        #Console printing
        #print(dataLoad[0])
        #print(dataLoad[2])
