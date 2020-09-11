from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("on_ready")


@bot.event
async def on_guild_join(guild):
    # 新しくGuildに入ったらログを残す
    print("新しくGuildに入った！")
    print(f"名前: {guild.name} / ID: {guild.id} / メンバー数: {guild.member_count}")


bot.run("ThisIsDummyToken00000000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
