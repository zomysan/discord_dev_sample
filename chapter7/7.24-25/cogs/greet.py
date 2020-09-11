from discord.ext import commands
import discord
import asyncio

class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, ctx):
        # 待機するメッセージのチェック関数
        def check_message_author(msg):
            return msg.author is ctx.author
        # あいさつする既存の処理
        await ctx.send(f"こんにちは、{ctx.author.name}さん。")
        await ctx.send("ご気分はいかがでしょうか？")
        try:
            # チェック関数に合格するようなメッセージを待つ
            msg = await self.bot.wait_for('message', check=check_message_author, timeout=10)
        except asyncio.TimeoutError:
            await ctx.send("タイムアウトしました。")
            return
        # 受け取ったメッセージの内容を使って返信
        embed = discord.Embed()
        embed.color = discord.Color.blue()
        embed.description = "あなたの気分を把握しました。"
        embed.add_field(name="あなたの気分", value=msg.content)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def hello_multi(self, ctx, count: int):
        for i in range(count):
            await ctx.send(f"こんにちは、{ctx.author.name}さん。")

    @hello_multi.error
    async def hello_multi_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send("パラメーターの形式が違います")
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("パラメーターの数が足りません")


def setup(bot):
    bot.add_cog(Greet(bot))