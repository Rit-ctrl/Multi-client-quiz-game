# Multi-client-quiz-game

This repo is an implementation of a multiplayer quiz game using socket programming.

## Introduction

TCP/IP was used to create the application stack. Python was chossen, due to its easy to code nature.

## Rules:

1. Game starts once the maximum number of players have joined.
2. Questions are sent to the players with options.
3. Players need to answer the question within 60 secs.
4. If a player fails to answer within the time limit or answers with the wrong answer, the player will get kicked out.
5. At the end, players who have answered all the questions can see the leaderboard. The leaderboard is set according to the average time taken by a player to answer a question.

## Configuring the game

### Questions:

One can edit the questions in the game by editing the question.csv file.

##### NOTE:
Do not remove the first and last lines of the question.csv file.

##### Format
The questions and options should be in the following format:
```
<question number>,<question>,<option a>,<option b>,<option c>,<option d>,<ans: correct option>
```

### Players, IP Address and PORT

```line __:``` defines the total number of players.  
```line __:``` defines the IP Address of the server.  
```line __:``` defines the Port the server is connected to.

## Starting the game
Run the following
```
python3 server.py
```

## Joining the game
Run the following
```
python3 client.py
```
Enter the correct Host IP Address and Port to join the game.
