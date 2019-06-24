from discord.ext import commands

admins = []


def is_staff():
    async def predicate(ctx):
        for id in admins:
            if ctx.author.id == id:
                print('Parsed that admin! Matched ' + str(ctx.author.id) + ' to ' + str(id))
                return True
        return False

    return commands.check(predicate)


class Staff(commands.Cog):
    def __init__(self, bot, provided_admins):
        self.bot = bot
        global admins
        admins = provided_admins

    @commands.command(
        name='stop',
        aliases=['shutdown'],
        description='This is a staff only command to stop the bot'
    )
    @is_staff()
    async def stop_bot(self, ctx):
        """Shutdown the bot"""
        await ctx.send('Oh, alright... I\'ll just shutup I guess.. :wave:')
        await self.bot.close()
