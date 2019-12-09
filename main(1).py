import json
import telepot
import time
import urllib2

#This function will coordinate and refresh the sending of the messages
def refresh(msg):
    print(msg['text'])
    if msg['text'] == "/start":
        GLOBAL = 1
    if msg['text'] == "/end":
        GLOBAL = 0
    if GLOBAL == 1:
        content_type, chat_type, chat_id = telepot.glance(msg)
#informations about the channel on thingspeak
        READ_API_KEY='7FLW25DPJV1NGOHK'
        CHANNEL_ID= '919289'

        
        TS = urllib2.urlopen("https://api.thingspeak.com/channels/919289/feeds.json?results=2" \
                       % (CHANNEL_ID,READ_API_KEY))
        response = TS.read()
        data=json.loads(response)
        if data == -1:
            print("No data available yet")
            time.sleep(10)
        else:
            a = int(data['field1'])
            if a >= 3000:
                bot.sendMessage(chat_id, "A umidade do solo esta muito baixa! | Valor: " + feeds[0]['field1'] + '%') °C
            if a >= 2000 and a < 3000:
                bot.sendMessage(chat_id, "A umidade do solo esta otima! | Valor: " + feeds[0]['field1'] + '%')
            if a < 2000:
                bot.sendMessage(chat_id, "A umidade do solo esta muito alta! | Valor: " + feeds[0]['field1'] + '%')
                
            b = int(data['field2'])
            if a >= 3000:
                bot.sendMessage(chat_id, "A umidade do solo esta muito baixa! | Valor: " + feeds[1]['field2'] + '°C') 
            if a >= 2000 and a < 3000:
                bot.sendMessage(chat_id, "A umidade do solo esta otima! | Valor: " + feeds[1]['field2'] + '°C')
            if a < 2000:
                bot.sendMessage(chat_id, "A umidade do solo esta muito alta! | Valor: " + feeds[1]['field2'] + '°C')
                
        TS.close()
        time.sleep(10)
            
#information about the bot        
bot = telepot.Bot("1001801074:AAHkuZSBRZFLKip8vBOX-qyDd8XcokiqVNY")
GLOBAL = 0
bot.message_loop(refresh)

while True:
    pass