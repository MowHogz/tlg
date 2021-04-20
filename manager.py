from users import user

class user_manager:
    def __init__(self,bot,admin_bot = False, admin = False, location = False):
        self.current_members = {}
        self.bot = bot
        self.ad_bot = admin_bot    #this is the bot which sends to the admin and back 
        self.admin = admin
        self.location = location
        #print(self.bot.token)
    
    def to_admin(self, user, message):
        self.ad_bot.send("{}".format(message))
    
    def add_user(self, client_info, message = " "):
        
        return self.current_members.update({
            client_info['id']:  user(self, client_info, self.location,message=message, admin = (client_info['id'] == self.admin))
        })
        

    def exists(self,client_info):                   #checks if user exists in database
        print ("This is the client info ")
        print (client_info)
        if client_info['id'] in self.current_members:
            return True
        else:
            False
    
    