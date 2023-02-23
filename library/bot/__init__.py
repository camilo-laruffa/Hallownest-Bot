from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord import Embed
from discord import Intents 
from datetime import datetime


PREFIX = "+"
OWNER_IDS = [1078311123515879535]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.schedule = AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX, 
            owner_ids=OWNER_IDS, 
            intents=Intents.all()
        )

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

            # Obtiene el canal con X id y manda un mensaje 
            channel = self.get_channel(540398488333189120)
            #await channel.send("Now online!")

            #Este es un mensaje embed que son esos mensajes locos que hacen los bots
            embed = Embed(title="Now online!", description="Hallow bot is at your service now.", colour=0x05ffe2, timestamp=datetime.now())
            fields = [("Owner","Camilo Laruffa",True), 
                        ("Server", self.guild.name, True),
                        ("Caidas de Tomás", "26", False)]
            for name,value,inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name="Camilo Laruffa", icon_url="https://cdn.discordapp.com/attachments/414473395082887170/1078427753893867520/image.png")
            embed.set_footer(text="chupen bolas")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/414473395082887170/1078428020802584576/image.png")
            embed.set_image(url=self.guild.icon)
            await channel.send(embed=embed)
                
        else:
            print("bot reconnected")

    async def on_message(self, message):
        pass


bot = Bot()