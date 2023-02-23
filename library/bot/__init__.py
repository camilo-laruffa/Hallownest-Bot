from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord import Intents 


PREFIX = "+"
OWNER_IDS = [1078311123515879535]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.schedule = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents=Intents.default())

    def run(self, version):
        self.VERSION = version

        with open("./library/bot/token", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("bot connected")

    async def on_disconnected(self):
        print("bot disconnected")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            #Cambiar esta ID por la del server de hallownest cuando este listo para el deploy (Ver minuto 10:30 de https://www.youtube.com/watch?v=jVnEqd8bnBk&list=PLYeOw6sTSy6ZGyygcbta7GcpI8a5-Cooc&index=6)
            self.guild = self.get_guild(414473395082887168)
            print("bot ready")        
        else:
            print("bot reconnected")

    async def on_message(self, message):
        pass


bot = Bot()