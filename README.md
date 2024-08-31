# Discord Anime Trivia Bot - README.yaml

overview:
  description: >
    The Discord Anime Trivia Bot is a versatile bot that brings anime-themed trivia quizzes to Discord servers.
    It is designed to support multiple servers simultaneously, manage user scores effectively, and provide
    multilingual quiz experiences using Google Translate API. The bot uses efficient data structures and MySQL
    for persistent storage to ensure a smooth and scalable user experience.

features:
  multi_server_support: >
    The bot can operate across multiple Discord servers concurrently, with each server maintaining its own set
    of quiz data to ensure an independent trivia experience.
  diverse_anime_topics: >
    The bot offers trivia questions on various anime series, such as "Black Clover," "Bleach," "Naruto," "One Piece,"
    "Attack on Titan," and more.
  real_time_score_tracking: >
    Scores are tracked in real-time using Python dictionaries, allowing users to view their scores and compete
    on leaderboards.
  translation_support: >
    Questions can be translated into different languages using the Google Translate API, making the quiz accessible
    to non-English speakers.
  persistent_data_storage: >
    MySQL is used to store quiz questions, user scores, and other relevant data, ensuring that progress is saved
    and can be retrieved even after the bot is restarted.
  docker_integration: >
    The bot is containerized using Docker, which simplifies deployment and ensures consistency across different
    environments.

data_structures:
  dictionaries:
    server_data: >
      This dictionary is used to manage server-specific data, such as active quizzes and user scores. Each key
      represents a server ID, and the value is another dictionary containing the quiz data for that server.
    option: >
      A dictionary mapping anime names to the number of available questions. This allows the bot to dynamically
      fetch questions based on the user's choice.
  lists:
    questions_list: >
      Stores the questions fetched from the database for the current quiz. This list is shuffled and iterated
      through as users answer questions.
    participants: >
      Maintains a list of users participating in the quiz, enabling the bot to track who has answered and update
      scores accordingly.
  priority_queue:
    min_heap: >
      Used for efficiently managing and retrieving the top scores for the leaderboard. The smallest scores are
      kept at the root, allowing quick access to the best players.

setup_instructions:
  prerequisites:
    - Python 3.x
    - MySQL Server
    - Docker (optional for containerization)
  installation:
    - step: Clone the repository
      command: |
        git clone https://github.com/NaveenPrabakar/Discord-Anime-Trivia-Bot.git
        cd Discord-Anime-Trivia-Bot
    - step: Install dependencies
      command: |
        pip install -r requirements.txt
    - step: Set up the MySQL database
      sub_steps:
        - step: Import the SQL schema from QuizTables.sql
          command: |
            source /path/to/QuizTables.sql;
        - step: Load quiz questions using LoadQuestions.sql
          command: |
            source /path/to/LoadQuestions.sql;
    - step: Configure the bot
      sub_steps:
        - step: Create a .env file and add your Discord bot token
          command: |
            DISCORD_TOKEN=your_discord_bot_token
        - step: Set up your MySQL connection details in main.py
          command: |
            connection = mysql.connector.connect(
              host="your_host",
              user="your_user",
              password="your_password",
              database="your_database"
            )
    - step: Run the bot
      command: |
        python main.py
    - step: Optional - Docker Setup
      sub_steps:
        - step: Build and run the Docker container
          command: |
            docker build -t discord-trivia-bot .
            docker run -d discord-trivia-bot

usage:
  commands:
    - name: "!hello"
      description: Greets the user and provides an introduction to the bot.
    - name: "!options"
      description: Displays a list of available anime topics for the quiz.
    - name: "!quiz [anime_name]"
      description: >
        Starts a quiz on the specified anime. The bot uses the `option` dictionary to retrieve and present questions.
    - name: "!score"
      description: Shows the user's current score, tracked in the `server_data` dictionary.
    - name: "!leaderboard"
      description: Displays the top scores, managed by the `min_heap` priority queue.
  admin_commands:
    - name: "!add_question [anime_name] [question] [correct_option] [wrong_option_1] [wrong_option_2] [wrong_option_3]"
      description: Adds a new question to the database.
    - name: "!remove_question [anime_name] [question_id]"
      description: Removes a question from the database.

project_structure:
  - file: "main.py"
    description: The main script that initializes the bot, defines commands, and manages server-specific data and interactions.
  - file: "questionBank.py"
    description: Handles the database operations, including fetching questions and storing new entries.
  - file: "Translate.py"
    description: Integrates Google Translate API to translate questions into different languages based on user preference.
  - file: "LoadQuestions.sql"
    description: A SQL script that populates the database with initial quiz questions.
  - file: "QuizTables.sql"
    description: A SQL script that defines the structure of the MySQL tables used by the bot.

contribution:
  description: >
    Contributions are welcome! If you have ideas for new features or improvements, please fork the repository and submit a pull request.




