from discord.ext import commands

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is online!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound): await ctx.send("That command is beyond my knowledge...")
        elif isinstance(error, commands.MissingRequiredArgument): await ctx.send("Looks like you're missing a few arguments?")
        elif isinstance(error, commands.BotMissingPermissions): await ctx.send("I don't have the power to do that...")
        else: await ctx.send(f"An error occurred: {error}")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

async def setup(bot):
    await bot.add_cog(test(bot))