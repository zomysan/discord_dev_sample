from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!")

@bot.command()
async def guild_info(ctx):
    from datetime import timedelta
    guild = ctx.guild
    await ctx.send(
        f"サーバー名: {guild.name}\n"
        f"サーバーID: {guild.id}\n"
        f"サーバーオーナー: {guild.owner.name}\n"
        f"メンバー数: {guild.member_count}\n"
        f"作成日: {guild.created_at + timedelta(hours=9)}\n"
    )

@bot.command()
async def guild_edit(ctx, name):
    guild = ctx.guild
    old_name = guild.name
    await guild.edit(name=name)
    await ctx.send(
        "Guildの名前を変更しました。\n"
        f"{old_name}→{name}"
    )

@bot.command()
async def guild_create_channel(ctx, name):
    guild = ctx.guild
    await guild.create_text_channel(name=name)
    await ctx.send(f"テキストチャンネル{name}を作成しました。")

@bot.command()
async def guild_kick(ctx, member: discord.Member, reason):
    guild = ctx.guild
    await ctx.send(f"{member.name}をKickします。")
    await guild.kick(user=member, reason=reason)

@bot.command()
async def guild_leave(ctx):
    guild = ctx.guild
    await ctx.send("このGuildから退出します。")
    await guild.leave()


bot.run("ThisIsDummyToken00000000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
