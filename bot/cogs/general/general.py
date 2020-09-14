

import discord
from discord.ext import commands

import time
import random

class General(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.initial_time = time.monotonic() # initialize time for calculating uptime
	 

	@commands.command()
	
	async def ping(self, ctx):
		current_ping = round(self.bot.latency, 2)
		current_uptime = round(time.monotonic() - self.initial_time, 2)
		await ctx.send(f"🏓 Pong with {current_ping}")
		await ctx.send(f"👍 Up Time {current_uptime}s")

	@commands.command(aliases=['8ball'])
	async def ball(self, ctx, *, question):
		responses = [
			"It is certain.",
			"It is decidedly so.",
			"Without a doubt.",
			"Yes – definitely.",
			"You may rely on it.",
			"As I see it, yes.",
			"Most likely.",
			"Outlook good.",
			"Yes.",
			"Signs point to yes.",
			"Reply hazy, try again.",
			"Ask again later.",
			"Better not tell you now.",
			"Cannot predict now.",
			"Concentrate and ask again.",
			"Don't count on it.",
			"My reply is no.",
			"My sources say no.",
			"Outlook not so good.",
			"Very doubtful."
		]
		await ctx.send(f"{random.choice(responses)}")

def setup(bot):
	bot.add_cog(General(bot))