from discord.ext import commands


def is_staff():
    async def predicate(ctx):
        return ctx.author.id == 98208218022428672
        # TODO Make this read from an admin file

    return commands.check(predicate)


class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='stop',
        aliases=['shutdown'],
        description='This is a staff only command to stop the bot'
    )
    @is_staff()
    async def stop_bot(self, ctx):
        """Shutdown the bot"""
        await ctx.send('Oh, alright... I\''' just shutup I guess.. :wave:')
        await self.bot.close()
