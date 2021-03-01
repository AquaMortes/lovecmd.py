@bot.command()

async def love(ctx, member:discord.Member=None):

    love = random.randint(0, 100)

    embed = discord.Embed(title="Love :heart:", description=f"{member} und {member.mention} passen zu {love}% zusammen")

    

    await ctx.send(embed=embed)
