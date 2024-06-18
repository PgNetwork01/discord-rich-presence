@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    botactivity = discord.Activity(type=discord.ActivityType.watching, name="Dert | /help")
    await bot.change_presence(activity=botactivity, status=discord.Status.do_not_disturb)
    await bot.tree.sync()

