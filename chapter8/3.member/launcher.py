from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!")

@bot.command()
async def member_info(ctx):
    from datetime import timedelta
    member = ctx.author
    await ctx.send(
        f"ユーザー名: {member.name}\n"
        f"ユーザーID: {member.id}\n"
        f"Discordへの参加日: {member.created_at + timedelta(hours=9)}\n"
        f"Guildへの参加日: {member.joined_at + timedelta(hours=9)}\n"
        f"ステータス: {str(member.status)}\n"
        f"モバイルからのログイン？: {member.is_on_mobile()}"
    )

@bot.command()
async def member_mention(ctx):
    member = ctx.author
    await ctx.send(f"{member.mention} メンションのテストです。")

@bot.command()
async def member_bot(ctx, member: discord.Member):
    if member.bot:
        await ctx.send(f"{member.name}はBotです。")
    else:
        await ctx.send(f"{member.name}はBotではありません。")

@bot.command()
async def member_send(ctx, member: discord.Member, content):
    await ctx.send(f"{member.name}にDMを送信します。")
    await member.send(content=content)

@bot.command()
async def member_voice(ctx):
    member = ctx.author
    if member.voice and member.voice.channel:
        await ctx.send(f"あなたは「{member.voice.channel.name}」にいます。")
    else:
        await ctx.send(f"あなたはボイスチャンネルに参加していません。")

@bot.command()
async def member_move(ctx, member: discord.Member,
                      voice_channel: discord.VoiceChannel):
    if not member.voice or not member.voice.channel:
        await ctx.send("ボイスチャンネルに参加していません。")
        return
    await member.move_to(voice_channel)
    await ctx.send(
        f"{member.name}をボイスチャンネル{voice_channel.name}に移動しました。")

bot.run("ThisIsDummyToken00000000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
