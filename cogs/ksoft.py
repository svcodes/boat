import discord
from discord.ext import commands
import ksoftapi
from utils import default

config = default.get("config.json")
kclient = ksoftapi.Client(config.ksoft_token)



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

    @commands.command()
    async def meme(self, ctx):
        meme = await kclient.images.random_meme()
        embed = discord.Embed(title=f"Meme: {meme.title}", description=f"Subreddit: r/{meme.subreddit}\n[Link]({meme.source})")
        embed.set_image(url=meme.image_url)
        embed.set_footer(text=f"Obtained with KSoft.Si | {meme.upvotes} ⬆")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(KSoft(bot))
