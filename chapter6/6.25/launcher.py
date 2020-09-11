from discord.ext import commands
import config

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("on_ready")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        # Botからのメッセージには反応しない
        # この判定をしないと無限ループが起きる
        return

    if "Bot" in message.content:
        await message.channel.send("は～い、Botで～す")

    # 下記の処理を追加
    await bot.process_commands(message)


@bot.command()
async def hello(ctx):
    # 待機するメッセージのチェック関数
    def check_message_author(msg):
        return msg.author is ctx.author
    # あいさつする既存の処理
    await ctx.send(f"こんにちは、{ctx.author.name}さん。")
    await ctx.send("ご気分はいかがでしょうか？")
    # チェック関数に合格するようなメッセージを待つ
    msg = await bot.wait_for('message', check=check_message_author)
    # 受け取ったメッセージの内容を使って返信
    await ctx.send(f"「{msg.content}」という気分なんですね。")


bot.run(config.TOKEN)