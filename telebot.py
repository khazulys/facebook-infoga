import telepot, json, time
from telepot.loop import MessageLoop
from requests import Session

token = '' #token akses facebook
bot = telepot.Bot('') #token telegram bot
with Session() as r:
    def telebot(chID, txtmsg):
        if(len(txtmsg) == 15):
            c = r.get("https://graph.facebook.com/{0}?access_token={1}".format(txtmsg, token))
            j = json.loads(c.content)
            

        else:
            bot.sendMessage(chID, "enter id for get information")
            
        bot.sendMessage(chID, j)
        
    def handle(msg):
        coType, chType, chID=telepot.glance(msg)
        if(coType=="text"):
              telebot(chID, msg['text'])
              
    MessageLoop(bot, handle).run_as_thread()
    while 1:
        time.sleep(10)
