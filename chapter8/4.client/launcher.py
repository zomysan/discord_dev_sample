from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!")

@bot.command()
async def client_change_presense(ctx, title):
    client = bot
    game = discord.Game(name=title)
    await client.change_presence(activity=game)

@bot.command()
async def client_close(ctx):
    client = bot
    await ctx.send("Botアカウントからログアウトします。")
    await client.close()

@bot.command()
async def client_info(ctx):
    client = bot
    await ctx.send(
        f"Botユーザー名: {client.user.name}\n"
        f"BotユーザーID: {client.user.id}\n"
        f"Guild数: {len(client.guilds)}\n"
        f"ボイス接続数: {len(client.voice_clients)}\n"
        f"ユニークユーザー数: {len(client.users)}\n"
        f"延べユーザー数: {sum([g.member_count for g in client.guilds])}\n"
    )

@bot.command()
async def client_application_info(ctx):
    client = bot
    app_info = await client.application_info()
    await ctx.send(
        f"アプリケーションID: {app_info.id}\n"
        f"Botオーナー: {app_info.owner.name}\n"
        f"Public Bot?: {app_info.bot_public}\n"
    )


bot.run("ThisIsDummyToken00000000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
