import discord
from discord.ext import commands
from utils import http


class Random(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def runpy(self, ctx, *, code)
        json = {"language": "python3", "source": code}
        returned = await http.post(url="https://emkc.org/api/v1/piston/execute", json=json)
        await ctx.send(returned)

    
def setup(bot):
    bot.add_cog(Random(bot))
