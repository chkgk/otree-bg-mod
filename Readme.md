# Channels background tasks in oTree
## Description
I have modified oTree to run channels background tasks with the runprodserver (+1of2 / +2of2) commands.

Background tasks can be defined very much like additional websocket consumers and websocket routes in the otree_extension dir of your project. They are then automatically picked up by oTree.

Basically, with this you can have long running processes in the background that continuously create or process data and then send it to the players over websockets.

## Caveat
This currently only works if you have a redis-server running and use the runprodserver command. 

## Demo
```bash
git clone https://github.com/chkgk/otree-background-tasks
cd otree-core
pip install -e .
cd ..
otree runprodserver
```

## Installation 
Head over to my fork of otree-core, then follow the development setup.