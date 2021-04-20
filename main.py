

import subprocess       #for the file conversion 
import requests

class download:
    
    def __init__(self,location, message = ""):
        self.step = 0

    def run(self,message):
        print ("This is the message the user has sent")
        print (message)
        