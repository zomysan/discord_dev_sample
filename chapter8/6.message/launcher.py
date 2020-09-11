from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!")

@bot.command()
async def message_add_reaction(ctx, emoji):
    msg = await ctx.send("このメッセージにリアクションを付ける")
    await msg.add_reaction(emoji)

@bot.command()
async def message_save_attachment(ctx):
    message = ctx.message
    if not message.attachments:
        await ctx.send("ファイルを添付してください")
        return
    attachment = message.attachments[0]
    await attachment.save(fp=attachment.filename)
    await ctx.send("1番目の添付ファイルを保存しました。")

bot.run("ThisIsDummyToken00000000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
