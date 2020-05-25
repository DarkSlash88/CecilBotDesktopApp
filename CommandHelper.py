def test(name: str):
    return f"Test worked {name}!"


async def hello(ctx):
    await ctx.channel.send(f"Hi {ctx.author.name}!")