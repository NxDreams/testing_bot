#Test2
import interactions
import discord
from discord.ext import commands
from discord.utils import get
from discord_components import Button, ButtonStyle, Select, SelectOption, DiscordComponents


token = "OTkwMDU2NjM3MzEyMTQ3NTA2.GXdvTl.ViEbVupv02eCCrs1gMvYLqgaNvCUeCemNluuSc"
client = commands.Bot(command_prefix="!")
bot = interactions.Client(token)
guild_id = 941185846655205418

@bot.event
async def on_message(message):

    msg = message.content

    if msg == 'hello':
        await message.channel.send("Hello! :)")

@bot.command(
    name = "ranks",
    description="Displays all the military ranks.",
    scope = guild_id,
    options = [
        interactions.Option(
            name = 'branch',
            description="Choose a military branch",
            type = interactions.OptionType.STRING,
            required = False,
            choices = [
                interactions.Choice(name="Air Force", value="Air Force"),
                interactions.Choice(name="Army",value="Army"),
                interactions.Choice(name="Coast Guard", value="Coast Guard"),
                interactions.Choice(name="Marine Corps",value="Marine Corps"),
                interactions.Choice(name="Navy", value="Navy"),
                interactions.Choice(name="Space Force", value="Space Force"),
            ]
        ),
        interactions.Option(
            name='pay_grade',
            description='Ranks Paygrade',
            type = interactions.OptionType.STRING,
            required = False,
            choices = [
                interactions.Choice(name="E1", value="E1"),
                interactions.Choice(name="E2",value="E2"),
                interactions.Choice(name="E3", value="E3"),
                interactions.Choice(name="E4",value="E4"),
                interactions.Choice(name="E5", value="E5"),
                interactions.Choice(name="E6", value="E6"),
                interactions.Choice(name="E7", value="E7"),
                interactions.Choice(name="E8",value="E8"),
                interactions.Choice(name="E9", value="E9"),
                interactions.Choice(name="O1", value="O1"),
                interactions.Choice(name="O2",value="O2"),
                interactions.Choice(name="O3", value="O3"),
                interactions.Choice(name="O4",value="O4"),
                interactions.Choice(name="O5", value="O5"),
                interactions.Choice(name="O6", value="O6"),
                interactions.Choice(name="O7", value="O7"),
                interactions.Choice(name="O8",value="O8"),
                interactions.Choice(name="O9", value="O9"),
                interactions.Choice(name="O10",value="O10"),
                interactions.Choice(name="O11", value="O11"),
            ]

        )
    ]
)
async def cmd (ctx: interactions.CommandContext, branch: str=None, pay_grade:str=None):

    if branch == None and pay_grade == None:
        embed = discord.Embed(title='Testing',color=0x000080)
        await ctx.send(embed=embed)

    if branch == "Marine Corps" or branch == "Space Force" and pay_grade == "O11":
        await ctx.send(':warning: Niether the Marine Corps or Space Force has an O11.')

    if branch == "Army" and pay_grade == None:
        
        await ctx.send("**Army Enlisted Ranks:**\n\n**E1:** Private 1\n**E2:** Private 2\n**E3:** Private First Class\n**E4:** Corporal and Specialist\n**E5:** Sergeant\n**E6:** Staff Sergeant\n**E7:** Sergear First Class\n**E8:** Master Sergeant and First Sergeant\n**E9:** Sergeant Major, Command Sergeant Major, Sergeant Major of the Army\n\n**Army Officer Ranks:**\n\n**O1:** 2nd Lieutenant\n**O2:** 1st Lieutenant\n**O3:** Captain\n**O4:** Major\n**O5:** Lieutenant Colonel\n**O6:** Colonel\n**O7:** Bridgadier General\n**O8:** Major General\n**O9:** Lieutenant General\n**O10:** General\n**O11:** General of the Army")

@bot.command(
    name="clan_links",
    description="Displays all of Kings Caverns clan links",
    scope=guild_id,
    options=[
        interactions.Option(
            name="clan",
            description='Provide the clan link',
            type = interactions.OptionType.STRING,
            required = False,
            choices =[
                interactions.Choice(name='BA',value="BA"),
                interactions.Choice(name="CC2", value='CC2'),
                interactions.Choice(name='FH',value='FH'),
                interactions.Choice(name='KC',value='KC'),
            ]
        )
    ]
)
async def clan(ctx:interactions.CommandContext, clan: str=None):
    if clan == None:
        await ctx.send("**Here are all of the Kings Cavern alliance clan links:**\n\n**BackAgain?:** https://link.clashofclans.com/en?actions=OpenClanProfile&tag=29LL9QGCJ\n**Kings Cavern:** https://link.clashofclans.com/en?actions=OpenClanProfile&tag=2LUR0RPVU\n**CraigsCrushers2:** https://link.clashofclans.com/en?actions=OpenClanProfile&tag=9U02R00C\n**FoxHound:** https://link.clashofclans.com/en?actions=OpenClanProfile&tag=98LUCVPJ")
    elif clan == "BA":
        await ctx.send("BA: https://link.clashofclans.com/en?actions=OpenClanProfile&tag=29LL9QGCJ")
    elif clan == "KC":
        await ctx.send("KC: https://link.clashofclans.com/en?actions=OpenClanProfile&tag=2LUR0RPVU")
    elif clan == 'CC2':
        await ctx.send("CC2: https://link.clashofclans.com/en?actions=OpenClanProfile&tag=9U02R00C")
    elif clan == "FH":
        await ctx.send("FH: https://link.clashofclans.com/en?actions=OpenClanProfile&tag=98LUCVPJ")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Help me"))

client.run(token)
bot.start()

