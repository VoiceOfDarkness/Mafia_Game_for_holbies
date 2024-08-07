# Mafia Game
[](https://github.com/VoiceOfDarkness/Mafia_Game_for_holbies/blob/master/static/img/Screenshot_7-8-2024_124354_mafia-for-holbies-4b73ef211906.herokuapp.com.jpeg)
Welcome to the Mafia Game, a web-based version of the classic social deduction game. This project allows players to join a room, receive random roles, and play the game in real-time.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Game Rules](#game-rules)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- Create and join game rooms with a unique code.
- Randomly assigned roles for players.
- Real-time updates using Flask-SocketIO.
- Responsive design for an optimal experience on different devices.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Poetry, Flask, Flask-SocketIO, MongoDB

## Getting Started

### Prerequisites

- Poetry

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/VoiceOfDarkness/Mafia_Game_for_holbies
   cd mafia-game
   ```

2. run with python or gunicorn
   ```sh
   python app.py
   or
   gunicorn -k gevent -w 1 app:app
   ```

### Running the Application

1. Open your web browser and navigate to `http://localhost:5000` or `http://localhost:8000`.
2. Create a new game room or join an existing one using the room code.
3. Enter your name and wait for the game to start once all players have joined.

## Game Rules

- **Mafia**: Eliminate the villagers without being discovered.
- **Don**: The leader of the Mafia, working with them to eliminate villagers.
- **Doctor**: Save players from being eliminated.
- **Sheriff**: Identify and eliminate the Mafia members.
- **Maniac**: Eliminate as many players as possible.
- **Villagers**: Identify and eliminate the Mafia members.
- **Kamikaze**: Sacrifice themselves to take out a Mafia member.

## Project Structure
```
 Procfile
├── README.md
├── app.py
├── config.py
├── database.py
├── home
│   ├── __init__.py
│   ├── home.py
│   └── templates
│       └── index.html
├── host
│   ├── __init__.py
│   ├── host.py
│   └── templates
│       └── host.html
├── player
│   ├── __init__.py
│   ├── player.py
│   └── templates
│       └── player.html
├── poetry.lock
├── pyproject.toml
├── static
│   ├── css
│   │   ├── 404.css
│   │   └── styles.css
│   ├── host.html
│   ├── img
│   │   └── favicon.ico
│   └── role.html
├── templates
│   ├── 404.html
│   └── base.html
├── utils
│   ├── role.py
│   └── room_code.py
└── websock.py
```


## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## Contact
- **Email**: abil.samedov502@gmail.com
- **GitHub**: [VoiceOfDarkness](https://github.com/voiceofdarkness)
