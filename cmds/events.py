import discord
from discord.ext import commands
import json
from discord.utils import get

with open ('config/aliases.json', 'r',encoding='utf8')as aliases:
	aliases = json.load(aliases)
with open ('config/config.json', 'r',encoding='utf8')as config:
	config = json.load(config)
with open ('config/key.json', 'r',encoding='utf8')as key:
	key = json.load(key)

class events(commands.Cog):
	def __init__(self, bot):
		self.bot=bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f'loaded cog: {__name__}')

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = self.bot.get_channel(int(config['welcome_channel']))
		await channel.send(f'{member.mention} joined {member.guild.name}!')
		role = get(member.guild.role, id=738610073118572624)
		await member.add_roles(role)

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		channel = self.bot.get_channel(int(config['goodbye_channel']))
		await channel.send(f'**{member.name}#{member.discriminator}** left {member.guild.name}!')

def setup(bot):
	bot.add_cog(events(bot))