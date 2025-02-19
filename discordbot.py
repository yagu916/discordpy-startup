from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
 async def on_message(message):
 if client.user in message.mentions: # 話しかけられたかの判定
     reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
     await message.channel.send(reply) # 返信メッセージを送信
    


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command() 
async def neko(ctx):
    await ctx.send('http://imgcc.naver.jp/kaze/mission/USER/20180112/72/7442902/0/250x248xf3828f97025dd9c3b94499e8.jpg')

bot.run(token)
