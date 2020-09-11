from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("on_ready")


@bot.event
async def on_message_delete(message):
    # 投稿日時が古い等の理由によりキャッシュされていないメッセージの削除は検知できないことに注意！
    # ソースコード上で１行が80字を超える場合、このように改行して80字におさめるとよい
    await message.channel.send(
        f"{message.author.name}さんのメッセージが削除されました。")
            

bot.run("ThisIsDummyToken00000000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
