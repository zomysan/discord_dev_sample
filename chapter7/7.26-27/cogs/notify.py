from discord.ext import commands
from discord.ext import tasks
from datetime import datetime  # 追加


class Notify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # 時報タスクの開始
        self.notifier.start()
        # 時報通知先チャンネル
        self.channel = None

    def cog_unload(self):
        # 時報タスクの中断
        self.notifier.cancel()

    @tasks.loop(minutes=10.0)
    async def notifier(self):
        print("start_notifier")
        now = datetime.now()
        # 通知先が登録されていれば通知
        if self.channel:
            await self.channel.send(
                f"現在、{now.strftime('%Y/%m/%d %H:%M:%S')}です")

    @commands.command()
    async def set_notify_channel(self, ctx):
        # 通知先テキストチャンネルを保持
        self.channel = ctx.channel
        # 登録完了を通知
        await ctx.send(f"「{ctx.channel.name}」に時報を通知します！")

def setup(bot):
    bot.add_cog(Notify(bot))