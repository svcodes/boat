import discord
from discord.ext import commands
from utils import http


class Random(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def runpy(self, ctx, *, code):
        json = {"language": "python3", "source": code}
        returned = await http.post(url="https://emkc.org/api/v1/piston/execute", json=json)
        embed = discord.Embed(title=f"did running succeed? {returned['ran']}")
        embed.add_field(name="Output", value=f"""```py
{returned['stdout']}
```""") 
        embed.add_field(name="Errors", value=f"""```py
{returned['stderr']}
```""") 
        await ctx.send(embed=embed)

    
def setup(bot):
    bot.add_cog(Random(bot))
