
from slacker import Slacker

class SlackBot():
    def __init__(self, config):
        self.config = config
        self.bot = Slacker(self.config['token'])

    def send_message(self, channel, message):
        if not channel:
            channel = self.config['default_channel']
        self.bot.chat.post_message(channel, message)
