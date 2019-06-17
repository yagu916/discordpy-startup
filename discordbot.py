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
    


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
            # 「/neko」と発言したら「にゃーん」が返る処理
async def neko(ctx):
    await ctx.send('ヨシ！')

bot.run(token)
