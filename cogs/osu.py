import discord
from discord.ext import commands
from utils import default, http
import urllib.parse
from math import floor


class Osu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.osu_key = self.config.osu_api_key

    @commands.group()
    async def osu(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Please include a subcommand! (.osu user <username> | .osu rs <username>)')

    @osu.command(aliases=['rs'])
    async def recent(self, ctx, username, result: int = 1):
        """recent map stats"""
        api = await http.get(url=f"https://osu.ppy.sh/api/get_user_recent?k={self.osu_key}&u={urllib.parse.quote_plus(username)}",res_method = "json")
        if len(api) == 0:
            return await ctx.send("error no data found")
        data = api[(result-1)]
        await ctx.send(f"""data
mapid: {data['beatmap_id']}
score: {data['score']}""")

    @osu.command()
    async def user(self, ctx, username):
        """user statistics for osu"""
        api = await http.get(url=f"https://osu.ppy.sh/api/get_user?k={self.osu_key}&u={urllib.parse.quote_plus(username)}", res_method="json")
        data = api[0]
        embed = discord.Embed(title = f"osu! stats for {data['username']}", colour = 0xff66aa)
        playtime_secs = int(data['total_seconds_played'])
        playtime_mins = floor(playtime_secs/60)
        playtime_hr = playtime_mins // 60
        remain_mins = playtime_mins % 60                              
        embed.description = f"""**Username:** {data['username']}
**Join Date:** {data['join_date']}

**Rank:** {data['pp_rank']}

**PP:** {floor(float(data["pp_raw"]))}

**Total Playcount:** {data['playcount']}

**Ranked/Total Score:** {data['ranked_score']}/{data['total_score']}

**Playtime:** {playtime_hr} hours, {remain_mins} minutes
"""
        embed.set_thumbnail(url = f"http://s.ppy.sh/a/{data['user_id']}")
        embed.set_image(url=f"http://lemmmy.pw/osusig/sig.php?colour=hexff66aa&uname={urllib.parse.quote_plus(username)}&pp=2&onlineindicator=undefined&xpbar&xpbarhex")

        await ctx.send(embed=embed)

    
def setup(bot):
    bot.add_cog(Osu(bot))
