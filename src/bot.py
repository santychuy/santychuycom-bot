import discord
from discord.ext import commands

from utils.meeting import handle_meeting_button, meeting

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.command()
async def repeat(ctx: commands.Context, times: int, content="repeating..."):
    """Repeats a message multiple times."""
    for _ in range(times):
        await ctx.send(content)


@repeat.error
async def repeat_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.BadArgument):
        await ctx.send(
            "El argumento pasado no es el que se espera, debe ser un numero, \nPor ejemplo: `!coach repeat 3 f*ck`"
        )


@bot.command()
async def meeting(ctx: commands.Context):
    embed = discord.Embed(
        title="Agendar una reunión con Santiago Carrasco",
        description="Selecciona una plataforma que quisieras llevar la reunión",
        color=0x242A2A,
    )
    zoom_btn = discord.ui.Button(
        label="Zoom", custom_id="zoom", style=discord.ButtonStyle.primary
    )
    meet_btn = discord.ui.Button(
        label="Google Meet",
        custom_id="meet",
        style=discord.ButtonStyle.primary,
    )
    discord_btn = discord.ui.Button(
        label="Discord", custom_id="discord", style=discord.ButtonStyle.primary
    )

    zoom_btn.callback = handle_meeting_button
    meet_btn.callback = handle_meeting_button
    discord_btn.callback = handle_meeting_button

    view = discord.ui.View().add_item(zoom_btn).add_item(meet_btn).add_item(discord_btn)

    await ctx.send(embed=embed, view=view, delete_after=60)
