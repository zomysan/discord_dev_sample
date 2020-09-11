from discord.ext import commands
from discord.ext import tasks


class Notify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # 時報タスクの開始
        self.notifier.start()

    def cog_unload(self):
        # 時報タスクの中断
        self.notifier.cancel()

    @tasks.loop(seconds=1.0)
    async def notifier(self):
        print("start_notifier")


def setup(bot):
    bot.add_cog(Notify(bot))