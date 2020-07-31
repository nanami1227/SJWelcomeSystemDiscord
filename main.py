import discord
from discord.ext import commands
import json
import os

with open ('configs/aliases.json', 'r',encoding='utf8')as aliases:
	aliases = json.load(aliases)
with open ('configs/config.json', 'r',encoding='utf8')as config:
	config = json.load(config)
with open ('configs/key.json', 'r',encoding='utf8')as key:
	key = json.load(key)

TOKEN = key['TOKEN']
bot = commands.Bot(command_prefix=config['prefix'])


@bot.event
async def on_ready():
	print(f'Logged in as: {bot.user.name}')
	print(f'With ID: {bot.user.id}')
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="MemberJoin"))
	print('>>SYSTEM ONLINE<<')

bot.remove_command('help')

for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds{filename[:-3]}')

bot.run(TOKEN)