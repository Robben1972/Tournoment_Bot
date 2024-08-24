# University Tournament Management

This project is designed to manage the registration and randomization of players for the University Tournament. It consists of a Django REST backend and two Telegram bots. The first bot is used for registering users, and the second one is for randomizing the registered users, which is intended for admin use only.

## Features

- **User Registration Bot**: Registers players for the tournament.
- **User Randomization Bot**: Randomizes the registered players, available only to admins.
- **Django REST Backend**: Handles the API endpoints for player management, match management, and rewards.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:Robben1972/Tournoment_Bot.git
cd repo-name
```

### 2. Create a Virtual Environment

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

Create a `.env` file in the root directory of the project and add the following environment variables:

```env
REGISTRATION_TOKEN=registration_bot_token
API_LINK=http://127.0.0.1:8000/api/player/
RANDOMISE_TOKEN=randomise_bot_token
WINNER_API=http://127.0.0.1:8000/api/winner/
OPPONENT_API=http://127.0.0.1:8000/api/opponent/
LOOSER_API=http://127.0.0.1:8000/api/looser/
REWARD_API=http://127.0.0.1:8000/api/reward/
```

Replace the placeholder values with your actual bot tokens and API links.

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start the Django Development Server

```bash
python manage.py runserver
```

### 7. Run the Telegram Bots

To start the bots, use the following commands in separate terminals:

```bash
python registration_bot.py
python randomise_bot.py
```

## Usage

1. **User Registration**: Players register for the tournament using the Registration Bot.
2. **User Randomization**: Admins can randomize the registered players using the Randomization Bot.
