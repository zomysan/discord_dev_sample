from discord.ext import commands
import config
import asyncio  # 追加

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
async def hello_reaction(ctx):
    # イイネ、良くないネの絵文字
    thumbs_up = '\N{THUMBS UP SIGN}'
    thumbs_down = '\N{THUMBS DOWN SIGN}'

    # wait_forに渡すチェック関数
    def check_reaction(reaction, user):
        # リアクションの送信ユーザーを確認
        user_ok = (user == ctx.author)
        # リアクションの種別を確認
        reaction_ok = (reaction.emoji == thumbs_up or
                       reaction.emoji == thumbs_down)
        return user_ok and reaction_ok

    # メッセージを送信
    await ctx.send(f"こんにちは、{ctx.author.name}さん。")
    msg = await ctx.send("いまの気分を選んでください。")
    # 送信したメッセージにリアクションを付与
    await msg.add_reaction(thumbs_up)
    await msg.add_reaction(thumbs_down)
    # ユーザーからのリアクションを待つ
    reaction, user = await bot.wait_for("reaction_add",
                                        check=check_reaction)
    # ユーザーのリアクションに応じてメッセージを変える
    feel = "良い気分" if reaction.emoji == thumbs_up else "良くない気分"
    await ctx.send(f"{feel}なんですね。")


bot.run(config.TOKEN)