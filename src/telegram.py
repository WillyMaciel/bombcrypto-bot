import telegram

def newBot(token, chat_id):
    return Bot(token, chat_id)

class Bot():
    """docstring for Bot"""
    def __init__(self, token, chat_id):

        self.token   = token
        self.chat_id = chat_id

        self.botInstance = self.newBot()

    def newBot(self):
        return telegram.Bot(token=self.token)

    def sendText(self, bot_message):
        try:
            return self.botInstance.send_message(chat_id=self.chat_id, text=bot_message)
        except:
            return 0

    def sendPhoto(self, photo_path):
        try:
            return self.botInstance.send_photo(chat_id=self.chat_id, photo=open(photo_path, 'rb'))
        except:
            return 0

    def getUpdates(self):
        return self.botInstance.getUpdates()
