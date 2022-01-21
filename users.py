#2.0.0 - Beta 
# we made some temporary changes (left commented out) used to send the album cover for Beta testing 
import subprocess
from fileinput import filename
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
        self.download = download(self.location, self)
        self.count = 0 
        self.photo_list = []
        self.count = 0
        self.welcome_message = """
        Welcome to Chaim's helpful PDF converter bot!
        Send photos you would like to convert (in .jpg form)
        Send /convert   When you want to convert the selection of photos to PDF 
        Send /clear     When you want to clear your selection """
        self.send(self.welcome_message)


    def send(self, message):
        self.manager.bot.send_message(self.id, message)

    def run(self, message, file_download = False):


        if file_download:
            try:
                # download the file (usign the bog.getFile().download feature)
                file_name = f"/photo{self.count}.jpg"
                file_download(self.location + file_name)
                self.photo_list.append(file_name)
                self.count += 1
                print (self.location + file_name)
            except:
                print ("Couldn't save photo")
        
        if (message == "/convert" or message == "convert") and len(self.photo_list) >= 1:
            # self.manager.bot.send_file(self.id, "../tlgextras/photo1.jpg")
            command = ['convert']
            for photo in self.photo_list:
                command.append(self.location + photo)
            
            command.append(self.location + "/final.pdf")
            subprocess.run(command)
            self.manager.bot.send_file(self.id, self.location  + "/final.pdf")

        if message == "clear" or message == "/clear":
            self.photo_list = []
            self.count = 0
            self.send(self.welcome_message)

        # self.send("The bot has received message number " + str(self.count))
        self.download.run(message)
        print ("we did stuff")
        
        return "You have accessed the run function of the user, You have done this {} times".format(self.count)
