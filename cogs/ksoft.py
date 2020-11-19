import discord
from discord.ext import commands
import ksoftapi




class KSoft(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    

    @commands.command()
    async def lyrics(self,ctx, *,query):
        """ Return lyrics for a given song """
        try:
            results = await kclient.music.lyrics(query=query,clean_up=True)
        except ksoftapi.NoResults:
            await ctx.send('No lyrics found for ' + query)
        else:
            first = results[0]
            embed = discord.Embed(title = f"Lyrics for {first.name} by {first.artist}", description=first.lyrics)
            embed.set_footer(text="Lyrics provided by KSoft.Si")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(KSoft(bot))
