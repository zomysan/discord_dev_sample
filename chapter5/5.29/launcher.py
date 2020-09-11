from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("on_ready")


@bot.event
async def on_voice_state_update(member, before, after):
    # 誰かがボイスチャンネルに入ったら、テキストチャンネルに通知する。
    if after.channel is not None:
        # 適当なテキストチャンネルを投稿先として使う。
        # テキストチャンネルが存在しないGuildでは失敗する
        text_channel = member.guild.text_channels[0]
        # テキストチャンネルに通知を送信
        await text_channel.send(
            f"{member.name}さんがボイスチャンネル「{after.channel.name}」に入室しました。")


bot.run("ThisIsDummyToken00000000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
