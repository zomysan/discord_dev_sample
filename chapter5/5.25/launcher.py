from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("on_ready")

@bot.event
async def on_message(message):
    # 事前に定義したNGワードが含まれたら、「NGワードですよ！」と警告する
    if message.author == bot.user:
        # Botからのメッセージには反応しない
        # この判定をしないと無限ループが起きる
        return

    # NGワードの定義
    NG_WORDS = ['NGワード', '禁止単語']

    # 全NGワードについて存在確認
    for ng_word in NG_WORDS:
        if ng_word in message.content:
            # NGワードを発見したらテキストチャンネルに通知
            await message.channel.send(f"**{ng_word}**はNGワードです。")
            break
            

bot.run("ThisIsDummyToken00000000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
