

import subprocess       #for the file conversion 
import requests

class download:
    
    def __init__(self,location,user,  message = ""):
        self.step = 0
        self.location = location
        self.user = user

    def run(self,message):
        return 0
        print ("This is the message the user has sent")
        # To send filelocation to user
        filelocation = self.location + "/the file"
        self.user.manager.bot.send_file(self.id, filelocation)
        print (message)
        