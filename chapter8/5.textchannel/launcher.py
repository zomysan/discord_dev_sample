from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!")

@bot.command()
async def tc_typing(ctx):
    import asyncio
    await ctx.send("処理を開始します。")
    async with ctx.channel.typing():
        # 長い処理の代わりにsleepする
        await asyncio.sleep(3)
    await ctx.send("処理が完了しました！")

@bot.command()
async def tc_purge(ctx, purge_word, limit: int):
    def contains_purge_word(message):
        return purge_word in message.content
    channel = ctx.channel
    await ctx.send(f"「{purge_word}」を含むメッセージを最大{limit}件削除します。")
    deleted = await channel.purge(limit=limit, check=contains_purge_word,
                                  before=ctx.message.created_at)
    await ctx.send(f'{len(deleted)}件のメッセージを削除しました。')

@bot.command()
async def tc_create_invite(ctx):
    # 24時間有効、10人まで招待可能な招待を作成
    channel = ctx.channel
    invite = await channel.create_invite(max_age=3600 * 24, max_uses=10)
    await ctx.send(invite.url)

@bot.command()
async def tc_send_file(ctx):
    await ctx.send(file=discord.File(fp="shovel.png"))

bot.run("ThisIsDummyToken00000000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
