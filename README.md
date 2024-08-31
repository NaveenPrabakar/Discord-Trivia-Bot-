# Discord Anime Trivia Bot

## Overview

The Discord Anime Trivia Bot is a versatile bot that brings anime-themed trivia quizzes to Discord servers. It supports multiple servers, manages user scores, and offers multilingual quiz experiences using Google Translate API. The bot uses efficient data structures and MySQL for persistent storage, ensuring a smooth and scalable user experience.

## Features

- **Multi-Server Support:** Operates across multiple Discord servers concurrently, with each server maintaining its own set of quiz data.
- **Diverse Anime Topics:** Offers trivia questions on various anime series, such as "Black Clover," "Bleach," "Naruto," "One Piece," and "Attack on Titan."
- **Real-Time Score Tracking:** Tracks scores in real-time using Python dictionaries, allowing users to view their scores and compete on leaderboards.
- **Translation Support:** Utilizes the Google Translate API to translate questions into different languages, making the quiz accessible to non-English speakers.
- **Persistent Data Storage:** MySQL is used to store quiz questions, user scores, and other data, ensuring progress is saved and retrievable even after bot restarts.
- **Docker Integration:** The bot is containerized using Docker, simplifying deployment and ensuring consistency across environments.

## Data Structures

- **Dictionaries (`dict`):**
  - **`server_data`:** Manages server-specific data, such as active quizzes and user scores. Each key represents a server ID, with the value being another dictionary containing quiz data for that server.
  - **`option`:** Maps anime names to the number of available questions, allowing the bot to dynamically fetch questions based on the user's choice.
 
 ![Screenshot 2024-08-31 102233](https://github.com/user-attachments/assets/a7d64e62-2d17-40eb-bb35-6d8c838ab1d1)
 ![Screenshot 2024-08-31 102243](https://github.com/user-attachments/assets/877db7ea-eb1c-4e9c-93c9-aa07f37bea1a)



- **Lists (`list`):**
  - **`questions_list`:** Stores questions fetched from the database for the current quiz. This list is shuffled and iterated through as users answer questions.
  - **`participants`:** Maintains a list of users participating in the quiz, enabling the bot to track who has answered and update scores accordingly.

  
 

## Setup Instructions

### Prerequisites

- Python 3.x
- MySQL Server
- Docker (optional for containerization)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NaveenPrabakar/Discord-Anime-Trivia-Bot.git
   cd Discord-Anime-Trivia-Bot

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Set Up the MySQL Database:**
   ```bash
   source /path/to/QuizTables.sql;
   source /path/to/LoadQuestions.sql;

4. **Congfigure the bot:**
   ```env
   DISCORD_TOKEN=your_discord_bot_token

5. **Set up your MySQL connection details in main.py:**
   ```python
   connection = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database"
   )

6. **Run the Bot:**
   ```bash
   python main.py

7. **Build Docker container:**
   ```bash
   docker build -t discord-trivia-bot .
   docker run -d discord-trivia-bot

## Usage

### Commands

- **!hello**: Greets the user and provides an introduction to the bot.
- **!options**: Displays a list of available anime topics for the quiz.
- **!quiz [anime_name]**: Starts a quiz on the specified anime. The bot uses the **!options** dictionary to retrieve and present questions.
- **!history [anime_name]**: Provides the User's history of what scores they have had so far in that anime
- **!language [language]**: Translates questions to the User's language preference

### Host commands

- **!end**: ends the on going game
- **Next Button**: Goes to the next question

### UI
![image](https://github.com/user-attachments/assets/0a481a5d-104a-47ad-af0b-894face11a32)

- Users press a button A, B or C for the answer
- If the answer is incorrect, it will privately tell the user it was wrong
![image](https://github.com/user-attachments/assets/fcd8c905-2207-4822-ac59-3129e28f5fc2)

- if the answer was correct, then it will say it was correct
![image](https://github.com/user-attachments/assets/b4816376-7e0d-441d-ba01-f7f701fbbae8)

-if only the host of the game can click next to continue the game





## Project Structure

- **main.py**: The main script that initializes the bot, defines commands, and manages server-specific data and interactions.
- **questionBank.py**: Handles the database operations, including fetching questions and storing new entries.
- **Translate.py**: Integrates Google Translate API to translate questions into different languages based on user preference.
- **LoadQuestions.sql**: A SQL script that populates the database with initial quiz questions.
- **QuizTables.sql**: A SQL script that defines the structure of the MySQL tables used by the bot.

## Contribution

Contributions are welcome! If you have ideas for new features or improvements, please fork the repository and submit a pull request.

   

