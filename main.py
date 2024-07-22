import discord
from discord.ext import commands
import questionBank

# Connecting to Discord
intents = discord.Intents.all()
triviea = commands.Bot(command_prefix="!", intents=intents)

# Dictionary to keep track of server-specific data
server_data = {}

# For testing purposes to see if the bot is running
@triviea.event
async def on_ready():

    print("Bot is running")

# Introduction command
@triviea.command()
async def hello(ctx):
    await ctx.send("Hello! I am the anime Trivia bot. I give out quizzes on various anime. Type the command '!more' for more details")

    await ctx.send("Hello numan, typical, jamz, saber. I am Trivia Bot. My creator is boruto show")

# Instruction command
@triviea.command()
async def more(ctx):
    await ctx.send("I provide anime quizzes on various anime. To play, simply type '!anime [anime]' and the questions will be asked.")

    await ctx.send("To answer the questions, just type '!answer [letter of choice]'.")

    await ctx.send("To see your current score, use the command '!current'.")

# Outputs the question and answer choices
@triviea.command()
async def anime(ctx, anime):
    server_id = str(ctx.guild.id)
    image = f"{anime}.png" 

    await ctx.send(file=discord.File(image))
    await ctx.send("This is the current anime quiz game.")
    await ctx.send("Type '!join' to join the game (all members must join or answers will not be recorded).")
    await ctx.send("To continue, type '!next'. To answer, use '!answer [letter of choice]'.")
    await ctx.send(f"You are the host of the game, {ctx.author.display_name}")

    # Initialize server-specific game data
    if server_id not in server_data:

        server_data[server_id] = {
            'permissions': True,
            'choice': anime,
            'answer': '',
            'num': 0,
            'server_room': {},
            'host': ctx.author.id
        }

    else:
        server_data[server_id]['permissions'] = True

        server_data[server_id]['choice'] = anime

        server_data[server_id]['host'] = ctx.author.id

# Joins the "server room" to play the game
@triviea.command()
async def join(ctx):
    server_id = str(ctx.guild.id)
    if server_id in server_data and server_data[server_id]['permissions']:

        await ctx.send(f"You have joined, {ctx.author.display_name}")

        server_data[server_id]['server_room'][ctx.author.id] = 0

    else:

        await ctx.send("You cannot join at this time")

# Tells the User their current score
@triviea.command()
async def current(ctx):

    server_id = str(ctx.guild.id)
    if server_id in server_data and ctx.author.id in server_data[server_id]['server_room']:

        score = server_data[server_id]['server_room'][ctx.author.id]

        num = server_data[server_id]['num']

        await ctx.send(f"Your current score is: {score}/{num}")

    else:
        await ctx.send("You are not part of this round of the quizzes or the game has not started.")

# Moves on to the next question and saves what is the correct answer
@triviea.command()
async def next(ctx):
    server_id = str(ctx.guild.id)
    if server_id in server_data and ctx.author.id == server_data[server_id]['host']:

        server_data[server_id]['num'] += 1

        server_data[server_id]['permissions'] = False  # Close the server rooms

        results = questionBank.question(server_data[server_id]['choice'])

        for row in results:
            question = row[0]

            answer1 = row[1]

            answer2 = row[2]

            answer3 = row[3]

            server_data[server_id]['answer'] = row[4]

            await ctx.send(f"{question}\n{answer1}\n{answer2}\n{answer3}")
    else:
        await ctx.send("You are not the host or you have not joined the room")



# Checks if the user's answer is correct (FIX THE SCORING SYSTEM)
@triviea.command(aliases=['A', 'B', 'C'])
async def answer(ctx, user_answer: str):

    server_id = str(ctx.guild.id)

    if server_id in server_data and ctx.author.id in server_data[server_id]['server_room']:

        if user_answer.strip().upper() == server_data[server_id]['answer'].strip().upper():

            await ctx.send("Correct!")
            server_data[server_id]['server_room'][ctx.author.id] += 1

        else:
            await ctx.send("Incorrect!")
            await ctx.send(f"The correct answer was {server_data[server_id]['answer']}")
    else:
        await ctx.send("You are not part of this round of the quizzes")

# Turn off the bot
@triviea.command()
async def off(ctx):
    await ctx.send("Shutting down...")
    await ctx.close()
    

#A unique token that connects to the discord bot
triviea.run("-----")
