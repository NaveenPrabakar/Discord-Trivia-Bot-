import discord
from discord.ext import commands

intents = discord.Intents.all()
triviea = commands.Bot(command_prefix = "!", intents=intents)

command1 = "!more" #command for instructions
command2 = "!wrong"


@triviea.event
async def on_ready():
    print("Bot is Run")

@triviea.command()
async def hello(ctx):
    await ctx.send("hello! I am the anime Trivia bot. I give out quizzes on various anime. Type the command '!more' for more details")
    await ctx.send("hello numan, typical, jamz, saber. I am Trivia Bot. My creator is boruto show")

@triviea.command()
async def more(command1):

    await command1.send("I provide anime quizzes to various anime. To play simply type '!' and the anime and questions will be asked")
    await command1.send("To answer the questions just type '!' and the letter of your answer")

@triviea.command()
async def wrong(command2):
    
    imagepath = r"C:\Users\nvnpr\OneDrive\Pictures\Screenshots\Screenshot 2024-07-20 202714.png"
    await command2.send(file=discord.File(imagepath))


triviea.run("MTI2NDM3NjM3NTM2ODg4MDIxMA.G02wFL.0Vzx1NMf_mHCLGDDHVFiqNJBBpOfQ69I36N89E")