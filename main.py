import discord
from discord.ext import commands
from discord.ui import Button, View
import questionBank

# Connecting to Discord
intents = discord.Intents.all()
trivia = commands.Bot(command_prefix="!", intents=intents)

# Dictionary to keep track of server-specific data
server_data = {}

# Options: All the shows the user may pick from and the questions available
option = {
    "blackclover": 58, "bleach": 42, "cote": 62, "eminanceinshadow": 43,
    "genshin": 46, "intiald": 53, "naruto": 50, "onepiece": 42,
    "roshidere": 42, "toradora": 43
}

# Introduction command
@trivia.command()
async def hello(ctx):
    await ctx.send("**Hello! I am the anime Trivia bot. I give out quizzes on various anime. Type the command '!more' for more details**")

# Options command
@trivia.command()
async def options(ctx):
    await ctx.send("These are the list of anime options to choose from")
    await ctx.send(f"**{list(option.keys())}**")

# Instruction command
@trivia.command()
async def more(ctx):
    instructions = (
        "**I provide anime quizzes on various anime. To play, simply type '!anime [anime]' and the questions will be asked.**\n"
        "**To answer the questions, just type '!answer [letter of choice]'.**\n"
        "**To see your current score, use the command '!current'.**\n"
        "**To see your history of scores, use the command '!history [anime name]'.**\n"
        "**If you would like to explore anime options, use the command '!options'.**"
    )
    await ctx.send(instructions)

# Outputs the question and answer choices
@trivia.command()
async def anime(ctx, anime):
    server_id = str(ctx.guild.id)
    image = f"pictures/{anime}.png"

    instructions = (f"**This is the {anime} quiz game.**\n"
                    "-----------------------------------\n\n"
                    "**Click 'join' to join the game (all members must join or answers will not be recorded).**\n"
                    "**To continue, click 'next'. To answer, use '!answer [letter of choice]'.**\n"
                    "-----------------------------------\n\n")

    await ctx.send(file=discord.File(image))
    await ctx.send(instructions)
    await ctx.send(f"**You are the host of the game, {ctx.author.display_name}**")

    # Initialize server-specific game data
    server_data[server_id] = {
        'permissions': True,
        'choice': anime,
        'answer': '',
        'num': 0,
        'server_room': {},
        'host': ctx.author.id,
        'num_questions': questionBank.randomNum(option.get(anime))
    }


    # Define the join and next button
    join_button = Button(label="Join", style=discord.ButtonStyle.primary)
    next_button = Button(label="Next", style=discord.ButtonStyle.primary)

    async def join_callback(interaction):
        if server_id in server_data and server_data[server_id]['permissions']:

            await interaction.response.send_message(f"**You have joined, {interaction.user.display_name}**", ephemeral=True)
            server_data[server_id]['server_room'][interaction.user.id] = 0

        else:
            await interaction.response.send_message("**You cannot join at this time**", ephemeral=True)
    
    async def next_callback(interaction):
        if server_id in server_data and interaction.user.id == server_data[server_id]['host'] and interaction.user.id in server_data[server_id]['server_room']:
            await send_question(interaction, server_id)
        else:
            await interaction.response.send_message("**You are not the host or you have not joined the room**", ephemeral=True)
    
    join_button.callback = join_callback
    next_button.callback = next_callback

    # Create a View and add the button
    view = View()
    view.add_item(join_button)
    view.add_item(next_button)

    # Send the message with the view
    await ctx.send(view=view)

# Tells the User their current score
@trivia.command()
async def current(ctx):

    server_id = str(ctx.guild.id)

    if server_id in server_data and ctx.author.id in server_data[server_id]['server_room']:

        score = server_data[server_id]['server_room'][ctx.author.id]
        num = server_data[server_id]['num']
        await ctx.send(f"**Your current score is: {score}/{num-1}**")

    else:
        await ctx.send("**You are not part of this round of the quizzes or the game has not started.**")


# Ends the game, resets everything
@trivia.command()
async def end(ctx):

    server_id = str(ctx.guild.id)
    if server_id in server_data and ctx.author.id == server_data[server_id]['host']:

        await ctx.send("**The game is over!**")
        leaderboard_message = get_leaderboard(server_id, ctx)
        await ctx.send("**Players | Score**")
        await ctx.send("**---------------------------------**")
        await ctx.send(f"{leaderboard_message}\n")
        reset(server_id)

    else:
        await ctx.send("You cannot end the game since you're not the host")

# Helper function to send the next question
async def send_question(interaction, server_id):

    results = questionBank.question(server_data[server_id]['choice'], server_data[server_id]['num_questions'],server_data[server_id]['num'])

    server_data[server_id]['permissions'] = False  # Close the server rooms

    for row in results:
        question, answer1, answer2, answer3, correct_answer = row
        server_data[server_id]['answer'] = correct_answer

        #Creating the buttons
        next_button = Button(label="Next", style=discord.ButtonStyle.primary)
        A_button = Button(label="A", style=discord.ButtonStyle.green, custom_id = "A")
        B_button = Button(label="B", style=discord.ButtonStyle.red, custom_id = "B")
        C_button = Button(label="C", style=discord.ButtonStyle.grey, custom_id = "C")

        async def next_callback(interaction):
            if server_id in server_data and interaction.user.id == server_data[server_id]['host']:

                await send_question(interaction, server_id)

            else:

                await interaction.response.send_message("**You are not the host or you have not joined the room**", ephemeral=True)

        async def answer_callback(interaction):

            await checkanswer(server_id, interaction)

        next_button.callback = next_callback
        A_button.callback = answer_callback
        B_button.callback = answer_callback
        C_button.callback = answer_callback

        view = View()
        view.add_item(next_button)
        view.add_item(A_button)
        view.add_item(B_button)
        view.add_item(C_button)

        await interaction.response.send_message(f"{question}\n{answer1}\n{answer2}\n{answer3}", view=view)
        server_data[server_id]['num'] += 1

#checks if the user chose the right answer
async def checkanswer(server_id, interaction):

    if server_id in server_data and interaction.user.id in server_data[server_id]['server_room']:


        if interaction.data['custom_id'].strip().upper() == server_data[server_id]['answer'].strip().upper():

            await interaction.response.send_message("Correct!")
            server_data[server_id]['server_room'][interaction.user.id] += 1  # Increment score if correct

        else:

            await interaction.response.send_message(f"Incorrect! The answer was {server_data[server_id]['answer']}", ephemeral = True)
    else:
        await interaction.response.send_message("You are not part of this round of the quizzes")



# Helper function to reset the game data
def reset(server_id):

    for user_id in server_data[server_id]['server_room']:
        questionBank.insertResults(str(user_id),server_data[server_id]['server_room'][user_id],server_data[server_id]['num'],
           server_data[server_id]['choice']
        )

    server_data[server_id] = {
        'permissions': False,
        'choice': "",
        'answer': '',
        'num': 0,
        'server_room': {},
        'host': 0,
        'num_questions': 0
    }

# Helper function to get the leaderboard
def get_leaderboard(server_id, ctx):

    sorted_scores = sorted(server_data[server_id]['server_room'].items(), key=lambda item: item[1], reverse=True)
    leaderboard_message = ""

    for user_id, score in sorted_scores:

        member = ctx.guild.get_member(int(user_id))
        username = member.display_name 
        leaderboard_message += f"{username}: {score}/{server_data[server_id]['num']}\n"

    return leaderboard_message

# The User's history regarding the game so far
@trivia.command()
async def history(ctx, anime):

    result1, result2 = questionBank.getHistory(ctx.author.id, anime)
    await ctx.send(f"You have gotten {result1}/{result2} in the {anime} quiz game")







#A unique token that connects to the discord bot
trivia.run("-----")
