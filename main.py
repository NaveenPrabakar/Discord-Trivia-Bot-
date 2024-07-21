import discord
from discord.ext import commands

import questionBank

#Connecting to discord
intents = discord.Intents.all()
triviea = commands.Bot(command_prefix = "!", intents=intents)

command1 = "!more" #command for instructions

command2 = "!cote" #command to start quiz

command3 = "!off" #turn off bot

Introduction = False #Boolean for true or false


#For testing purposes to see if the bot is running
@triviea.event
async def on_ready():
    print("Bot is Run")

#Introduction commmand
@triviea.command()
async def hello(ctx):
    await ctx.send("hello! I am the anime Trivia bot. I give out quizzes on various anime. Type the command '!more' for more details")
    await ctx.send("hello numan, typical, jamz, saber. I am Trivia Bot. My creator is boruto show")

#Instruction command
@triviea.command()
async def more(command1):

    await command1.send("I provide anime quizzes to various anime. To play simply type '!' and the anime and questions will be asked")
    await command1.send("To answer the questions just type '!' and the letter of your answer")

#Outputs the question and answer choices
@triviea.command()
async def cote(command2):

    
    image = "cote.png" #FIX IMAGE ISSUE
    await command2.send(file = discord.File(image))
    await command2.send("This is the cote anime quiz game")

    num, results = questionBank.question(command2)
    answer = "" # the correct answer
    for row in results:
        question = row[0]
        answer1 = row[1]
        answer2 = row[2]
        answer3 = row[3]
        answer = row[4]
        await command2.send(f"{question}\n {answer1} \n {answer2} \n {answer3}")


#Turn off the bot
@triviea.command()
async def off(command3):
    await command3.send("Shutting down...")
    await command3.close()
    

#A unique token that connects to the discord bot
triviea.run("-----")
