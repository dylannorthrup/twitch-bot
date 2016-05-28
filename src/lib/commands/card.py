#!/usr/bin/env python
# coding: utf8



#try:
#  import requests
#except ImportError:
#  print "DEBUG: Couldn't import requests. Ignore this if you're calling the library directly"

import requests

#def card_info(jblob):
#  j = jblob
#  return r_val

def card(*args):
  usage = 'Usage: !card <card name>'
  if len(args) < 1:
    return usage

#  for e in args[0]:
#    print "element: %s" % e

#  print "DEBUG: args -> %s" % (", ".join(args[0]))

  card_name = ""
  card_search_param = ""
  for thing in args[0]:
    print thing
    if card_name == "":
      card_name = thing
    else:
      card_name = "%s %s" % (card_name, thing)
      card_search_param = "%s+%s" % (card_search_param, thing)

  print 'DEBUG: Card name is <%s>' % card_name
  url = 'http://doc-x.net/hex/search.rb?output_format=json&type=Troop|Action|Constant|Shard|Artifact&name=%s' % card_search_param
  
  try:
    print "Trying to connect to %s" % url
    raw_cards = requests.get(url)
  except:
    return 'Error connecting to url %s' % url

  try:
    cards = raw_cards.json()
    cards = cards['cards']
  except:
    return "Couldn't parse the JSON from raw_cards: " % raw_cards

  # Set up what we're going to return from this
  r_string = "Found multiple cards: "

  print cards

  # If we got multiple cards back, see if one of them is an exact match
  if len(cards) == 0:
    return "No cards found matching search '%s'." % card_name
  elif len(cards) > 1:
    print "Cards length is %d" % len(cards)
    #print cards
    for c in cards:
      # Epic cards are AA cards and we skip those for clarity
      if c['rarity'] == 'Epic':
        continue
      if c['name'].lower() == card_name.lower():
        return "%s (%s %s) cost %s (%s) - %s. \"%s\"" % (c['name'], c['set_id'], c['rarity'], c['cost'], c['threshold'], c['type'], c['text']) 
#        return card_info(c)
      r_string = "%s %s," % (r_string, c['name'])

  # Finally, return whatever we've managed to put into 'r_string' (removing the last ',' from it
  r_string = r_string[:-1]
  return(r_string)

#if __name__ == "__main__":
#  from sys import argv, path
#  path.append('/home/docxstudios/localpylibs/lib/python2.7/site-packages/')
#  path.append('/home/docxstudios/twitch-bot/')
#  from src.bot import *
#  from src.config.config import *
#  import requests
#  
#  foo = card('Kill')
#  foo = card('Arcane')
#  print foo

