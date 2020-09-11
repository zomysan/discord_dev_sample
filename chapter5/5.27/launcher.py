from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("on_ready")


@bot.event
async def on_member_join(member):
    # Guildメンバーがふえたら挨拶DMを送信する
    # memberのDM受け取り設定によっては失敗する
    await member.send(
        f"{member.name}さん、サーバー「{member.guild.name}」にようこそ！\n"
        f"わたしは「{bot.user.name}」といいます。\n"
        "このサーバーでは、特にきまりごとはありません。ごゆっくりどうぞ。"
    )


bot.run("ThisIsDummyToken00000000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
