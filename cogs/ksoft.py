import discord
from discord.ext import commands
import ksoftapi

kclient = ksoftapi.Client("695cb5adaf19999c1e66774ea03d241fe4f6a3ee")


class KSoft(commands.Bot):
    def __init__(self,bot):
        self.bot = bot
    

    @commands.command()
    async def lyrics(ctx, *,query):
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