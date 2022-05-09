import discord
from discord import mentions
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("d_token")

with open("swears.txt", "r") as wordlist:
    swearwords = list(wordlist.read().split())

gif = "https://tenor.com/view/watch-your-mouth-watch-your-profanity-watch-it-gif-5600117"


class myClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        message_safe = True
        print(f"Message from {message.author}: {message.content}")

        if message.author == self.user or message.author == 'INSER_BOT_NAME':
            return
        else:
            user_message = message.content.lower().split()
            for index, word in enumerate(user_message):
                for swear in swearwords:
                    if user_message[index] == swear:
                        message_safe = False
                        user_message[index] = "▂" * len(word)
                        censored_message = " ".join(user_message)

        if not message_safe:
            await message.reply(f"@{message.author} said: {censored_message}\n" + gif, mention_author=True)
            await message.delete(delay=None)


client = myClient()

if __name__ == "__main__":
    client.run(TOKEN)
