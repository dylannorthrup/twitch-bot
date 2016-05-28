from src.config.config import *

commands = {
  '!test': {
    'limit': 1,
    'return': 'This is a test!'
  },

# '!randomemote': {
#   'limit': 180,
#   'argc': 0,
#   'return': 'command'
# },
#
# '!wow': {
#   'limit': 30,
#   'argc': 3,
#   'return': 'command'
# },

###WORKERBOT COMMANDS
  '!card': {
    'limit': -1,
    'argc': -1,
    'return': 'command'
  },

  '!now': {
    'limit': 0,
    'argc': 0,
    'return': 'command'
  },

  '!equip': {
    'limit': 0,
    'argc': 0,
    'return': 'command'
  },
  '!legend': {
    'limit': 0,
    'argc': 0,
    'return': 'command'
  },
  '!gem': {
    'limit': 0,
    'argc': 0,
    'return': 'command'
  },
  '!keyword': {
    'limit': 0,
    'argc': 0,
    'return': 'command'
  },
  '!price': {
    'limit': 0,
    'argc': 0,
    'return': 'command'
  },
  '!decks': {
    'argc': 1,
    'return': 'command'
  },
  '!ptg': {
    'argc': 1,
    'return': 'command'
  },
  '!gtp': {
    'argc': 1,
    'return': 'command'
  },
  '!ratio': {
    'argc': 0,
    'return': 'command'
  },
  '!join': {
    'argc': 0,
    'return': 'command'
  },
  '!leave': {
    'argc': 0,
    'return': 'command'
  },
  '!whispers': {
    'argc': 1,
    'return': 'command'
  },
  '!streams': {
    'argc': 0,
    'return': 'command'
  },
  '!setign': {
    'argc': 1,
    'return': 'command'
  },
  '!ign': {
    'argc': 1,
    'return': 'command'
  },
  '!img': {
    'argc': 1,
    'return': 'command'
  },
  '!info': {
    'limit': 10,
    'return': 'Hi, I am WorkerBot. I can find card/equipment text and auction house values by using !card/!equip/!price "cardname". I keep track of HEX: Shards of Fate in game names. Type !setign "ign" to link your twitch username to your IGN.'
  },
  # Show some information about the thing
  '!about': {
    'limit': 10,
    'return': 'Version 2.0 | For more information go to twitch.tv/workerbot | Thanks Celendine, Dinotropia, Veetorp and DylanNorthrup for the data | Images hosted by Thepsis | Coded in Python by DylanNorthrup (based on previous version written by Skaro and Risterral.'
  },
  # Donate page
  '!donate': {
    'limit': 20,
    'return': 'Donate to WorkerBot at https://www.twitchalerts.com/donate/workerbot'
  },
  # Pimp the shardshopper page
  '!shardshopper': {
    'limit': 30,
    'return': 'Check out ShardShopper at http://fiveshards.com/shard-shopper/'
  },
  # Give a link to where folks can look at loot tables DYANMIC
  '!pveloot': {
    'argc': 0,
    'return': 'command'
  },
  # Show the folks where they can download the client
  '!download': {
    'limit': 30,
    'return': 'Download HEX: Shards of Fate at http://www.hextcg.com/client-download/'
  },
  # Show the folks where they can register for a Hex account
  '!register': {
    'limit': 30,
    'return': 'Register your HEX: Shards of Fate account at http://us.hex.gameforge.com/account.html#/#registration'
  },
  # Give a shout out to whatever stuff we want to have run DYNAMIC
  '!shoutout': {
    'argc': 0,
    'return': 'command'
  },
  # Tell us if there's a holiday going on  DYNAMIC
  '!holiday': {
    'argc': 0,
    'return': 'command'
  },
  # Pimp the Hex Collection spreadsheet
  '!hexcollection': {
    'limit': 30,
    'return': ' Are you a collector at heart? We have a tool that will collect everything automagically! Check it out here: http://board.hex.gameforge.com/index.php?thread/49461-updated-hex-collection-tool-hex-collection-thingajiggy/'
  },

  '!hello': {
    'limit': 2,
    'return': 'Howdy!'
  }

}


for channel in config['channels']:
  for command in commands:
    commands[command][channel] = {}
    commands[command][channel]['last_used'] = 0
