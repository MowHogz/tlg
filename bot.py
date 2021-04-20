#v2.1 - the bot is now using the official Telegram bot API  
#the code needs lots of cleaning up 
from telegram import Bot
import requests


class simple_bot:
    def __init__(self,token,default_client = False):
        self.bot = Bot(token)
        self.default_client = default_client                            #admin 

    def send(self,message):
        self.send_message(self.default_client,message)
    
    def get_updates(self, offset=0, timeout=10):
        updates = self.bot = getUpdates(offset = offset, timeout = timeout)

        return updates

    def send_message(self, chat_id, text):

        self.bot.send_message(chat_id, text)
        


class BotHandler:
    def __init__(self, token,directory = False ):
        self.bot = Bot(token)
        #self.dir = directory
        #self.log_file = open(self.dir + "logs/tsendlog.txt",'a') 
        #url = "https://api.telegram.org/bot<token>/"
        #logging disabled now
    def refresh_logger(self): 
        try:
            self.log_file.close()
        except:
            pass
        self.log_file = open(self.dir + "logs/tsendlog.txt",'w+') 
        print ("succesfully opened bot logger ")
    def logger(self,loggy_stuff):
        self.log_file.write("\n{}\n".format(loggy_stuff))
        #pass

    def get_updates(self, offset=0, timeout = 10):
        updates = self.bot.getUpdates(offset = offset, timeout = timeout)

        return updates

    def send_message(self, chat_id, text):

        self.bot.send_message(chat_id, text)

    def get_first_update(self): #i think this serves no purpose
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update
    def send_file(self,chat_id,file_location):
        #file = file_location 
        self.bot.send_file(id, open(file_location,'rb'))
        files = {
            'document': open(file, 'rb')
        }

        #message = (self.api_url + 'sendDocument?chat_id=' + str(chat_id))

        #send = requests.post(message, files = files)
        #return send
    def send_pic(self,chat_id,file_location):
        files = {
            'photo': open(file_location, 'rb')
            }
        
        message = "{}sendPhoto?chat_id={}".format(self.api_url,str(chat_id))

        r= requests.post(message, files=files)
    
    def send_pic_file(self,chat_id,file):
        self.bot.send_photo(chat_id, file)
    def send_vid(self,chat_id,file_location):
        self.bot.send_video(chat_id, open(file_location,'rb'))
        files = {
            'video': open(file_location, 'rb')
            }
        
        message = "{}sendVideo?chat_id={}".format(self.api_url,str(chat_id))
        
        #r= requests.post(message, files=files)
    def send_audio(self,chat_id,file_location):
        return self.bot.send_audio(chat_id, open(file_location,'rb'))
        
        # files = {
            #'audio': open(file_location, 'rb')
            #}
        
        #message = "{}sendAudio?chat_id={}".format(self.api_url,str(chat_id))
        
        #r= requests.post(message, files=files)
    
    def send_link(self, chat_id,text, link):
        
        return 0
        print ("This is the magnet link")
        print (link)
        params = {'chat_id': chat_id, 'text':link, 'parse_mode': 'HTML', 'entities': [{'offset': 0, 'length': 5, 'type': 'text_link', 'url': 'google.com'}]}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        print ("This is the message we are sending : \n {}".format(resp))
        return resp
