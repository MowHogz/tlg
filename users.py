#2.0.0 - Beta 
# we made some temporary changes (left commented out) used to send the album cover for Beta testing 
from main import download
class user:
    def __init__(self,manager, client_info,location , message = " ", admin = False):
        
        self.manager = manager 
        self.admin = admin          #bool
        self.client_info = client_info
        try:    self.name = client_info['first_name']
        except: self.name = "Unknown"

        self.id = client_info['id']
        self.location = location
        self.download = download(self.location)

        self.count = 0
    def send(self, message):
        self.manager.bot.send_message(self.id, message)

    def run(self, message):
        self.count += 1
        self.send("The bot has received message number " + str(self.count))

        self.download.run(message)
        print ("we did stuff")
        
        return "You have accessed the run function of the user, You have done this {} times".format(self.count)
